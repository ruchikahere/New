from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.user
class Task(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    task_date = models.DateField()
    task_description = models.TextField()

    def __str__(self):
        return self.task_name
    
class Task1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


# Create your models here.
