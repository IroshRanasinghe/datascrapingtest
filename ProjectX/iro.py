from shapely import geometry
p1 = geometry.Point((8.801024, 79.479210))
p2 = geometry.Point((8.955824, 81.942374))
p3 = geometry.Point((6.319765, 79.246741))
p4 = geometry.Point((6.293201, 82.100873))

pointList = [p1, p2, p3, p4]
poly = geometry.Polygon([[p.x, p.y] for p in pointList])

print(poly.wkt)