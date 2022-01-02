from collections import Counter
from itertools import combinations
from numpy import array

rotations = [
    ((0, 1, 0), (0, 0, 1)),
    ((1, 0, 0), (0, 0, 1)),
    ((0, -1, 0), (0, 0, 1)),
    ((-1, 0, 0), (0, 0, 1)),
    ((0, 1, 0), (0, 0, -1)),
    ((1, 0, 0), (0, 0, -1)),
    ((0, -1, 0), (0, 0, -1)),
    ((-1, 0, 0), (0, 0, -1)),

    ((0, 1, 0), (1, 0, 0)),
    ((0, 0, 1), (1, 0, 0)),
    ((0, -1, 0), (1, 0, 0)),
    ((0, 0, -1), (1, 0, 0)),
    ((0, 1, 0), (-1, 0, 0)),
    ((0, 0, 1), (-1, 0, 0)),
    ((0, -1, 0), (-1, 0, 0)),
    ((0, 0, -1), (-1, 0, 0)),

    ((1, 0, 0), (0, 1, 0)),
    ((0, 0, 1), (0, 1, 0)),
    ((-1, 0, 0), (0, 1, 0)),
    ((0, 0, -1), (0, 1, 0)),
    ((1, 0, 0), (0, -1, 0)),
    ((0, 0, 1), (0, -1, 0)),
    ((-1, 0, 0), (0, -1, 0)),
    ((0, 0, -1), (0, -1, 0)),
]


def rotate(vec):
    x, y, z = vec
    return {
        ((0, 1, 0), (0, 0, 1)): (x, y, z),
        ((1, 0, 0), (0, 0, 1)): (-y, x, z),
        ((0, -1, 0), (0, 0, 1)): (-x, -y, z),
        ((-1, 0, 0), (0, 0, 1)): (y, -x, z),
        ((0, 1, 0), (0, 0, -1)): (-x, y, -z),
        ((1, 0, 0), (0, 0, -1)): (y, x, -z),
        ((0, -1, 0), (0, 0, -1)): (x, -y, -z),
        ((-1, 0, 0), (0, 0, -1)): (-y, -x, -z),

        ((0, 1, 0), (1, 0, 0)): (-z, y, x),
        ((0, 0, 1), (1, 0, 0)): (y, z, x),
        ((0, -1, 0), (1, 0, 0)): (z, -y, x),
        ((0, 0, -1), (1, 0, 0)): (-y, -z, x),
        ((0, 1, 0), (-1, 0, 0)): (z, y, -x),
        ((0, 0, 1), (-1, 0, 0)): (-y, z, -x),
        ((0, -1, 0), (-1, 0, 0)): (-z, -y, -x),
        ((0, 0, -1), (-1, 0, 0)): (y, -z, -x),

        ((1, 0, 0), (0, 1, 0)): (z, x, y),
        ((0, 0, 1), (0, 1, 0)): (-x, z, y),
        ((-1, 0, 0), (0, 1, 0)): (-z, -x, y),
        ((0, 0, -1), (0, 1, 0)): (x, -z, y),
        ((1, 0, 0), (0, -1, 0)): (-z, x, -y),
        ((0, 0, 1), (0, -1, 0)): (x, z, -y),
        ((-1, 0, 0), (0, -1, 0)): (z, -x, -y),
        ((0, 0, -1), (0, -1, 0)): (-x, -z, -y),
    }


def checkOverlap(scan1, scan2):
    if scan1 == scan2:
        return True, scan1
    rotscan2 = [[rotate(b2)[dir] for b2 in scan2] for dir in rotations]
    for b1 in scan1:
        vec1 = array(b1)
        for rscan2 in rotscan2:
            for rb2 in rscan2:
                vec2 = array(rb2)
                vecdiff = vec2 - vec1
                translatedrscan2 = {tuple(array(rbeac2) - vecdiff) for rbeac2 in rscan2}
                if len(translatedrscan2 & scan1) > 11:
                    return True, translatedrscan2, len(translatedrscan2 & scan1), -vecdiff
    return False, ''


def findBeacons():
    scannerstack = [(0, scanners[0])]
    seen = set()
    realbeacons = set()
    realscanners = [array((0, 0, 0)) for _ in range(size)]
    while scannerstack:
        idx, scanner = scannerstack.pop()
        seen |= {idx}
        realbeacons |= scanner
        scancovers = {list(cover - {idx})[0] for cover in covers if idx in cover and len(cover & seen) < 2}
        overlaps = {i: checkOverlap(scanner, scanners[i]) for i in scancovers}
        for i in scancovers:
            if overlaps[i][0]:
                realscanners[i] = overlaps[i][3]
        overlaps = [(i, overlaps[i][1]) for i in scancovers if overlaps[i][0]]
        scannerstack += overlaps
    return realbeacons, realscanners


def l1(v1, v2):
    x1, y1, z1 = v1
    x2, y2, z2 = v2
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


with open('day19.txt') as f:
    raw = f.read().splitlines()
    scanners = []
    j = 0
    start = False
    for i in range(len(raw)):
        line = raw[i]
        if 'scanner' in line:
            start = True
            scanners.append(set())
        elif line == '':
            start = False
            j += 1
        elif start:
            beac = tuple(map(int, line.split(',')))
            scanners[j].add(beac)

    totalvertices = sum(len(beacon) for beacon in scanners)

    edgeslist = [list(combinations(scan, 2)) for scan in scanners]
    distances = [{edge: l1(*edge) for edge in edges} for edges in edgeslist]

    size = len(scanners)

    # Dictionary containing, for each pair (i,j) of scanners,
    # the set of common distances between beacons seen by each of them
    inter = {(i, j):
                 set(distances[i].values()) & set(distances[j].values())
             for i, j in combinations(range(size), 2)}

    # Dictionary containing, for each pair (i,j) of scanners,
    # the list of edges between beacons, seen by each of them, which realise said the distances found above
    meet = {(i, j):
                [{v: {edge for edge in distances[i] if distances[i][edge] == v} for v in inter[i, j]}] +
                [{v: {edge for edge in distances[j] if distances[j][edge] == v} for v in inter[i, j]}]
            for i, j in combinations(range(size), 2)}

    meetvertices = {(i, j):
                        [sum(set().union(*meet[i, j][0].values()), ())] +
                        [sum(set().union(*meet[i, j][1].values()), ())]
                    for i, j in combinations(range(size), 2)}

    # Dictionary containing, for each pair (i,j) of scanners,
    # the list of vertices which appear in some edge in the list above, and how many times it appears
    vertices = {(i, j):
                    [Counter(meetvertices[i, j][0])] +
                    [Counter(meetvertices[i, j][1])]
                for i, j in combinations(range(size), 2)}

    # Dictionary containing, for each pair (i,j) of scanners,
    # the sublist of the list above consisting of the vertices which appear at least 11 times
    overlapvertices = {(i, j):
                           [{k: v for k, v in vertices[i, j][0].items() if v > 10}] +
                           [{k: v for k, v in vertices[i, j][1].items() if v > 10}]
                       for i, j in combinations(range(size), 2)}

    overlappedbeacons = {(i, j): min(len(overlapvertices[i, j][0]), len(overlapvertices[i, j][1])) for i, j in
                         combinations(range(size), 2)}

    covers = [set(pair) for pair in combinations(range(size), 2) if overlappedbeacons[pair] > 11]

    realbeacons, realscanners = findBeacons()
    print('Parte 1:', len(realbeacons))

    realdistances = [l1(*edge) for edge in combinations(realscanners, 2)]
    print('Parte 2:', max(realdistances))
