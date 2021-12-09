letters = 'abcdefg'
displayDict = {
	frozenset('abcefg'): 0,
	frozenset('cf'): 1,
	frozenset('acdeg'): 2,
	frozenset('acdfg'): 3,
	frozenset('bcdf'): 4,
	frozenset('abdfg'): 5,
	frozenset('abdefg'): 6,
	frozenset('acf'): 7,
	frozenset('abcdefg'): 8,
	frozenset('abcdfg'): 9}
lettersLens = {l: [sum([1 for d in displayDict.keys() if l in d and len(d) == i]) for i in range(10)] for l in letters}


def decode(sgnlist):
	code = sgnlist[-4:]
	lettersDict = {
		'a': '',
		'b': '',
		'c': '',
		'd': '',
		'e': '',
		'f': '',
		'g': ''}
	sgnSet = {frozenset(sgn) for sgn in sgnlist}
	sgnlens = {l: [sum([1 for d in sgnSet if l in d and len(d) == i]) for i in range(10)] for l in letters}

	for l in letters:
		lettersDict[l] = [k for k, v in sgnlens.items() if lettersLens[l] == v][0]

	reverseDict = {v: k for k, v in lettersDict.items()}
	out = []
	for c in code:
		newc = frozenset([reverseDict[i] for i in c])
		out += [str(displayDict[newc])]

	return int(''.join(out))


with open('day8.txt') as f:
	inp = f.read().splitlines()
	inplines = [k[0] + k[1] for k in [i.split('|') for i in inp]]
	inplines = [i.split() for i in inplines]

	digits = [line[-4:] for line in inplines]
	alldigits = sum(digits, [])

	sol1 = [1 for dig in alldigits if len(dig) in [2, 3, 4, 7]]
	print('Parte 1:', sum(sol1))

	sol2 = []
	for line in inplines:
		sol2 += [decode(line)]

	print('Parte 2:', sum(sol2))
