from django.db.models import fields
import django_filters
from .models import RegionalUser


class RegionalUserFilter(django_filters.FilterSet):
    class Meta:
        model = RegionalUser
        fields = {
            'name': ['icontains'],
            'last_name': ['icontains'],
            'email': ['exact'],
            'username': ['exact'],
            'profile': ['exact'],
            'region': ['exact'],
        }