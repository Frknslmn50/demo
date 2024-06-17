from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('poem/<str:pk>/', views.poem, name='poem'),
    path('create-poem/', views.createPoem, name='create-poem'),
    path('update-poem/<str:pk>/', views.updatePoem, name='update-poem')
]