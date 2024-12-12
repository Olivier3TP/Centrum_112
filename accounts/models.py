from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('dispatcher', 'Dyspozytor'),
        ('medic', 'Ratownik medyczny')
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='dispatcher')

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'