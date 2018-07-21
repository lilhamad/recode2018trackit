from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Welcome to Unilever Site")

# Create your views here.
