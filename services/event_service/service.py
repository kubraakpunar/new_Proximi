from django.forms import ValidationError
from .models import Event,EventLocation,EventRating,EventSchedule 
from .service import BaseService 
from django.db.models import Avg

class EventService(BaseService):
    model = Event 

class EventLocationService(BaseService):
    model = EventLocation 

class EventRatingService(BaseService):
    model = EventRating 

    def create_event_rating(self, event, user, rating): 
        if rating < 1 or rating > 5:
            raise ValidationError("Rating must be between 1 and 5.") 
        
        event_rating = self.model.objects.create(
            event=event,
            user=user,
            rating=rating,
        )
        related_ratings = event.ratings.filter(event__name=event.name)

        event.rating_count = related_ratings.count()
        average_rating = event.ratings.aggregate(average=Avg('rating'))['average']
        event.rating = round(average_rating, 1) if average_rating else 0.0
        event.save()
        return event_rating

class EventScheduleService(BaseService):
    model = EventSchedule