from django.db import models
from django.contrib.auth.models import User

from core.models import BaseModel

# Create your models here.
ROLE_CHOICES = (
    ('customer', 'Customer'),
    ('staff', 'Staff'),
)

class ProfileSetting(BaseModel):
    actor = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=120, choices=ROLE_CHOICES, default='user')

class Profile(BaseModel):
    actor = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=125)
    phone = models.CharField(max_length=15)
    