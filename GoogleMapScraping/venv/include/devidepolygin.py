from math import radians, sin, cos, acos
# width
width_from_lat=radians(float(7.998356))
width_from_lon=radians(float(80.012464))
width_to_lat=radians(float(8.041721))
width_to_lon=radians(float(81.218943))

width = 6371.01 * acos(sin(width_from_lat)*sin(width_to_lat) + cos(width_from_lat)*cos(width_to_lat)*cos(width_from_lon - width_to_lon))
print("The distance is %.2fkm." % width)

# length
from_lat=radians(float(7.998356))
from_lon=radians(float(80.012464))
to_lat=radians(float(6.590929))
to_lon=radians(float(80.195861))

length = 6371.01 * acos(sin(from_lat)*sin(to_lat) + cos(from_lat)*cos(to_lat)*cos(from_lon - to_lon))
print("The distance is %.2fkm." % length)

area = (width*length)/4
print(area)