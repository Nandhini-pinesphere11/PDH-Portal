from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User


from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
import random


from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode


from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.utils.encoding import force_str



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('dashboard')
        else:
            # If the user has entered an email address, we want to show the password reset form
            email = request.POST.get('username')
            if email:
                password_reset_form = PasswordResetForm({'email': email})
                if password_reset_form.is_valid():
                    password_reset_form.save(request=request)
                    return redirect('password_reset_done')
            else:
                password_reset_form = PasswordResetForm()
    else:
        form = AuthenticationForm()
        password_reset_form = PasswordResetForm()
    return render(request, 'authentication/login.html', {'form': form, 'password_reset_form': password_reset_form})


def logout(request):
    auth.logout(request)
    response = redirect('login')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})
def generate_otp():
    digits = [i for i in range(0, 10)]
    otp = ""
    for i in range(6):
        otp += str(random.choice(digits))
    return otp


User = get_user_model()

@csrf_protect
def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None
            if user is not None:
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                reset_url = f"{request.scheme}://{request.get_host()}/reset_password_confirm/{uid}/{token}/"

                # generate and send OTP to user's email
                otp = generate_otp()  # your implementation to generate OTP
                send_mail(
                    'Reset Password OTP', 
                    f'Your OTP for resetting password is {otp}', 
                    settings.EMAIL_HOST_USER, 
                    [email], 
                    fail_silently=False,
                )
                request.session['reset_password_user_id'] = user.pk
                request.session['reset_password_otp'] = otp
                request.session['reset_password_token'] = token
                messages.success(request, 'OTP sent to your email')
                return redirect('reset_password_verify_otp')
            else:
                messages.error(request, 'Email not found')
    else:
        form = PasswordResetForm()
    return render(request, 'authentication/reset_password.html', {'form': form})

@csrf_protect
def reset_password_verify_otp(request):
    user_id = request.session.get('reset_password_user_id')
    otp = request.session.get('reset_password_otp')
    token = request.session.get('reset_password_token')
    if not all([user_id, otp, token]):
        return redirect('reset_password')
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        input_otp = request.POST.get('otp')
        if input_otp == otp:
            # remove session data after successful OTP verification
            del request.session['reset_password_user_id']
            del request.session['reset_password_otp']
            del request.session['reset_password_token']
            messages.success(request, 'OTP verified')
            return redirect('reset_password_confirm', uidb64=urlsafe_base64_encode(force_bytes(user.pk)), token=token)
        else:
            messages.error(request, 'OTP verification failed')
    return render(request, 'authentication/reset_password_verify_otp.html')



def reset_password_confirm(request, uidb64, token):
    # Decode the uidb64 to get the user id and retrieve the user object
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # Verify that the token is valid
    token_generator = PasswordResetTokenGenerator()
    if user is not None and token_generator.check_token(user, token):
        # If the token is valid, render the password reset form
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                # Save the new password
                form.save()
                messages.success(request, 'Your password has been reset. You may now login with your new password.')
                return redirect('login')
        else:
            form = SetPasswordForm(user)
        return render(request, 'authentication/reset_password_complete.html', {'form': form})
    
    else:
        # If the token is invalid, display an error message
        messages.error(request, 'The password reset link is invalid or has expired.')
        return redirect('login')     
