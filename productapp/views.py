from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def productapp(request):
    return HttpResponse('this is shop page')

