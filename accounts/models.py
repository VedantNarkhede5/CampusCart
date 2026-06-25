from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    college_name = models.CharField(
        max_length=200,
        blank=True
    )

    department = models.CharField(
        max_length=100,
        blank=True
    )

    year = models.CharField(
        max_length=50,
        blank=True
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    upi_id = models.CharField(
        max_length=100,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    profile_photo = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username
    
