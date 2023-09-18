from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Company(models.Model):
    account = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class Jobseeker(models.Model):
    account = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)

class Job(models.model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    applicant = models.ManyToManyField(Jobseeker, blank=True, null=True, on_delete=models.SET_NULL)