from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    """Custome User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_MALE, "Female"),
        (GENDER_MALE, "Other"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, blank=True, max_length=10, null=True)  
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)

