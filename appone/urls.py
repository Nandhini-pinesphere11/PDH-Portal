from django.urls import path
from appone import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('create_domain/', views.create_domain, name='create_domain'),
    path('domain/<int:pk>/', views.domain_detail, name='domain_detail'),
    path('domain_list/', views.manage, name='manage'),
    path('no_f_domains/', views.manage_copy, name='manage_copy'),
    path('upcoming-domains/', views.upcoming_domains, name='upcoming_domains'),
    path('send-renewal-alerts/', views.send_renewal_alerts, name='send_renewal_alerts'),
    path('send-alerts/', views.send_alerts, name='send_alerts'),
    path('domain/edit/<int:domain_id>/', views.edit_domain, name='edit_domain'),
    path('domain/delete/<int:domain_id>/', views.delete_domain, name='delete_domain'),
   

]
