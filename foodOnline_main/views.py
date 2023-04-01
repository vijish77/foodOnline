
from django.shortcuts import HttpResponse

def home(object):
    return HttpResponse('Hello World')