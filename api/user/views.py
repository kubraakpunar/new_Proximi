from rest_framework import viewsets
from .serializers import ( 
    UserSerializer
) 
from user_service.models import ( 
    User
)
from django.conf import settings 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer