import tramdata as td
from graphs import WeightedGraph, view_shortest

class TramNetwork(WeightedGraph):
    ...

TRAM_FILE = './tramnetwork.json'

def readTramNetwork(tramfile=TRAM_FILE):
    ...

def demo():
    G = readTramNetwork()
    a, b = input('from,to ').split(',')
    view_shortest(G, a, b)

if __name__ == '__main__':
    demo()
