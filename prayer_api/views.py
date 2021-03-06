from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import SelectCityForm, CITES
import requests


CITES = dict(CITES)


def home(request, city='ma'):
    city = CITES.get(city)
    country = 'Saudi Arabia'
    method = 4
    result = requests.get(f"http://api.aladhan.com/v1/timingsByCity?\
        method={method}&city={city}&country={country}")
    data = result.json()
    data = data['data']
    return render(
        request, 'prayer/city_timing.html',
        context={
            'city': city,
            'hijri': data['date']['hijri'],
            'gregorian': data['date']['gregorian'],
            'timings': data['timings']}
        )


# The two return all works.
def select_city(request):
    if request.method == 'POST':
        form = SelectCityForm(request.POST)
        if form.is_valid():
            selected_city = form.cleaned_data.get('city')
            return redirect(reverse_lazy('home', args=[selected_city]))
            # return redirect(reverse_lazy('home', kwargs={'city': selected_city})) 

    form = SelectCityForm()
    return render(request, 'select_city.html', context={'form': form})
