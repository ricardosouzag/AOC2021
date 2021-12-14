def DoOneStep(pairs):
	newpairs = {}
	for pair, cnt in pairs.items():
		x, y = pair
		z = instructions[x + y]
		newpairs[x + z] = newpairs.get(x + z, 0) + cnt
		newpairs[z + y] = newpairs.get(z + y, 0) + cnt
	return newpairs


def GetPairs(polymer):
	return [tuple(polymer[j:j + 2]) for j in range(len(polymer) - 1)]


def CountFromPairs(elem, pairs):
	return sum([v for k, v in pairs.items() if elem == k[0]])


def GrowPolymer(steps):
	polypairs = GetPairs(template)
	polypairscounts = {poly:polypairs.count(poly) for poly in polypairs}

	ret = polypairscounts
	for i in range(steps):
		ret = DoOneStep(ret)

	counts = dict()
	for e in letters:
		counts[e] = counts.get(e, 0) + CountFromPairs(e, ret)
	counts[template[-1]] += 1

	return sorted([v for k, v in counts.items()])


with open('day14.txt') as f:
	raw = f.read().splitlines()
	template = raw[0]
	instructions = dict([int.split(' -> ') for int in raw[2:]])
	letters = set(instructions.values())

	part1 = GrowPolymer(10)
	print('Parte 1:', part1[-1] - part1[0])

	part2 = GrowPolymer(40)
	print('Parte 2:', part2[-1] - part2[0])
