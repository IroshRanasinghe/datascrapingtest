import googlemaps
import json
import pprint
import time
from random import randint
from time import sleep

API_KEY = 'AIzaSyBzeqyVAgdXLUSB8YGVI2dzYcMgnsgOC2I'
gmaps = googlemaps.Client(key=API_KEY)
# places_result = gmaps.places_nearby(location=point_x + "," + point_y, radius=40000, open_now=False, type='restaurant')


places_result = gmaps.places_nearby(location='6.9220039,79.7861639', radius=40000, open_now=False, type='restaurant')
sleep(randint(10, 100))
place_result = gmaps.places_nearby(page_token=places_result['next_page_token'])

# loop through each of the places in the results, and get the place details.
for place in places_result['results']:
    # define the place id, needed to get place details. Formatted as a string.
    my_place_id = place['place_id']

    # define the fields you would liked return. Formatted as a list.
    my_fields = ['name', 'formatted_phone_number', 'website']

    # make a request for the details.
    places_details = gmaps.place(place_id=my_place_id, fields=my_fields)

    # print the results of the details, returned as a dictionary.
    pprint.pprint(places_details['result'])

    # store the results in a list object.
    # stored_results.append(places_details['result'])

with open('apptest.csv', 'w') as of:
    for d in places_details['result']:
        of.write(format(d))