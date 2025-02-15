from django.urls import path
from .views import insert_employee, fetch_employee

urlpatterns = [
    path('add/', insert_employee),
    path('employee/', fetch_employee),
]
