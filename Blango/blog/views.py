from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_post(request):
    return HttpResponse("Return all blog post")