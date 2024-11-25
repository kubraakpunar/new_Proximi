from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid 
from django.utils.translation import gettext_lazy as _
from services.user_service.models import User 
from core.models import BaseModel
from django.contrib.auth import get_user_model

class Event(BaseModel):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)
    organizer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="organized_events")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class EventSchedule(BaseModel):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='schedule')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField() 

    def __str__(self):
        return f"{self.event.name} - Schedule"
    
class EventLocation(BaseModel):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='location')
    location_name = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True) 

    def __str__(self):
        return f"{self.event.name} - Location"
    
class EventRating(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="event_ratings", null=True)
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name="rating")
    rating = models.DecimalField(max_digits=5, decimal_places=2,default=0.0)
    rating_count = models.PositiveIntegerField(default=0)

    def add_rating(self, user, new_rating):
        # Mevcut kullanıcı ve etkinlik için rating kontrolü yapıyoruz
        existing_rating = EventRating.objects.filter(user=user, event=self.event).first()  # `first()` ile tek bir sonuç alıyoruz
        
        if existing_rating:
            # Eğer kullanıcı zaten oy vermişse, rating'i güncelle
            existing_rating.rating = new_rating
            existing_rating.save()
        else:
            # Eğer kullanıcı daha önce oy vermemişse, yeni rating oluştur
            self.rating_count += 1
            self.rating = (self.rating * (self.rating_count - 1) + new_rating) / self.rating_count  # doğru hesaplama
            self.save()

            # Yeni EventRating kaydını oluştur
            EventRating.objects.create(user=user, event=self.event, rating=new_rating)


        def __str__(self):
            return f"{self.event.name} - Rating"