from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # Home page
    path('', views.register, name='register'),  # Register page
    path('login/', views.user_login, name='login'),  # Login page
    path('logout/', views.user_logout, name='logout'),  # Logout functionality
    path('predict/', views.predict, name='predict'),  # Prediction page
    path('result/', views.result, name='result'),  # Result page
]
