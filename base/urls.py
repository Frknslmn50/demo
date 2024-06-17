from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('poem/<str:pk>/', views.poem, name='poem')
]