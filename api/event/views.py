from rest_framework import viewsets
from .serializers import (
    EventSerializer,
    EventLocationSerializer, 
    EventScheduleSerializer,
    EventRatingSerializer
)
from services.event_service.models import(
    Event,
    EventRating,
    EventLocation,
    EventSchedule
)
from django.conf import settings 

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventScheduleViewSet(viewsets.ModelViewSet):
    queryset = EventSchedule.objects.all()
    serializer_class = EventScheduleSerializer

class EventLocationViewSet(viewsets.ModelViewSet):
    queryset = EventLocation.objects.all()
    serializer_class = EventLocationSerializer 

class EventRatingViewSet(viewsets.ModelViewSet):
    queryset = EventRating.objects.all()
    serializer_class = EventRatingSerializer