from django.urls import path,include
from rest_framework.routers import DefaultRouter 
from api.profile.views import ProfileViewSet, InterestViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'interests', InterestViewSet)

urlpatterns = [ 
    path('', include(router.urls))
]