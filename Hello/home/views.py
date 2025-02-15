from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    return HttpResponse("this is contact page")

from django.http import HttpResponse

def home_view(request):
    if request.method == "GET":
        return HttpResponse("This is a GET request.")
    elif request.method == "POST":
        return HttpResponse("This is a POST request.")
    else:
        return HttpResponse("Unsupported request method.", status=400)
    
def submit_view(request):
    if request.method == "POST":
        name = request.POST.get("name")  # Get data from form
        return HttpResponse(f"Hello, {name}! Your form has been submitted.")
    else:
        return HttpResponse("This view only handles POST requests.")
    
from django.http import HttpResponse
from django.views import View

class MyView(View):
    name = "Ruchika"
    def get(self, request):
        return HttpResponse(self.name)
    
from django.shortcuts import render
from home.models import Student

#Read Operation (Database se Data Fetch karna)
def student_list(request):
    students = Student.objects.all()
    return render(request, 'list.html', {'students': students})

#  Create Operation (Database me Data Add karna)
def add_student(request):
    try:
        new_student = Student(name="saurabh Sharma", age=22, email="saurabh@example.com")
        new_student.save()  # Data database me store ho gaya
        return render(request, 'list.html')
    except Exception as e:
        return HttpResponse(e)

#  Update Operation (Student ka age update karna)
@csrf_exempt
def update_student(request):
    try:
        if request.method == "POST":
            print("................................................")
            student = Student.objects.get(name="saurabh Sharma")  # Student fetch karo
            student.age = 23  # Age update karo
            student.save()  # Changes save karo
        # student = Student.objects.all()
        student = Student.objects.filter(name="saurabh Sharma").first()
        student = [student]
        print(student)
        return render(request, 'list.html', {'students': student})
    except Exception as e:
        return HttpResponse(e)

#  Delete Operation (Student record delete karna)
def delete_student(request):
    try:
        student = Student.objects.get(name="Ruchika Sharma")
        student.delete()  # Student record delete ho gaya
        return render(request, 'list.html')
    except Exception as e:
        print(e)
        return HttpResponse(e)
    
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            print("Form Data:", form.cleaned_data)
            form.save()
            return render(request, 'success.html')  
            return redirect('student_list') 
    else:
        form = StudentForm()

    return render(request, "student_form.html", {"form": form})

def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})


    
