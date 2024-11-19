from rest_framework import serializers 
from profile_service.models import Profile, Interest

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'location']

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest 
        fields = ['name']