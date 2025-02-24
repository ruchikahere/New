from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, DocumentForm
from .models import Profile, Document
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from .models import Message
from .serializers import MessageSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import PyPDF2

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('login')
    
    return render(request,'register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request,'login.html')

@login_required

def home(request):
    return render(request,'home.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def upload_profile(request):
    if request.method =='POST':
        form =ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # Save the uploaded file to the database
            return render(request, 'upload.html', {'form': form})  # Redirect after saving the data
    else:
        form = ProfileForm()

    return render(request, 'upload.html', {'form': form})

def profile_view(request):
     profile = Profile.objects.get(user="saurabh")
     print(profile.picture) # Current logged-in user ka object
     return render(request, 'profile.html', {'users' :profile})

# def understood_conceot(request):
#     print("i understood the concept")
#     friends=[
#         'ankit',
#         'Ruchika'
#     ]
#     return JsonResponse(friends,safe =False)
# views.py


def document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()  # Save the document to the database
            # Open the uploaded PDF and read it using PyPDF2
            if document.file.name.endswith('.pdf'):
                with open(document.file.path, 'rb') as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    text = ''
                    for page in pdf_reader.pages:
                        text += page.extract_text()  # Extract text from each page
                    # Return the text as a response or process it further
                    return HttpResponse(text, content_type='text/plain')
            else:
                return HttpResponse("Uploaded file is not a PDF.", content_type='text/plain')
    else:
        form = DocumentForm()

    return render(request, 'document_upload.html', {'form': form})

@api_view(['POST'])
def home(request):
    return Response({'status': 200, 'message': 'Hello from django rest framework'})

@api_view(['GET', "POST"])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        book.delete()
        return Response({'message':"deleted"},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST'])
def message_list(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    
    if request.method =='POST':
        serializer = MessageSerializer(data=request.data)
        if serializer .is_valid():
            serializer .save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def message_delete(request, pk):
    try:
        message = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return Response({"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND)

    reason = request.data.get('reason', 'No reason provided')
    deleted_message_data = MessageSerializer(message).data

    message.delete()

    return Response({
        "message": "Message deleted successfully",
        "deleted_data": deleted_message_data,
        "reason": reason
    }, status=status.HTTP_200_OK)

@api_view(['PUT'])
def message_update(request, pk):
    try:
        message = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return Response({"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = MessageSerializer(message, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Message updated successfully",
            "updated_data": serializer.data
        }, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def public_api(request):
    return Response({"message": "Anyone can see this API!"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private_api(request):
    return Response({"message": f"Hello {request.user}, You are authenticated!"})




            



    







