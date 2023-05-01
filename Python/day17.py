from math import sqrt


def triangle(n):
	return int(n * (n + 1) / 2)


def antitriangle(n):
	return int((sqrt(1 + 8 * n) - 1) / 2)


def getxsintarget(x0):
	xs = {}
	runningx = 0
	for i in range(x0):
		runningx += x0 - i
		if runningx in targetxs:
			xs.update({i + 1: runningx})
	return x0, xs


def getysintarget(y0):
	ys = {}
	runningy = 0
	i = 0
	while runningy > targetVerticalBounds[0]:
		runningy += y0 - i
		if runningy in targetys:
			ys.update({i + 1: runningy})
		i += 1
	return y0, ys


with open('day17.txt') as f:
	raw = f.read().splitlines()
	line = raw[0]
	line = line.split(':')[1]
	target = line.split(',')
	targetHorizontalBounds = list(map(int, target[0][3:].split('..')))
	targetVerticalBounds = list(map(int, target[1][3:].split('..')))
	targetxs = set(range(targetHorizontalBounds[0], targetHorizontalBounds[1] + 1))
	targetys = set(range(targetVerticalBounds[0], targetVerticalBounds[1] + 1))

	maxvel = abs(targetVerticalBounds[0]) - 1
	maxheight = triangle(maxvel)
	print('Parte 1:', maxheight)

	minx = antitriangle(targetHorizontalBounds[0])
	maxx = targetHorizontalBounds[1]
	miny = targetVerticalBounds[0]
	maxy = maxvel

	reachedxs = {}
	for x in range(minx, maxx + 1):
		reachedxs |= {getxsintarget(x)[0]: getxsintarget(x)[1]} if getxsintarget(x)[1] else {}

	reachedys = {}
	for y in range(miny, maxy + 1):
		reachedys |= {getysintarget(y)[0]: getysintarget(y)[1]} if getysintarget(y)[1] else {}

	initspeeds = set()
	for x in reachedxs:
		for y in reachedys:
			if reachedxs[x].keys() & reachedys[y].keys():
				initspeeds |= {(x, y)}
			elif x in reachedxs[x] and [ysteps for ysteps in reachedys[y].keys() if ysteps >= x]:
				initspeeds |= {(x, y)}

	print('Parte 2:', len(initspeeds))
