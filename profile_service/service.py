from .models import Profile,Interest
from core.service import BaseService 

class ProfileService(BaseService):
    model = Profile 

class InterestService(BaseService):
    model = Interest 
    