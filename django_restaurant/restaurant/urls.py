from django.urls import path

from restaurant import views

urlpatterns = [
    path('sign_up', views.sign_up, name='Add User Details'),
    path('login', views.login, name='Login User'),
    path('get_menu', views.get_menu, name='Get Menu'),
    path('add_order', views.add_order, name='Add Order'),
]