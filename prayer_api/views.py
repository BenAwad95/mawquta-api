from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json

def home(request):
    city = 'Jeddah'
    country = 'Saudi Arabia'
    method = 4
    result = requests.get(f"http://api.aladhan.com/v1/timingsByCity?method={method}&city={city}&country={country}")
    data = result.json()
    print(type(data))
    # data = json.dumps(data)
    # print(type(data))
    data = data['data']
    # return HttpResponse(data)
    # return JsonResponse(data)
    return render(request, 'prayer/city_timing.html', context={'city': city, 'hijri': data['date']['hijri'], 'gregorian': data['date']['gregorian'], 'timings': data['timings']})
