from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, LocationForm
from .models import Location
from django.http import HttpResponseRedirect
import requests


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    # url = 'https://www.trackcorona.live/api/countries/{}'
    # covid_data = []

    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = LocationForm()



    # locations = Location.objects.all()

    # for location in locations:
    #     r = requests.get(url.format(location)).json()
    #     country_info = {
    #     'location': r['data'][0]['location'],
    #     'confirmed': r['data'][0]['confirmed'],
    #     'dead': r['data'][0]['dead'],
    #     'recovered': r['data'][0]['recovered'],
    #     }
    #
    #     covid_data.append(country_info)
    #
    #
    # context = {'covid_data': covid_data, 'form': form}
    context = {'form': form}
    return render(request, 'users/profile.html', context)
