from .models import Event,EventLocation,EventRating,EventSchedule 
from .service import BaseService 

class EventService(BaseService):
    model = Event 

class EventLocationService(BaseService):
    model = EventLocation 

class EventRatingService(BaseService):
    model = EventRating 

class EventScheduleService(BaseService):
    model = EventSchedule