from django.urls import path
from .views import home, RegionalUserCreateView, RegionalUserListView, correo

urlpatterns = [
    path('', home, name='home'),
    path('correo/', correo, name='correo'),
    path('create/', RegionalUserCreateView.as_view(), name='create'),
    path('list/', RegionalUserListView.as_view(), name='list')
]