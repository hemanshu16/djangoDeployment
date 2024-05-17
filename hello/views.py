from django.shortcuts import render
from random_word import RandomWords
import environ
env = environ.Env()

r = RandomWords()
# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Name :- "+env('myName') + "  "+r.get_random_word())