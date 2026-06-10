from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('drinks/', views.drinks_list, name='drinks_list'),
    path('stats/', views.stats, name='stats'),
    path('add/', views.add_record, name='add_record'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]