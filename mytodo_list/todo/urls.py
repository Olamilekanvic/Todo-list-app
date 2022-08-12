from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    # path('done/', views.done, name='done'),
    path('task/<int:pk>/', views.edit, name='edit'),
    path('task/<int:pk>/delete', views.delete, name='delete'),
]
