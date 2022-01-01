from functools import reduce
from itertools import product

from numpy import zeros


def neighbors(coord):
    row, col = coord
    ret = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            ret += [(row + i, col + j)]
    return ret


def getOutput(coord, mat):
    x, y = mat.shape
    wincoords = neighbors(coord)
    window = []
    for wincoord in wincoords:
        row, col = wincoord
        if row < 0 or row >= x or col < 0 or col >= y:
            window += [0]
        else:
            window += [mat[row, col]]
    instruction = int(reduce(lambda x, y: x + str(y), window, ''), 2)
    return 1 if algorithm[instruction] == '#' else 0


def enhance(mat):
    x, y = mat.shape
    output = zeros((x + 2, y + 2), dtype=int)
    outcoords = product(range(x + 2), range(y + 2))
    for i, j in outcoords:
        output[i, j] = getOutput((i - 1, j - 1), mat)
    return output


with open('day20.txt') as f:
    raw = f.read().splitlines()
    algorithm = raw[0]
    image = raw[2:]

    imagemat = zeros((len(image), len(image[0])), dtype=int)
    rows, cols = imagemat.shape
    coords = product(range(rows), range(cols))
    for i, j in coords:
        imagemat[i, j] = 1 if image[i][j] == '#' else 0

    print(len(enhance(enhance(imagemat)).nonzero()))
