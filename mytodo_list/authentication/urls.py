from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='registerpage'),
    path('login/', views.signin, name='loginpage'),
    path('logout/', views.signout, name='logout'),
]