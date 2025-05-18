from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('contact/', views.contanct, name='contact')
]