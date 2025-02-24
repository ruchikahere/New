from django.urls import path
from .views import register, user_login, home, user_logout
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_profile, profile_view
from .views import document_upload
from .views import message_list
from .import views
from .views import public_api, private_api
from rest_framework.authtoken.views import obtain_auth_token
from .views import ExampleView


urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('upload/', upload_profile, name='upload_profile'),
    path('profile/', profile_view, name = 'profile_view'),
    path('documentupload/', views.document_upload, name='document_upload'),
    path('books/', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
    path('messages/', message_list, name='message-list'),
    path('messages/<int:pk>/delete/', views.message_delete, name='message_delete'),
    path('messages/<int:pk>/update/', views.message_update, name='message_update'),
    path('public/', public_api, name='public_api'),
    path('private/', private_api, name='private_api'),
    path('token/', obtain_auth_token, name='api_token_auth'),
    path('example/', ExampleView.as_view(), name='example_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

