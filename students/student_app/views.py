from django.shortcuts import render, HttpResponse
from .connections import conn, cursor

def insert_employee(request):
    sql = "INSERT INTO employees (name, department, salary) VALUES(%s, %s, %s)"
    values = ("John Doe", "Computer Science", 8000)
    cursor.execute(sql, values)
    conn.commit()

    return HttpResponse("students are inserted successfullyyyy")
def fetch_employee(request):
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()

    result = "<h1>Employee List</h1><ul>"
    for row in data:
        result += f"<li>ID: {row[0]}, Name: {row[1]}, Department: {row[2]}, Salary: {row[3]}</li>"
    
    result += "</ul>"
    return HttpResponse(result)

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate , login , logout
# from django.contrib.auth.decorators import login_required

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
# # Authentication (checking username & password)
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')  # Redirect to home page if login is successful
#         else:
#             return render(request, 'login.html', {'error': 'Invalid Username or Password'})

#     return render(request, 'login.html')


# @login_required
# def home(request):
#     return render(request, 'home.html')


# def user_logout(request):
#     logout(request)
#     return redirect('login')