from collections import Counter
from itertools import combinations


def l1(v1, v2):
    x1, y1, z1 = v1
    x2, y2, z2 = v2
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


def getcopies(v):
    seen = frozenset({v})
    copies = [v]
    while copies:
        copii = copies.pop()
        seen |= frozenset({copii})
        for i, j in beaconpairs:
            if copii in beaconpairs[i, j]:
                newcopy = beaconpairs[i, j][copii]
                if not newcopy in seen:
                    copies += [newcopy]
    return seen


with open('day19.txt') as f:
    raw = f.read().splitlines()
    scanners = []
    j = 0
    start = False
    for i in range(len(raw)):
        line = raw[i]
        if 'scanner' in line:
            start = True
            scanners.append([])
        elif line == '':
            start = False
            j += 1
        elif start:
            beac = tuple(map(int, line.split(',')))
            scanners[j].append(beac)

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

    overlappedbeacons = {(i, j): len(overlapvertices[i, j][0]) for i, j in combinations(range(size), 2)}

    covers = [pair for pair in combinations(range(size), 2) if overlappedbeacons[pair] > 11]

    overlapedges = {(i, j):
                        [{edge for edge in edgeslist[i] if set(edge) <= overlapvertices[i, j][0].keys()}] +
                        [{edge for edge in edgeslist[j] if set(edge) <= overlapvertices[i, j][1].keys()}]
                    for i, j in combinations(range(size), 2)}

    beaconpairing = {(i, j):
                         [{beacon: Counter([l1(*e) for e in overlapedges[i, j][0] if beacon in e]) for beacon in
                           overlapvertices[i, j][0]}] +
                         [{beacon: Counter([l1(*e) for e in overlapedges[i, j][1] if beacon in e]) for beacon in
                           overlapvertices[i, j][1]}]
                     for i, j in combinations(range(size), 2)}

    beaconpairs = {}
    for i, j in covers:
        for v1 in beaconpairing[i, j][0]:
            v1fingerprint = beaconpairing[i, j][0][v1]
            for v2 in beaconpairing[i, j][1]:
                v2fingerprint = beaconpairing[i, j][1][v2]
                if v1fingerprint == v2fingerprint:
                    beaconpairs[i, j] = beaconpairs.get((i, j), {}) | {v1: v2, v2: v1}
                    break

    copieslist = set(sum([[getcopies(vertex) for vertex in scanner] for scanner in scanners], []))
    print(len(copieslist))

    print(totalvertices)
