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

