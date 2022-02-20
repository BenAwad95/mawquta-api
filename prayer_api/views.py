from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import SelectCityForm
import requests

from prayer_api import forms

CITES = {
    'ja': 'Jeddah',
    'ma': 'Makkah'
}

def home(request, city='ja):
    print(city)
    city = CITES.get(city)
    country = 'Saudi Arabia'
    method = 4
    result = requests.get(f"http://api.aladhan.com/v1/timingsByCity?\
        method={method}&city={city}&country={country}")
    data = result.json()
    # print(type(data))
    # data = json.dumps(data)
    # print(type(data))
    data = data['data']
    # return HttpResponse(data)
    # return JsonResponse(data)
    return render(
        request, 'prayer/city_timing.html',
        context={
            'city': city,
            'hijri': data['date']['hijri'],
            'gregorian': data['date']['gregorian'],
            'timings': data['timings']}
        )


def select_city(request):
    if request.method == 'POST':
        form = SelectCityForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            selected_city = form.cleaned_data.get('city')
            return redirect(reverse_lazy('home', args={'city': selected_city}))
    form = SelectCityForm()
    return render(request, 'select_city.html', context={'form': form})
