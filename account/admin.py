from django.contrib import admin
from . models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'last_updated', 'gender']
    raw_id_fields = ['user']
