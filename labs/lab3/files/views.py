from django.shortcuts import render
from .forms import RouteForm

from .utils.tramviz import show_shortest

def tram_net(request):
    return render(request, 'tram/home.html', {})

def find_route(request):
    form = RouteForm()
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            route = form.data
            timepath, geopath, outfile = show_shortest(route['dep'], route['dest'])
            return render(
                request,
                'tram/show_route.html',
                {
                    'route': form.instance.__str__(),
                    'timepath': timepath,
                    'geopath': geopath,
                    'shortest_path_svg': outfile,
                }
            )
    else:
        form = RouteForm()
    return render(request, 'tram/find_route.html', {'form': form})
