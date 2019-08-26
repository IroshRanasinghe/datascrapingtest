import math
import numpy
from shapely import geometry


def getArray(grid):
    n = numpy.zeros((grid[-1][0] + 1, grid[-1][1] + 1))
    for (y, x) in grid:
        n[y, x] = 1
    return n


# Determines if the new point is within the bounds
def getBoundingSquare(newCoord, npArr):
    try:
        if npArr[int(math.floor(newCoord[0])), int(math.floor(newCoord[1]))] == 1 and \
                npArr[int(math.floor(newCoord[0])), int(math.ceil(newCoord[1]))] == 1 and \
                npArr[int(math.ceil(newCoord[0])), int(math.floor(newCoord[1]))] == 1 and \
                npArr[int(math.ceil(newCoord[0])), int(math.ceil(newCoord[1]))] == 1:
            return 1
        else:
            return 0
    except IndexError:
        return 0


# Creates the new points using the desired side length
def interpolator(grid, side_length):
    startCorner = grid[0]
    endCorner = grid[-1]
    npArr = getArray(grid)
    newGrid = []
    if side_length < 1:
        exprY = int((endCorner[0] + 1) * 1 // side_length - 1)
        exprX = int((endCorner[1] + 1) * 1 // side_length - 1)
    else:
        exprY = int((endCorner[0] + 1))
        exprX = int((endCorner[1] + 1))
    for y in range(startCorner[0], exprY):
        for x in range(startCorner[1], exprX):
            newCoord = (y * side_length + startCorner[0], x * side_length + startCorner[1])
            newCoord2 = (float(y + startCorner[0]), float(x + startCorner[1]))
            if getBoundingSquare(newCoord, npArr):
                newGrid.append(newCoord)
            if getBoundingSquare(newCoord2, npArr) and newCoord2 not in newGrid:
                newGrid.append(newCoord2)
    newGrid.sort()
    return newGrid


def subdivide(grid, side_length):
    grid = interpolator(grid, float(side_length))
    subSquares = []
    while len(grid) >= 4:
        sy, sx = grid[0]
        if (sy + side_length, sx + side_length) in grid:
            square = []
            for y in range(2):
                for x in range(2):
                    if (sy + y * side_length, sx + x * side_length) in grid:
                        square.append((sy + y * side_length, sx + x * side_length))
                        if not (y == 1 or x == 1):
                            grid.remove((sy + y * side_length, sx + x * side_length))

            if square not in subSquares and (len(square) == (side_length + 1) ** 2 or len(square) == 4):
                subSquares.append(square)
            (startY, startX) = square[0]
            (endY, endX) = square[-1]
            counter = 0
            while counter < len(grid):
                item = grid[counter]
                if (item[0] < endY and item[1] < endX):
                    grid.remove(item)
                else:
                    counter += 1
        else:
            grid.pop(0)
    allowed = 0
    for item in grid:
        for square in subSquares:
            if item in square:
                allowed += 1
                continue
    if len(grid) > allowed:
        print('Could not divide entire polygon')
    for square in subSquares:
        print(square)
    return subSquares


if __name__ == '__main__':
    grid=[(0,1),(2,1),(2,3),(3,4)]
    subdivide(grid, 0.5)
