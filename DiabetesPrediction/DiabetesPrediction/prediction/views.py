from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm  
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# Home Page
@login_required(login_url='/login/', redirect_field_name=None)
def home(request):
    return render(request, 'home.html')

# User Registration View
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data["password"])  # Hash the password
            user.save()  
            return redirect('home')  # Redirect to login page
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:  # Check if both fields are filled
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")  # Redirect to home page
            else:
                return render(request, "login.html", {"error": "Invalid Username or Password"})
        else:
            return render(request, "login.html", {"error": "Please fill all fields"})

    return render(request, "login.html")

# User Logout View
def user_logout(request):
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to login page

# Prediction Input Page (Only for Logged-in Users)
@login_required
def predict(request):
    return render(request, 'predict.html')

# Result Page (Only for Logged-in Users)
@login_required  
def result(request):
    # Load the diabetes dataset
    diabetes_dataset = pd.read_csv(r'C:\Users\Ruchika Sharma\Downloads\DiabetesPrediction\diabetes.csv')

    # Prepare training data
    X = diabetes_dataset.drop(columns='Outcome', axis=1)
    Y = diabetes_dataset['Outcome']
    
    # Standardize the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split dataset
    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, stratify=Y, random_state=2)

    # Train the SVM model
    classifier = svm.SVC(kernel='linear')
    classifier.fit(X_train, Y_train)

    if request.method == "GET":
        try:
            # Get user input from form
            val1 = float(request.GET["n1"])
            val2 = float(request.GET["n2"])
            val3 = float(request.GET["n3"])
            val4 = float(request.GET["n4"])
            val5 = float(request.GET["n5"])
            val6 = float(request.GET["n6"])
            val7 = float(request.GET["n7"])
            val8 = float(request.GET["n8"])

            # Make a prediction
            input_data = np.array([[val1, val2, val3, val4, val5, val6, val7, val8]])
            input_scaled = scaler.transform(input_data)
            pred = classifier.predict(input_scaled)

            # Interpret result
            result1 = "Positive" if pred == [1] else "Negative"

        except Exception as e:
            result1 = "Error in processing input"

        return render(request, 'predict.html', {"result2": result1})

    return redirect('predict')
