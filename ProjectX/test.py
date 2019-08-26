import shapely.geometry
import pyproj

# Set up projections
p_ll = pyproj.Proj(init='epsg:4326')
p_mt = pyproj.Proj(init='epsg:3857') # metric; same as EPSG:900913

# Create corners of rectangle to be transformed to a grid
# nw = shapely.geometry.Point((-5.0, 40.0))
# se = shapely.geometry.Point((-4.0, 41.0))
a_point = shapely.geometry.Point((8.801024, 79.479210))
b_point = shapely.geometry.Point((8.955824, 81.942374))
c_point = shapely.geometry.Point((6.319765, 79.246741))
d_point = shapely.geometry.Point((6.293201, 82.100873))

stepsize = 5000 # 5 km grid step size

# Project corners to target projection
a = pyproj.transform(p_ll, p_mt, a_point.x, a_point.y) # Transform NW point to 3857
b = pyproj.transform(p_ll, p_mt, b_point.x, b_point.y) # .. same for SE
c = pyproj.transform(p_ll, p_mt, c_point.x, c_point.y) # .. same for SE
d = pyproj.transform(p_ll, p_mt, d_point.x, d_point.y) # .. same for SE

# Iterate over 2D area
gridpoints = []
x = a[0]
while x < b[0]:
    y = a[1]
    while y < b[1]:
        p = shapely.geometry.Point(pyproj.transform(p_mt, p_ll, x, y))
        gridpoints.append(p)
        y += stepsize
    x += stepsize

with open('testout.csv', 'w') as of:
    of.write('lon;lat\n')
    for p in gridpoints:
        of.write('{:f};{:f}'.format(p.x, p.y))