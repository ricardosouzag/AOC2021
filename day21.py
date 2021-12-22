import itertools
from collections import Counter
from functools import reduce


def DeterministicDice():
	for i in itertools.count(1, 3):
		yield [varmod(i - 1, 10), varmod(i, 10), varmod(i + 1, 10)]


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


def Reach21(currvals):
	newvals = {}
	for stat, cnts in currvals.items():
		pos, val = stat
		if val > 20:
			newvals[stat] = dictadd(newvals.get(stat,{}), cnts)
			continue
		for die, amt in quantumDice.items():
			newpos = GetPosition(pos, die)
			newval = val + newpos
			newcnts = {k + 1: v * amt for k, v in cnts.items()}
			newvals[(newpos, newval)] = dictadd(newvals.get((newpos, newval), {}), newcnts)

	if [key[1] for key in newvals.keys() if key[1] < 21]:
		return Reach21(newvals)
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
	print(3 * cnt * loser)

	quantum = list(itertools.product([1, 2, 3], repeat=3))
	quantumDice = [sum(die) for die in quantum]
	quantumDice = {dice: quantumDice.count(dice) for dice in quantumDice}

	quantum1, quantum2 = Reach21({(start[0], 0): {0: 1}}), Reach21({(start[1], 0): {0: 1}})

	p1wins = sum([v1 * sum([v2 for k2,v2 in quantum2.items() if k1 <= k2]) for k1,v1 in quantum1.items()])
	p2wins = sum([v1 * sum([v2 for k2,v2 in quantum2.items() if k1 > k2]) for k1,v1 in quantum1.items()])

	print(p1wins, p2wins, max(p1wins, p2wins))
