from .forms import BandSearchForm
from .models import Band
from django.shortcuts import render

def home(request):
    form = BandSearchForm(request.GET)
    if form.is_valid() and (q := form.data.get('query')):
        # filter based on search query
        results = Band.objects.filter(name__contains=q)
    else:
        results = Band.objects.all()

    return render(
        request, # client request
        'bands_home.html', # template to render
        { "bands": results, "form": form } # data passed to template
    )
