from rest_framework import viewsets 
from .serializers import (
    ProfileSerializer,
    InterestSerializer
)
from services.profile_service.models import(
    Profile,
    Interest
)
from django.conf import settings 
from rest_framework.permissions import IsAuthenticated


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]  # Sadece giriş yapmış kullanıcılar

    def get_queryset(self):
        # Sadece giriş yapan kullanıcının profilini döndür
        return Profile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Profil oluştururken authenticated kullanıcıyı bağla
        serializer.save(user=self.request.user)

class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Event oluştururken kullanıcıyı bağla
        serializer.save(created_by=self.request.user)