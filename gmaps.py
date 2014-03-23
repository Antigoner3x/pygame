#import google maps
from googlemaps import GoogleMaps
from HTMLParser import HTMLParser
#from sys import argv
from directions import *

#Parser submitted by stackoverflow user Eloff
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self,d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)
    
def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

#Googlemaps Object
mapService = GoogleMaps()
#get directions from google
directions = mapService.directions(home, destination)

for step in directions['Directions']['Routes'][0]['Steps']:
    print strip_tags(step['descriptionHtml'])
    