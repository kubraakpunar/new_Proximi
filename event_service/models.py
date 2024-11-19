from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid 
from django.utils.translation import gettext_lazy as _
from user_service.models import User 

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)
    organizer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="organized_events")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class EventSchedule(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='schedule')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField() 

    def __str__(self):
        return f"{self.event.name} - Schedule"
    
class EventLocation(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='location')
    location_name = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True) 

    def __str__(self):
        return f"{self.event.name} - Location"
    
class EventRating(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name="rating")
    rating = models.DecimalField(max_digits=5, decimal_places=2,default=0.0)
    rating_count = models.PositiveIntegerField(default=0)

    def add_rating(self, new_rating):
        total_score = self.rating * self.rating_count
        self.rating_count += 1 
        self.rating = (total_score + new_rating) / self.rating_count
        self.save() 

    def __str__(self):
        return f"{self.event.name} - Rating"