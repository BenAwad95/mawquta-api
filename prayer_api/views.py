from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

def home(request):
    result = requests.get("http://api.aladhan.com/v1/timingsByCity?method=8&city=Makkah&country=Saudi%20Arabia")
    data = result.json()
    # return HttpResponse(data)
    return JsonResponse(data)
