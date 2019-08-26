
# def rect_count(n, m):
#     return (m * n * (n + 1) * (m + 1)) // 4
#
#
# # Driver code
# n, m = 2, 2
# print(rect_count(n, m))

# A = L x W

# length = 50
# width = 10
#
# grid = (length * width) / 5
# print(grid)

# NS_length=


# 4

import googlemaps

API_KEY = 'AIzaSyBzeqyVAgdXLUSB8YGVI2dzYcMgnsgOC2I'
gmaps = googlemaps.Client(key=API_KEY)


origin_latitude = 12.9551779
origin_longitude = 77.6910334
destination_latitude = 28.505278
destination_longitude = 77.327774
distance = gmaps.distance_matrix([str(origin_latitude) + " " + str(origin_longitude)],
                                 [str(destination_latitude) + " " + str(destination_longitude)], mode='walking')[
    'rows'][0]['elements'][0]

print(distance)
