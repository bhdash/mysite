from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.


def index_view(request):
    return HttpResponse("Home Page")

def contact_view(request):
    return HttpResponse("Contact Page")

def about_view(request):
    return HttpResponse("About Page")