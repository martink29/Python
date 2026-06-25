from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('vulnerable/', views.vulnerable_page),
    path('safe/', views.safe_page),
    path('read-file-vulnerable/', views.read_file_vulnerable),
    path('read-file-safe/', views.read_file_safe),
]