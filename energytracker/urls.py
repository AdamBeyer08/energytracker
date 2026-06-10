from django.contrib import admin
from django.urls import path
from tracker import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('drinks/', views.drinks_list, name='drinks_list'),
    path('stats/', views.stats, name='stats'),
    path('add/', views.add_record, name='add_record'),

    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]