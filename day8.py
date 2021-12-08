import numpy as np


letters = 'abcdefg'
displayDict = {'abcefg':0, 'cf':1, 'acdeg':2, 'acdfg':3, 'bcdf':4, 'abdfg':5, 'abdefg':6, 'acf':7, 'abcdefg':8, 'abcdfg':9}
displayDict = {frozenset(k):v for k,v in displayDict.items()}
lettersLens = {l: [sum([1 for d in displayDict.keys() if l in d and len(d) == i]) for i in range(10)] for l in letters}


def decode(sgnlist):
    code = sgnlist[-4:]
    lettersDict = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': ''}
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

starttime = time.time()
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
