from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    courses = models.ManyToManyField(Course, related_name='students')

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

class attendenceFile(models.Model):
    filiere = models.CharField(max_length=50)
    groupe = models.CharField(max_length=50)
    fileName = models.CharField(max_length=100)

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='recette_users' 
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='recette_users_permissions'
    )


    