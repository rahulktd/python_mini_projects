from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.


class Students(AbstractUser):
    is_student = models.BooleanField(default=False)
    email = models.EmailField()
    username = models.CharField(max_length=30,unique=True)
    standard = models.CharField(max_length=10)
    name = models.CharField(max_length=25, null=True)
    address = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=20, null=True, unique=True)

class Complaint(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    message = models.TextField()

class Reply(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class Notification(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, null=True, blank=True)
