from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Task, Task1

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# When a User is saved, save the Profile as well
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(pre_save, sender=Task1)
def check_task_description(sender, instance, **kwargs):
    if not instance.description:
        instance.description = "No description provided"

@receiver(pre_delete, sender=User)
def warn_before_deleting_user(sender, instance, **kwargs):
    print(f" Warning: User {instance.username} is about to be deleted!")

@receiver(post_delete, sender=User)
def delete_user_tasks(sender, instance, **kwargs):
    print(f" Deleting all tasks for user {instance.username}...")
    Task.objects.filter(user=instance).delete()

