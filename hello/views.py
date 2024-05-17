from django.shortcuts import render
from random_word import RandomWords
r = RandomWords()
# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse(r.get_random_word())