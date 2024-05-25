from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# my first view.....
def members(request):
    return HttpResponse("This is the members page")



