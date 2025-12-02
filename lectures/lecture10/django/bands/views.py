from .forms import BandSearchForm
from .models import Band
from django.shortcuts import render

all_bands = [
    { "name": "The Black Crowes", "year": 1984 },
    { "name": "The Black Keys", "year": 2001 },
    { "name": "Black Sabbath", "year": 1968 }
]

def home(request):
    form = BandSearchForm(request.GET)
    if form.is_valid() and (q := form.data.get('query')):
        # filter based on search query
        results = [ b for b in all_bands if q in b["name"] ]
    else:
        results = all_bands

    return render(
        request, # client request
        'bands_home.html', # template to render
        { "bands": results, "form": form } # data passed to template
    )
