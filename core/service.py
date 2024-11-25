from .middleware import get_current_user

class BaseService:
    model = None

    @classmethod
    def create(cls, data):
        current_user = get_current_user()
        instance = cls.model(**data)
        if current_user and hasattr(cls.model, 'updated_by'):
            instance.updated_by = current_user
        instance.save()
        return instance 
    
    @classmethod
    def update(cls, instance, data):
        current_user = get_current_user()
        for key, value in data.items():
            setattr(instance, key, value)
        if current_user and hasattr(cls.model, 'updated_by'):
            instance.updated_by = current_user
        instance.save()
        return instance 