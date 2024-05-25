# Importing the 'path' function from django.urls to define URL patterns
# Importing views from the current package ('.') to connect them to URLs

from django.urls import path
from . import views

# Defining URL patterns
urlpatterns = [
    #~ Mapping the URL 'members/' to the 'members' view function in views.py
    #~ The 'name' parameter gives the URL pattern a name for easy reference
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'), 
]
