from itertools import product
import numpy as np


def GetNeighbors(coord, grid):
	x, y = coord
	neighbors = {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)} & grid
	return neighbors


def H(point, target): return abs(point[0] - target[0]) + abs(point[1] - target[1])


def MinimizeCost(source, target, grid):
	rows, cols = grid.shape
	points = set(product(range(rows), range(cols)))

	opens = [source]
	openset = {source:(0, 0)}
	closed = set()

	while opens:
		opens.sort(key=lambda n:sum(openset[n]), reverse=True)
		node = opens.pop()
		g, h = openset[node]

		newopens = []
		for neigh in GetNeighbors(node, points):
			if neigh == target:
				return int(g + grid[target])
			if neigh in closed:
				continue
			if neigh in openset:
				gn, hn = openset[neigh]
				openset[neigh] = (min(gn, g + grid[neigh]), hn)
				continue
			newopens.append(neigh)
		opens += newopens

		openset.pop(node)
		closed.add(node)
		openset.update(
				{opennode:(g + grid[opennode], H(opennode, target)) for opennode
				 in
				 newopens}
				)


with open('day15.txt') as f:
	raw = f.read().splitlines()
	map = np.matrix([[int(n) for n in list(line)] for line in raw])
	r, c = map.shape
	coords = set(product(range(r), range(c)))

	start = (0, 0)
	end = (r - 1, c - 1)

	# print('Parte 1:', MinimizeCost(start, end, map))

	map2 = np.zeros((5 * r, 5 * c))
	for i in range(5):
		for j in range(5):
			for x, y in coords:
				map2[i * r + x, j * c + y] = ((map[x, y] + i + j - 1) % 9) + 1

	r2, c2 = map2.shape
	start2, end2 = (0, 0), (r2 - 1, c2 - 1)

	print(MinimizeCost(start2, end2, map2))
