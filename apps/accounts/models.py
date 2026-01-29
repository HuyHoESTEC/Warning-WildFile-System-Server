from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('monitor', 'Monitor Staff'),
        ('field_officer', 'Field Officer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='field_officer')
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"