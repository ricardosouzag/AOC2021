import copy

import numpy as np


def DoFold(fold, map):
	dir, amt = fold.split('=')
	amt = int(amt)
	ret = set()
	if dir == 'x':
		for point in map:
			if point[0] < amt:
				ret.add(point)
			else:
				ret.add((2 * amt - point[0], point[1]))
	else:
		for point in map:
			if point[1] < amt:
				ret.add(point)
			else:
				ret.add((point[0], 2 * amt - point[1]))
	return ret


def ToMatrix(coords):
	xs, ys = [x for x, y in coords], [y for x, y in coords]
	mx, Mx = min(xs), max(xs)
	print(mx, Mx)
	my, My = min(ys), max(ys)
	print(my, My)
	mat = np.zeros([Mx - mx + 1, My - my + 1])
	for coord in coords:
		mat[coord] = 1
	return mat


with open('day13.txt') as f:
	raw = f.read().splitlines()
	instructions = [line.replace('fold along ', '') for line in raw if 'fold' in line]
	points = {tuple([int(x) for x in line.split(',')]) for line in raw if 'fold' not in line and any(line)}

	print('Parte 1:', len(DoFold(instructions[0], points)))

	res = copy.deepcopy(points)
	for inst in instructions:
		res = DoFold(inst, res)

	print('Parte 2:', ToMatrix(res))
