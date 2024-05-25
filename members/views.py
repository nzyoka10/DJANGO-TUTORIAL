# from django.shortcuts import render
# from django.http import HttpResponse

from django.http import HttpResponse
from django.template import loader

# Create your views here.
def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())




# my first view.....
# def members(request):
#     return HttpResponse("This is the members page")



