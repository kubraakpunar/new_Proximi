from rest_framework import viewsets
from .serializers import ( 
    UserSerializer
) 
from user_service.models import ( 
    User
)
from django.conf import settings 
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] 

