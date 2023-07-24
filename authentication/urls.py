from django.urls import path
from django.contrib.auth import views as auth_views

from .views import reset_password, reset_password_verify_otp

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('reset_password/', reset_password, name='reset_password'),
    path('reset_password_verify_otp/', reset_password_verify_otp, name='reset_password_verify_otp'),
    path('reset_password_confirm/<uidb64>/<token>/', views.reset_password_confirm, name='reset_password_confirm'),
   

   
]
