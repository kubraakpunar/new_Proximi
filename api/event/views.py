from rest_framework import viewsets
from .serializers import (
    EventSerializer,
    EventLocationSerializer, 
    EventScheduleSerializer,
    EventRatingSerializer
)
from event_service.models import(
    Event,
    EventRating,
    EventLocation,
    EventSchedule
)
from django.conf import settings 
from rest_framework.permissions import IsAuthenticated 

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated] 

class EventScheduleViewSet(viewsets.ModelViewSet):
    queryset = EventSchedule.objects.all()
    serializer_class = EventScheduleSerializer
    permission_classes = [IsAuthenticated]

class EventLocationViewSet(viewsets.ModelViewSet):
    queryset = EventLocation.objects.all()
    serializer_class = EventLocationSerializer 
    permission_classes = [IsAuthenticated]

class EventRatingViewSet(viewsets.ModelViewSet):
    queryset = EventRating.objects.all()
    serializer_class = EventRatingSerializer
    permission_classes = [IsAuthenticated]