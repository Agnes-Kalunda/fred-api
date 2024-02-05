
from django.http import JsonResponse , HttpResponse
import requests
from decouple import config


def default_view(request):
    return HttpResponse("Welcome to the FRED API Django App!")

def get_fred_series(request, series_id):
    api_key = config(FRED_API_KEY)
    fred_api_url = f'https://api.stlouisfed.org/fred/series?series_id=GNPCA&api_key=abcdefghijklmnopqrstuvwxyz123456&file_type=json'

    try:
        response = requests.get(fred_api_url)
        data = response.json()
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)})
