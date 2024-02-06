
from django.http import JsonResponse , HttpResponse
import requests
from decouple import config
from django.shortcuts import render


def default_view(request):
    return HttpResponse("Welcome to the FRED API Django App!")

def get_fred_series(request, series_id='UNRATE'):
    api_key = config('FRED_API_KEY')

    #endpoint for series observation
    fred_api_url = f'https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json'

    response = requests.get(fred_api_url)
    data = response.json()

    context = {
        'data' : data,
        'series_id' : series_id,
    }

    return render (request, 'home.html', context)
