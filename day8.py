import numpy as np

letters = 'pqrstuv'
origletters = 'abcdefg'
displayDict = ['pqrtuv', 'ru', 'prstv', 'prsuv', 'qrsu', 'pqsuv', 'pqstuv', 'pru', 'pqrstuv', 'pqrsuv']
displayDict = [set(d) for d in displayDict]
lettersLens = {l: [sum([1 for d in displayDict if l in d and len(d) == i]) for i in range(10)] for l in letters}
print(lettersLens)


def decode(sgnlist):
    code = sgnlist[-4:]
    lettersDict = {'p': '', 'q': '', 'r': '', 's': '', 't': '', 'u': '', 'v': ''}
    sgnSet = {frozenset(sgn) for sgn in sgnlist}
    sgnlens = {l: [sum([1 for d in sgnSet if l in d and len(d) == i]) for i in range(10)] for l in origletters}

    for l in letters:
        lettersDict[l] = [k for k, v in sgnlens.items() if lettersLens[l] == v][0]

    reverseDict = {v: k for k, v in lettersDict.items()}
    out = []
    for c in code:
        newc = set([reverseDict[i] for i in c])
        out += [str(displayDict.index(newc))]

    return int(''.join(out))


with open('day8.txt') as f:
    inp = f.read().splitlines()
    inplines = [k[0] + k[1] for k in [i.split('|') for i in inp]]
    inplines = [i.split() for i in inplines]
    signals, digits = np.transpose([i.split('|') for i in inp])
    digits = [dig.split() for dig in digits]
    alldigits = sum(digits, [])

    sol1 = [1 for dig in alldigits if len(dig) in [2, 3, 4, 7]]
    print('Parte 1:', sum(sol1))

    sol2 = []
    for i in range(len(inplines)):
        sol2 += [decode(inplines[i])]

    print('Parte 2:', sum(sol2))
