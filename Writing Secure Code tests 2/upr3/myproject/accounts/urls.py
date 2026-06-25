from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('change-email-vulnerable/', views.change_email_vulnerable, name='change_email_vulnerable'),
    path('change-email-safe/', views.change_email_safe, name='change_email_safe'),
]