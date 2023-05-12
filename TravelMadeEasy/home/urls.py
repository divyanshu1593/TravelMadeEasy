from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('user_login', views.user_login, name='user_login'),
    path('agent_login', views.agent_login, name='agent_login'),
    path('user_signup', views.user_signup, name='user_signup'),
    path('user_signup_handle', views.user_signup_handle, name='user_signup_handle'),
    path('user_home', views.user_home, name='user_home'),
    path('user_login_handle', views.user_login_handle, name='user_login_handle'),
    path('agent_signup', views.agent_signup, name='agent_signup'),
    path('agent_signup_handle', views.agent_signup_handle, name='agent_signup_handle'),
    path('agent_login_handle', views.agent_login_handle, name='agent_login_handle'),
    path('agent_home', views.agent_home, name='agent_home'),
    path('agent_hotel', views.agent_hotel, name='agent_hotel'),
    path('agent_hotel_handle', views.agent_hotel_handle, name='agent_hotel_handle'),
    path('user_hotel', views.user_hotel, name='user_hotel'),
    path('hotel_booking_handle', views.hotel_booking_handle, name='hotel_booking_handle'),
    path('hotel_cancle_handle', views.hotel_cancle_handle, name='hotel_cancle_handle'),
    path('agent_vehicle', views.agent_vehicle, name='agent_vehicle'),
    path('agent_vehicle_handle', views.agent_vehicle_handle, name='agent_vehicle_handle'),
    path('user_vehicle', views.user_vehicle, name='user_vehicle'),
    path('vehicle_booking_handle', views.vehicle_booking_handle, name='vehicle_booking_handle'),
    path('vehicle_cancle_handle', views.vehicle_cancle_handle, name='vehicle_cancle_handle'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('aboutusUser', views.aboutusUser, name='aboutusUser')
]