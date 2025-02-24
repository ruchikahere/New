from django.urls import path
from .views import insert_employee, fetch_employee
from . import views

urlpatterns = [
    path('add/', insert_employee),
    path('employee/', fetch_employee),
    # path('login/', views.user_login, name='login'),
    # path('home/', views.home, name='home'),
    # path('logout/', views.user_logout, name='logout'),
]
