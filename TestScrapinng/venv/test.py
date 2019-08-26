def sub_rectangles(factor=4, westlimit=0, southlimit=0, eastlimit=2, northlimit=2):
    table = list()
    # Divide the difference between the limits by the factor
    lat_adj_factor = (northlimit - southlimit) / factor
    lon_adj_factor = (eastlimit - westlimit) / factor
    # Create longitude and latitude lists
    lat_list = []
    lon_list = []
    for i in range(factor + 1):
        lon_list.append(westlimit)
        westlimit += lon_adj_factor
    for i in range(factor + 1):
        lat_list.append(southlimit)
        southlimit += lat_adj_factor
    # Build a list of longitude and latitude pairs
    for i in range(0, len(lon_list) - 1):
        for j in range(0, len(lat_list) - 1):
            table.append([(lon_list[i], lat_list[j]), (lon_list[i + 1], lat_list[j]), (lon_list[i], lat_list[j + 1]),
                          (lon_list[i + 1], lat_list[j + 1])])
            print(table)
    return table
