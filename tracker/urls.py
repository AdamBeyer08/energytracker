from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('drinks/', views.drinks_list, name='drinks'),
    path('stats/', views.stats, name='stats'),
    path('add/', views.add_record, name='add_record'),
    path('login/', auth_views.LoginView.as_view(template_name='index.html', extra_context={'section': 'login'}), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]