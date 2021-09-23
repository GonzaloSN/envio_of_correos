from django.contrib import admin

# Register your models here.
from .models import Region, Profile, RegionalUser

admin.site.register(Region)
admin.site.register(Profile)
admin.site.register(RegionalUser)