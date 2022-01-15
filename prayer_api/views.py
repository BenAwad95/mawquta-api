from django.shortcuts import render
from django.http import HttpResponse
import requests

def home(request):
    print(request)
    result = requests.get("http://api.aladhan.com/v1/timingsByCity?method=8&city=Makkah&country=Saudi%20Arabia")
    return HttpResponse("Good Work, Keep on it💪🏼")
