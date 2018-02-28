from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test, name='Test'),
    path('add/', views.add, name='add_clients'),
]
