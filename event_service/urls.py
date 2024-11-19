from django.urls import path,include 
from rest_framework.routers import DefaultRouter 
from api.event.views import EventViewSet, EventLocationViewSet, EventRatingViewSet, EventScheduleViewSet

router = DefaultRouter() 
router.register(r'events', EventViewSet)
router.register(r'event-locations', EventLocationViewSet)
router.register(r'event-schedules', EventScheduleViewSet)
router.register(r'event-ratings', EventRatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]