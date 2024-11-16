from django.db import models
from django.contrib.auth.models import AbstractUser 
import uuid 
from django.utils.translation import gettext_lazy as _ 

class User(AbstractUser): 
    uuid = models.UUIDField(default=uuid.uuid4,editable=False, unique=True)
    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=128)
