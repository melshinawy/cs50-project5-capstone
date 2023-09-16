from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(AbstractUser):
#     class Role(models.TextChoices):
#         ADMIN = "ADMIN", 'Admin'
#         EMPLOYER = "EMPLOYER", 'Employer'
#         APPLICANT = "APLICANT", 'Aplicant'
    
#     base_role = Role.ADMIN

#     role = models.CharField(max_length=50, choices=Role.choices)