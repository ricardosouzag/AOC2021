import numpy as np


def varabs(num, base):
    # if base is non-negative, returns the smallest non-negative number X such that abs(X-base) = abs(num-base)
    # if base == 0 this is just abs(num)
    # if base < 0 returns the smallest non-negative number X such that abs(X+base) = abs(num-base)
    return abs(base-abs(base-num))



def connect(points, visited):
    newvis = visited | points
    newpoints =   {(x + 1, y) for x, y in points if x + 1 < n} \
                | {(x - 1, y) for x, y in points if x - 1 > -1} \
                | {(x, y + 1) for x, y in points if y + 1 < m} \
                | {(x, y - 1) for x, y in points if y - 1 > -1}
    newpoints = {(x, y) for x, y in newpoints if inputs[x, y] != 9 and (x, y) not in visited}

    if not any(newpoints):
        return newvis
    else:
        return connect(newpoints, newvis)


with open('day9.txt') as f:
    inputs = np.matrix([[int(e) for e in line] for line in f.read().splitlines()])

    n, m = inputs.shape

    lows = []

    for i in range(n):
        for j in range(m):
            if  inputs[i, j] < inputs[varabs(i - 1, 0), j]\
            and inputs[i, j] < inputs[varabs(i + 1, n - 1), j]\
            and inputs[i, j] < inputs[i, varabs(j - 1, 0)]\
            and inputs[i, j] < inputs[i, varabs(j + 1, m - 1)]:
                lows += [inputs[i, j]]

    ret = [l + 1 for l in lows]
    print('Parte 1:', sum(ret))

    basins = set()
    for i in range(n):
        for j in range(m):
            if inputs[i, j] == 9:
                continue
            if any([basin for basin in basins if (i, j) in basin]):
                continue
            basins.add(frozenset(connect({(i, j)}, set())))

    basinslens = sorted([len(basin) for basin in basins])
    print('Parte 2:', np.prod(basinslens[-3:]))
