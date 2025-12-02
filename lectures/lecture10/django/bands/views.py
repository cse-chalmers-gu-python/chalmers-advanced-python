from .forms import BandSearchForm
from .models import Band
from django.shortcuts import render

all_bands = [
    { "name": "The Black Crowes", "year": 1984 },
    { "name": "The Black Keys", "year": 2001 },
    { "name": "Black Sabbath", "year": 1968 }
]

def home(request):
    return render(
        request, # client request
        'bands_home.html', # template to render
        { "bands": all_bands } # data passed to template
    )
