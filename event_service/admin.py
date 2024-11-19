from django.contrib import admin
from .models import Event,EventLocation,EventRating,EventSchedule 

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'organizer', 'created_at', 'updated_at')
    search_fields = ('name', 'organizer') 


@admin.register(EventSchedule)
class EventScheduleAdmin(admin.ModelAdmin):
    list_display = ('event', 'start_date', 'end_date')
    search_fields = ('event',)

@admin.register(EventLocation)
class EventLocationAdmin(admin.ModelAdmin):
    list_display = ('event', 'location_name', 'latitude', 'longitude')
    search_fields = ('event', 'location_name') 

@admin.register(EventRating)
class EventRatingAdmin(admin.ModelAdmin):
    list_display = ('event','rating')
    search_fields = ('event', 'rating')