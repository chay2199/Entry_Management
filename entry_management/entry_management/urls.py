from django.contrib import admin
from django.urls import path
from entry_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('check_in/', views.post, name='check_in'),
    path('check_out/', views.success_view, name='check_out'),
    path('loop/', views.user_login, name='loop'),
]
