from collections import Counter


def Coords(coord):
    return tuple([tuple([int(c) for c in e.split(',')]) for e in coord.replace('->', '').split()])


def FillLine1(r):
    if r[0][0] == r[1][0]:
        if r[0][1] < r[1][1]:
            return tuple([tuple([r[0][0], i]) for i in range(r[0][1], r[1][1] + 1)])
        else:
            return tuple([tuple([r[0][0], i]) for i in range(r[1][1], r[0][1] + 1)])

    if r[0][1] == r[1][1]:
        if r[0][0] < r[1][0]:
            return tuple([(i, r[0][1]) for i in range(r[0][0], r[1][0] + 1)])
        else:
            return tuple([(i, r[0][1]) for i in range(r[1][0], r[0][0] + 1)])

    return ()

def FillLine2(r):
    if r[0][0] == r[1][0]:
        if r[0][1] < r[1][1]:
            return tuple([tuple([r[0][0], i]) for i in range(r[0][1], r[1][1] + 1)])
        else:
            return tuple([tuple([r[0][0], i]) for i in range(r[1][1], r[0][1] + 1)])

    if r[0][1] == r[1][1]:
        if r[0][0] < r[1][0]:
            return tuple([(i, r[0][1]) for i in range(r[0][0], r[1][0] + 1)])
        else:
            return tuple([(i, r[0][1]) for i in range(r[1][0], r[0][0] + 1)])

    if r[0][0] - r[0][1] == r[1][0] - r[1][1]:
        if r[0][0] < r[1][0]:
            return tuple([(r[0][0] + i, r[0][1] + i) for i in range(r[1][0] - r[0][0] + 1)])
        else:
            return tuple([(r[1][0] + i, r[1][1] + i) for i in range(r[0][0] - r[1][0] + 1)])

    if r[0][0] + r[0][1] == r[1][0] + r[1][1]:
        if r[0][0] < r[1][0]:
            return tuple([(r[0][0] + i, r[0][1] - i) for i in range(r[1][0] - r[0][0] + 1)])
        else:
            return tuple([(r[1][0] + i, r[1][1] - i) for i in range(r[0][0] - r[1][0] + 1)])


    return ()


with open("day5.txt", "r") as f:
    input = f.read().splitlines()
    lines = [Coords(line) for line in input]
    points = sum(tuple([FillLine1(line) for line in lines]), ())
    grid = Counter(points)
    sol = [(k,v) for k, v in grid.items() if v > 1]

    print('Parte 1:', len(sol))



    points = sum(tuple([FillLine2(line) for line in lines]), ())
    grid = Counter(points)
    sol = [(k,v) for k, v in grid.items() if v > 1]

    print('Parte 2:', len(sol))
