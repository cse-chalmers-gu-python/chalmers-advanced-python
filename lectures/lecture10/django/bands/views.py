from .forms import BandSearchForm
from .models import Band
from django.shortcuts import render

all_bands = [
    { "name": "The Black Crowes", "year": 1984 },
    { "name": "The Black Keys", "year": 2001 },
    { "name": "Black Sabbath", "year": 1968 }
]

def home(request):
    q = request.GET.get('query')

    if q:
        # filter based on search query
        results = [ b for b in all_bands if q in b["name"] ]
    else:
        results = all_bands

    return render(
        request, # client request
        'bands_home.html', # template to render
        { "bands": results } # data passed to template
    )
