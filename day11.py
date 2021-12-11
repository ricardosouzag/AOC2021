import copy
from itertools import product

import numpy as np


def getNeighbors(ocs):
	neighbors = [(x + 1, y) for x, y in ocs if x + 1 < r] \
	            + [(x - 1, y) for x, y in ocs if x - 1 > -1] \
	            + [(x, y + 1) for x, y in ocs if y + 1 < c] \
	            + [(x, y - 1) for x, y in ocs if y - 1 > -1] \
	            + [(x + 1, y + 1) for x, y in ocs if x + 1 < r and y + 1 < c] \
	            + [(x + 1, y - 1) for x, y in ocs if x + 1 < r and y - 1 > -1] \
	            + [(x - 1, y + 1) for x, y in ocs if x - 1 > -1 and y + 1 < c] \
	            + [(x - 1, y - 1) for x, y in ocs if x - 1 > -1 and y - 1 > -1]
	return sorted(neighbors)


with open('day11.txt') as f:
	octopi = np.matrix([[int(o) for o in line] for line in f.read().splitlines()])

	r, c = octopi.shape

	coords = list(product(range(r), range(c)))

	flashes = 0
	steps = 100
	allflash = []
	cnt = 0

	while not any(allflash):
		cnt += 1
		boom = set()

		for coord in coords:
			octopi[coord] += 1

		newboom = {coord for coord in coords if octopi[coord] > 9}
		boom |= newboom

		while any(newboom):
			flashes += len(newboom)
			neighs = getNeighbors(newboom)
			for neigh in neighs:
				octopi[neigh] += 1
			newboom = {coord for coord in coords if octopi[coord] > 9} - boom
			boom |= newboom

		for b in boom:
			octopi[b] = 0

		if len(boom) == r * c:
			allflash.append(cnt)

		if cnt == steps:
			print('Parte 1:', flashes)

	print('Parte 2:', allflash[0])
