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
        fields = ['name', 'description', 'organizer', 'created_at', 'updated_at']


class EventScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSchedule 
        fields = ['event', 'start_date', 'end_date']

class EventLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLocation 
        fields = ['event', 'location_name', 'latitude', 'longitude']

class EventRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRating
        fields = ['event', 'rating', 'rating_count']