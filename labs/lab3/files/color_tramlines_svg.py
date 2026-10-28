import sys
import xml.etree.ElementTree as et

def color_stops(
        infile: str,
        outfile: str,
        colormap: dict[str,str] = {}
    ):
    """
    Set the colour of stop circles in tramlives SVG file

    - infile: path to input SVG file
    - outfile: path where resulting SVG file should be written
    - colormap: dict of stop names to colours, e.g. {"Lana": "#ff0000", "Korsvägen": "gold"}

    Every element with data-stop="<name>" and a fill attribute gets the new fill.
    """

    et.register_namespace('', 'http://www.w3.org/2000/svg')
    tree = et.parse(infile)
    found = set()
    for el in tree.iter():
        name = el.get('data-stop')
        if name in colormap and el.get('fill') is not None:
            el.set('fill', colormap[name]); found.add(name)
    for name in sorted(set(colormap) - found):
        print('no such stop on the map:', name, file=sys.stderr)
    tree.write(outfile, encoding='utf-8', xml_declaration=True)
