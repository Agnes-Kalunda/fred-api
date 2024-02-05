
from django.urls import path
from .views import *


urlpatterns = [
    path('', default_view, name='default_view'),
    path('get_fred_series/<str:series_id>/', get_fred_series, name='get_fred_series'),
]
