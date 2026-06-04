from django.contrib import admin
from django.urls import path
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('napoje/', views.drinks_list, name='drinks_list'),
    path('statistiky/', views.stats, name='stats'),
    path('pridat/', views.add_record, name='add_record'),
    path('registrace/', views.register, name='register'),
    path('odhlasit/', views.logout_view, name='logout'),
]