from django.contrib import admin
from .models import Profile,Interest

@admin.register(Profile) 
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'bio', 'location')
    search_fields = ('user_id__username', 'location')

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )    