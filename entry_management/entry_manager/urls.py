from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('check_in/', views.checkin, name='check_in'),
    path('check_out/', views.success_view, name='check_out'),
    path('loop/', views.checkout, name='loop'),
]