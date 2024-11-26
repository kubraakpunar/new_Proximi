from django.db import models 
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import AnonymousUser

User = get_user_model() 

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated_by"
    )
    def save(self, *args, **kwargs):
        if isinstance(self.updated_by, User):
            if isinstance(self.updated_by, AnonymousUser):
                self.updated_by = None  # AnonymousUser olduğunda None ata
            else:
                self.updated_by = self.updated_by  # Geçerli User ise UUID ata
        else:
            self.updated_by = None  # Geçersiz User nesnesi ise None ata
        
        super().save(*args, **kwargs)

    class Meta:
        abstract = True