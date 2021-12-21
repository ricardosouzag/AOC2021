import ast
import math
from functools import reduce


def Add(snail1, snail2):
	return Snailfish('[' + snail1.sequence + ',' + snail2.sequence + ']')


class Snailfish:
	_symbols = {'[', ']', ','}

	def _canExplode(self):
		return any([v for k, v in self.depths.items() if v > 4 if len(ast.literal_eval(k[0])) > 1])

	def _canSplit(self):
		return any([n for n in self.numlist.values() if int(n) > 9])

	def __init__(self, pairs):
		self.sequence = pairs
		self.GetDepths()
		self.Reduce()
		self.list = ast.literal_eval(self.sequence)

	def GetMagnitude(self):
		return self._GetMagnitude(self.list)


	def _GetMagnitude(self, arrlike):
		if isinstance(arrlike[0], int):
			val1 = arrlike[0]
		else:
			val1 = self._GetMagnitude(arrlike[0])

		if isinstance(arrlike[1], int):
			val2 = arrlike[1]
		else:
			val2 = self._GetMagnitude(arrlike[1])

		return 3 * val1 + 2 * val2

	def Reduce(self):
		if self._canExplode():
			self.Explode()
			self.GetDepths()
			self.Reduce()
		elif self._canSplit():
			self.Split()
			self.GetDepths()
			self.Reduce()

	def GetDepths(self):
		openBrackets = 0
		self.numlist = {}
		self.depths = {}
		tempnumlist = []
		pairslist = []
		for i in range(len(self.sequence)):
			char = self.sequence[i]
			if char == '[':
				pairslist.append(i)
				openBrackets += 1
			elif char == ']':
				idx = pairslist.pop()
				self.depths.update({(self.sequence[idx:i + 1], idx): openBrackets})
				openBrackets -= 1
			elif char not in self._symbols:
				tempnumlist.append([i, self.sequence[i]])
		num = []
		i = 0
		j = 0
		while i < len(tempnumlist):
			while tempnumlist[i + j][0] == tempnumlist[i][0] + j:
				num.append(tempnumlist[i + j][1])
				j += 1
				if i + j >= len(tempnumlist):
					break
			self.numlist.update({tempnumlist[i][0]: ''.join(num)})
			i = i + j
			j = 0
			num = []
		self._numsIdx = sorted(list(self.numlist.keys()))

	def Explode(self):
		dead = [k for k, v in self.depths.items() if v > 4 if len(ast.literal_eval(k[0])) > 1][0]
		size = len(dead[0])
		deadlist = ast.literal_eval(dead[0])
		deadindex = dead[1]
		nums = deadindex + 1, deadindex + size - 1 - len(str(deadlist[1]))
		predead, postdead = self.sequence[:deadindex], self.sequence[deadindex + size:]
		first, second = self._numsIdx.index(nums[0]), self._numsIdx.index(nums[1])
		if first > 0:
			prevNumIdx = self._numsIdx[first - 1]
			prevNum = self.numlist[prevNumIdx]
			prevNumSize = len(prevNum)
			predead = predead[:prevNumIdx] + str(deadlist[0] + int(prevNum)) + predead[prevNumIdx + prevNumSize:]
		if self._numsIdx[second] != self._numsIdx[-1]:
			nextNumIdx = self._numsIdx[second + 1]
			nextNum = self.numlist[nextNumIdx]
			nextNumSize = len(nextNum)
			relnextNumIdx = nextNumIdx - (deadindex + size)
			postdead = postdead[:relnextNumIdx] + str(deadlist[1] + int(nextNum)) + postdead[
			                                                                        relnextNumIdx + nextNumSize:]
		dead = '0'
		self.sequence = predead + dead + postdead

	def Split(self):
		slashnum = [int(n) for n in self.numlist.values() if int(n) > 9][0]
		slash = str(slashnum)
		slashindex = self.sequence.find(slash)
		size = len(slash)
		preslash, postslash = self.sequence[:slashindex], self.sequence[slashindex + size:]
		left, right = math.floor(slashnum / 2), math.ceil(slashnum / 2)
		split = '[' + str(left) + ',' + str(right) + ']'
		self.sequence = preslash + split + postslash


with open('day18.txt') as f:
	raw = f.read().splitlines()

	# test1 = '[[[[4,3],4],4],[7,[[8,4],9]]]'
	# test2 = '[1,1]'
	# print(test1)
	# print(test2)
	# snailtest = Add(Snailfish(test1), Snailfish(test2))
	snailfeesh = [Snailfish(line) for line in raw]
	part1 = reduce(Add, snailfeesh)
	print('Parte 1:', part1.GetMagnitude())

	maxmag = 0
	while snailfeesh:
		snail1 = snailfeesh.pop()
		for snail2 in snailfeesh:
			addsnail1 = Add(snail1, snail2).GetMagnitude()
			addsnail2 = Add(snail2, snail1).GetMagnitude()
			maxmag = max(maxmag, addsnail1, addsnail2)

	print('Parte 2:', maxmag)



