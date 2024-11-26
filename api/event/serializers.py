from rest_framework import serializers
from services.event_service.models import ( 
    Event,
    EventLocation,
    EventRating,
    EventSchedule
)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'description', 'organizer','rating','rating_count', 'created_at', 'updated_at']


class EventScheduleSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(source='event.name', read_only=True)
    
    class Meta:
        model = EventSchedule 
        fields = ['event_name', 'start_date', 'end_date']

class EventLocationSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(source='event.name', read_only=True)
    
    class Meta:
        model = EventLocation 
        fields = ['event_name', 'location_name', 'latitude', 'longitude']

class EventRatingSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(source='event.name', read_only=True)
    
    class Meta:
        model = EventRating
        fields = ['event_name', 'rating']