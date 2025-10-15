# visualization of shortest path in Lab 3, modified to work with Django

from .trams import readTramNetwork
from .graphs import dijkstra
from .color_tram_svg import color_svg_network
import os
from django.conf import settings
from django.core.files.storage import default_storage

def show_shortest(dep, dest):
    network = readTramNetwork()

    # TODO: replace this mock-up with actual computation using dijkstra.
    # First you need to calculate the shortest and quickest paths,
    # by using appropriate cost functions in dijkstra().
    # Then you just need to use the lists of stops returned by dijkstra()
    # You sould also tell which tram lines you use and where changes happen.

    quickest = [dep, 'Chalmers', dest]
    shortest = [dep, 'Chalmers', dest] 
    
    timepath = 'Quickest: ' + ', '.join(quickest) + ', 5 minutes'
    geopath = 'Shortest: ' + ', '.join(shortest) + ', 100 km'

    def colors(v):
        if v in shortest:
            return 'cyan'
        else:
            return 'white'

    # build dynamic file name from arguments, safely
    dep_safe = default_storage.get_valid_name(dep)
    dest_safe = default_storage.get_valid_name(dest)
    outfile_unique_name = f"shortest_path_{dep_safe}_{dest_safe}.svg"

    # this part should be left as it is:
    # change the SVG image with your shortest path colors
    infile = os.path.join(settings.BASE_DIR, 'tram/templates/tram/images/gbg_tramnet.svg')
    outfile = os.path.join(settings.BASE_DIR, f'tram/templates/tram/images/generated/{outfile_unique_name}')
    color_svg_network(infile, outfile, colormap=colors)
    # return the path texts to be shown in the web page
    return timepath, geopath, outfile

