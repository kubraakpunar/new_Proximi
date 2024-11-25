from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _

class Interest(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name = _('Interest')
        verbose_name_plural = ('Interests')

        def __str__(self):
            return f"{self.name}"
        
class Profile(BaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, to_field='uuid', primary_key=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100)
    interest = models.ManyToManyField(Interest, related_name='profiles', blank=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

        def __str__(self):
            return f"{self.user_id}'s Profile"