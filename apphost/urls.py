from django.urls import path
from apphost.views import create_hosting, edit_hosting, delete_hosting, manage_host,upcoming_hosting,hosting_detail

urlpatterns = [
    path('host_list/', manage_host, name='manage-host'),
    path('create/', create_hosting, name='create-hosting'),
    path('hosting/<int:pk>/', hosting_detail, name='hosting_detail'),
    path('hosting/edit/<int:host_id>/', edit_hosting, name='edit_hosting'),
    path('hosting/delete/<int:host_id>/', delete_hosting, name='delete_hosting'),
    path('upcoming-hosting/', upcoming_hosting, name='upcoming_hosting'),
]
