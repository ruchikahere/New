from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.CharField(max_length=100)
    picture = models.ImageField(upload_to ='profile_pics/')

    def __str__(self):
        return self.user
    
class Document(models.Model):
    title = models.CharField(max_length= 255)
    file = models.FileField(upload_to ='documents/' )

    def __str__(self):
        return self.title

class Book(models.Model):
    titlee = models.CharField(max_length = 100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title 

class Message(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
    


    

