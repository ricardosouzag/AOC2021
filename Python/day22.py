from itertools import product
import numpy as np


def getAllNodes(cube):
    xs = range(cube[0][0], cube[0][1] + 1)
    ys = range(cube[1][0], cube[1][1] + 1)
    zs = range(cube[2][0], cube[2][1] + 1)
    return set(product(xs, ys, zs))


def volume(cube):
    return (cube[0][1] - cube[0][0]) * (cube[1][1] - cube[1][0]) * (cube[2][1] - cube[2][0])


def sublist(lst1, lst2):
    ls1 = [element for element in lst1 if element in lst2]
    ls2 = [element for element in lst2 if element in lst1]
    return ls1 == ls2


def checkNodeInCube(node, cube):
    nx, ny, nz = node
    cx, cy, cz = cube
    return cx[0] <= nx <= cx[1] and cy[0] <= ny <= cy[1] and cz[0] <= nz <= cz[1]


def joinCubes(cube1, cube2):
    x1, X1 = cube1[0]
    y1, Y1 = cube1[1]
    z1, Z1 = cube1[2]
    x2, X2 = cube2[0]
    y2, Y2 = cube2[1]
    z2, Z2 = cube2[2]
    xs, Xs = sorted([x1, x2]), sorted([X1, X2])
    ys, Ys = sorted([y1, y2]), sorted([Y1, Y2])
    zs, Zs = sorted([z1, z2]), sorted([Z1, Z2])
    if xs[1] < Xs[0] and ys[1] < Ys[0] and zs[1] < Zs[0]:
        if ((xs[0], Xs[1]), (ys[0], Ys[1]), (zs[0], Zs[1])) in [cube1, cube2]:
            return [((xs[0], Xs[1]), (ys[0], Ys[1]), (zs[0], Zs[1]))]
        minicubes = []
        allxs = xs + Xs
        allys = ys + Ys
        allzs = zs + Zs
        for i in range(3):
            x = allxs[i]
            xp = allxs[i + 1]
            for j in range(3):
                y = allys[j]
                yp = allys[j + 1]
                for k in range(3):
                    z = allzs[k]
                    zp = allzs[k + 1]
                    if (checkNodeInCube((x, y, z), cube1) and checkNodeInCube((xp, yp, zp), cube1)) or (
                            checkNodeInCube((x, y, z), cube2) and checkNodeInCube((xp, yp, zp), cube2)):
                        minicubes += [((x, xp), (y, yp), (z, zp))]
                    else:
                        continue
        return minicubes
    return [cube1, cube2]


def diffCubes(cube1, cube2):
    x1, X1 = cube1[0]
    y1, Y1 = cube1[1]
    z1, Z1 = cube1[2]
    x2, X2 = cube2[0]
    y2, Y2 = cube2[1]
    z2, Z2 = cube2[2]
    xs, Xs = sorted([x1, x2]), sorted([X1, X2])
    ys, Ys = sorted([y1, y2]), sorted([Y1, Y2])
    zs, Zs = sorted([z1, z2]), sorted([Z1, Z2])
    if xs[1] < Xs[0] and ys[1] < Ys[0] and zs[1] < Zs[0]:
        minicubes = joinCubes(cube1, cube2)
        minicubes.remove(((xs[1], Xs[0]), (ys[1], Ys[0]), (zs[1], Zs[0])))
        return minicubes
    return [cube1]


with open('day22.txt') as f:
    raw = f.read().splitlines()
    lines = [line.split() for line in raw]
    lines = {line[1]: line[0] for line in lines}

    cubes = []
    instructions = {}
    for key in lines:
        cube = key.split(',')
        cube = tuple([tuple(map(int, cub[2:].split('..'))) for cub in cube])
        cubes += [cube]
        instructions[cube] = 1 if lines[key] == 'on' else 0

    initcubes = [cube for cube in cubes if
                 cube[0][0] >= -50 and
                 cube[0][1] <= 50 and
                 cube[1][0] >= -50 and
                 cube[1][1] <= 50 and
                 cube[2][0] >= -50 and
                 cube[2][1] <= 50
                 ]

    allnodesinit = product(range(-50, 51), repeat=3)

    onnodes = 0
    reverseInitCubes = list(reversed(initcubes))
    for node in allnodesinit:
        for cube in reverseInitCubes:
            if checkNodeInCube(node, cube):
                if instructions[cube] == 1:
                    onnodes += 1
                break
    print('Parte 1:', onnodes)

    oncubes = [cube for cube in cubes if instructions[cube] == 1]
    minx, maxx = min(cube[0][0] for cube in oncubes), max(cube[0][1] for cube in cubes)
    miny, maxy = min(cube[1][0] for cube in oncubes), max(cube[1][1] for cube in cubes)
    minz, maxz = min(cube[2][0] for cube in oncubes), max(cube[2][1] for cube in cubes)

    xs = range(minx, maxx + 1)
    ys = range(miny, maxy + 1)
    zs = range(minz, maxz + 1)

    onnodesgen = product(xs, ys, zs)
    onnodesfinal = 0
    itcubes = reversed(cubes)
    for node in onnodesgen:
        for cube in itcubes:
            if checkNodeInCube(node, cube):
                if instructions[cube] == 1:
                    onnodesfinal += 1
                break
    print('Parte 2:', onnodesfinal)
