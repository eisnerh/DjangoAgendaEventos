from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test, name='Test'),
    path('add_clients/', views.add_clients, name='add_clients'),
    path('list_of_events/', views.list_of_events, name='list_of_events'),
    path('materiales/', views.materiales, name='materiales'),
]
