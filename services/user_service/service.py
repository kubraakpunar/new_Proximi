from .models import User 
from core.service import BaseService 

class UserService(BaseService):
    model = User