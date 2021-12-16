from itertools import product
from queue import PriorityQueue
import numpy as np


def GetNeighbors(coord, grid):
	x, y = coord
	neighbors = {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)} & grid
	return neighbors


def H(point, target): return abs(point[0] - target[0]) + abs(point[1] - target[1])


def MinimizeCost(source, target, grid):
	rows, cols = grid.shape
	points = set(product(range(rows), range(cols)))

	opens = PriorityQueue()
	openset = {source:0}
	opens.put((H(source, target) + openset[source], source))

	while opens:
		h, node = opens.get()
		g = openset[node]

		for neigh in GetNeighbors(node, points):
			if neigh == target:
				return g + grid[target]
			neigh_g = g + grid[neigh]
			neigh_h = H(neigh, target)
			if neigh not in openset or openset[neigh] > neigh_g:
				openset.update({neigh:neigh_g})
				opens.put((neigh_h + neigh_g, neigh))


with open('day15.txt') as f:
	raw = f.read().splitlines()
	map = np.matrix([[int(n) for n in list(line)] for line in raw])
	r, c = map.shape
	coords = set(product(range(r), range(c)))

	start = (0, 0)
	end = (r - 1, c - 1)

	print('Parte 1:', MinimizeCost(start, end, map))

	map2 = np.zeros((5 * r, 5 * c), dtype=int)
	for i in range(5):
		for j in range(5):
			for x, y in coords:
				map2[i * r + x, j * c + y] = ((map[x, y] + i + j - 1) % 9) + 1

	r2, c2 = map2.shape
	start2, end2 = (0, 0), (r2 - 1, c2 - 1)

	print('Parte 2:', MinimizeCost(start2, end2, map2))
