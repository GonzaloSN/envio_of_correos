import django_tables2 as tables
from .models import RegionalUser


class RegionalUserTable(tables.Table):
    id        = tables.Column(orderable=False, 
                              verbose_name='#',
                              attrs={
                                  'th': {'class': 'text-white'}})
    name      = tables.Column(orderable=False, 
                              attrs={
                                  'th': {'class': 'text-white'}})
    last_name = tables.Column(orderable=False, 
                              attrs={
                                  'th': {'class': 'text-white'}})
    email     = tables.Column(orderable=False, 
                              attrs={
                                  'th': {'class': 'text-white'}})
    username  = tables.Column(orderable=False, 
                              attrs={
                                  'th': {'class': 'text-white'}})
    password  = tables.Column(orderable=False, 
                              attrs={
                                  'th': {'class': 'text-white'}})
    profile   = tables.Column(orderable=False, 
                              attrs={
                                  'th': {'class': 'text-white'}})
    region    = tables.Column(orderable=False, 
                              attrs={
                                  'th': {'class': 'text-white'}})
    options   = tables.Column(verbose_name='Opciones',
                              orderable=False,
                              empty_values=(),
                              attrs={
                                  'td': {'class': 'text-center'},
                                  'th': {'class': 'text-center text-white col-md-2'}})

    class Meta:
        model = RegionalUser
        fields = ('id', 'name', 'last_name', 'email', 'username', 'password', 'profile', 'region')
        attrs = {'class': 'table table-striped table-hover'}
    
   
