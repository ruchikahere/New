from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("home", views.home_view, name='home_view'),
    path("submit/", views.submit_view, name="submit_view"),
    path("hello/", views.View.as_view(), name="hello"),
    path('cl', views.MyView.as_view(name= 'rishu'), name='cl'),
    path('students/', views.student_list, name='student_list'),  # Read (fetch data)
    path('add/', views.add_student, name='add_student'),  # Create (add data)
    path('update/', views.update_student, name='update_student'),  # Update (modify data)
    path('delete/', views.delete_student, name='delete_student'),  # Delete (remove data)
    path('register/', views.student_form, name='student_form'),
    path('students/', views.student_list, name='student_list'),
    path('student-form', views.student_form, name='student_form'),
]

