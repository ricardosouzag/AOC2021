from itertools import count, product, accumulate
from functools import reduce


def DeterministicDice():
	for i in count(1, 3):
		yield [varmod(i, 10), varmod(i + 1, 10), varmod(i + 2, 10)]


def GetPosition(startpos, dice):
	return varmod(startpos + dice, 10)


def dictadd(dict1, dict2):
	newdict = {}
	keys = dict1.keys() | dict2.keys()
	for key in keys:
		newdict[key] = dict1.get(key, 0) + dict2.get(key, 0)
	return newdict


def varmod(num, base):
	return ((num - 1) % base) + 1


def QuantumDiracDice(currvals, goal):
	newvals = {}

	for stat, cnts in currvals.items():
		pos, val = stat

		if val > goal - 1:
			newvals[stat] = dictadd(newvals.get(stat, {}), cnts)
			continue

		for die, amt in quantumDice.items():
			newpos = GetPosition(pos, die)
			newval = val + newpos
			newcnts = {k + 1: v * amt for k, v in cnts.items()}
			newvals[(newpos, newval)] = dictadd(newvals.get((newpos, newval), {}), newcnts)

	if [key for key in newvals.keys() if key[1] < goal]:
		return QuantumDiracDice(newvals, goal)

	return reduce(dictadd, newvals.values())


with open('day21.txt') as f:
	raw = f.read().splitlines()
	start = [int(line[-1]) for line in raw]

	player = {1: (start[0], 0), 2: (start[1], 0)}

	cnt = 0

	while not [v for k, v in player.items() if v[1] > 999]:
		for roll in DeterministicDice():
			move = sum(roll)
			if cnt % 2 == 0:
				endpos = GetPosition(player[1][0], move)
				player[1] = (endpos, player[1][1] + endpos)
			else:
				endpos = GetPosition(player[2][0], move)
				player[2] = (endpos, player[2][1] + endpos)
			cnt += 1
			if [v for k, v in player.items() if v[1] > 999]: break

	loser = min([v[1] for k, v in player.items()])
	print('Parte 1:', 3 * cnt * loser)

	quantum = list(product([1, 2, 3], repeat=3))
	quantumDice = [sum(die) for die in quantum]
	quantumDice = {dice: quantumDice.count(dice) for dice in quantumDice}

	quantum1 = QuantumDiracDice({(start[0], 0): {0: 1}}, 21)
	quantum2 = QuantumDiracDice({(start[1], 0): {0: 1}}, 21)

	p1list = [quantum1.get(i, 0) for i in range(1, max(quantum1.keys()) + 1)]
	p2list = [quantum2.get(i, 0) for i in range(1, max(quantum2.keys()) + 1)]

	p1leftovers = list(accumulate(p1list, lambda a, b: 27 * a - b, initial=1))[1:]
	p2leftovers = list(accumulate(p2list, lambda a, b: 27 * a - b, initial=1))[1:]

	p1wins = [p1list[i] if i == 0 else p1list[i] * p2leftovers[i - 1] for i in range(len(p1list))]
	p2wins = [p2list[i] * p1leftovers[i] for i in range(len(p2list))]

	print('Parte 2:', max(sum(p1wins), sum(p2wins)))
