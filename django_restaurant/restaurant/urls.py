from django.urls import path

from restaurant import views

urlpatterns = [
    path('sign_up', views.sign_up, name='Add User Details'),
]