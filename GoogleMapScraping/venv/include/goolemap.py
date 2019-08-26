# import shapely.geometry
# import pyproj
#
import googlemaps
import json
import pprint
import time
from random import randint
from time import sleep

#
# # WGS84 bounds:
# # 79.64 5.86
# # 81.95 9.88
# input_coordinate_system = pyproj.Proj(init='epsg:4326')
# output_coordinate_system = pyproj.Proj(init='epsg:5234')
#
# # NW = shapely.geometry.Point((74453.86, 73977.22))
# # SE = shapely.geometry.Point((329008.98, 518632.65))
#
# NW = shapely.geometry.Point((9.711037, 79.481871))
# SE = shapely.geometry.Point((6.276359, 82.015429))
# NW = shapely.geometry.Point((-5.0, 40.0))
# SE = shapely.geometry.Point((-4.0, 41.0))

# step_size = 5000
#
# S = pyproj.transform(input_coordinate_system, output_coordinate_system, NW.x, NW.y)
# E = pyproj.transform(input_coordinate_system, output_coordinate_system, SE.x, SE.y)
#
# gridpoints = []
#
# x = S[0]
# while x < E[0]:
#     y = S[1]
#     while y < E[1]:
#         p = shapely.geometry.Point(pyproj.transform(input_coordinate_system, output_coordinate_system, x, y))
#         gridpoints.append(p)
#         y += step_size
#     x += step_size
#
# with open("map.csv", "w") as f:
#     for point in gridpoints:
#         point_x = point.x
#         point_y = point.y
#
#         coordinate = "{:f} \n {:f}"
#         f.write(coordinate.format(point_x, point_y))
#         f.close()

API_KEY = 'AIzaSyAeL5MR2XfxGi28XaBsSH_53nu-7zcjNDM'
gmaps = googlemaps.Client(key=API_KEY)
# places_result = gmaps.places_nearby(location=point_x + "," + point_y, radius=40000, open_now=False, type='restaurant')


places_result = gmaps.places_nearby(location='6.9220039,79.7861639', radius=40000, open_now=False, type='restaurant')
# sleep(randint(10, 100))

sleep(3)
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
