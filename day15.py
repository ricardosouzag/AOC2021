import copy
from itertools import product

import numpy as np


def GetNeighbors(coord):
	x, y = coord
	neighbors = {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)} & coords
	if end in neighbors:
		neighbors = {end}
	return neighbors


def FindMaxPathLength(org):
	stack = [(org, set(), 0)]
	visited = {}
	minpathlen = 9 * (r + c)
	while stack:
		present, past, value = stack.pop()
		if present in visited:
			if visited[present] < value:
				continue
			else:
				visited[present] = value
		else:
			visited[present] = value
		past |= {present}
		if present == end:
			minpathlen = min(minpathlen, value + map[present])
		stack += [(neigh, past.copy(), value + map[present]) for neigh in GetNeighbors(present) - past]
	return minpathlen


with open('day15.txt') as f:
	raw = f.read().splitlines()
	map = np.matrix([[int(n) for n in list(line)] for line in raw])
	r, c = map.shape
	coords = set(product(range(r), range(c)))

	start = (0, 0)
	end = (r - 1, c - 1)

	print(FindMaxPathLength(start) - 1)
