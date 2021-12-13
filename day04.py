import copy


def CheckCardBingo(ks):
    bingo = set()
    ks = tuple([tuple([tuple(e) for e in k]) for k in ks])
    n = len(ks[0])
    for k in ks:
        for row in k:
            if sum(row) == 0:
                bingo.add(k)
        for i in range(n):
            if sum([k[j][i] for j in range(n)]) == 0:
                bingo.add(k)
    return bingo

def Result(card):
    return sum(sum([[int(e) for e in card[i] if e != -1] for i in range(len(card))],[]))

with open("day4.txt", "r") as f:
    input = f.read().splitlines()
    calls = ([i.split(',') for i in input[:input.index('')]][0])
    parsedinput = input[input.index('') + 1:]
    cards = []
    while '' in parsedinput:
        card = [str(i).split() for i in parsedinput[:parsedinput.index('')]]
        for i in range(len(card)):
            card[i] = [int(e) for e in card[i]]
        cards += [card]
        parsedinput = parsedinput[parsedinput.index('') + 1:]

    n = len(cards[0])

    def SolveProblem1():
        for number in calls:
            for card in cards:
                for i in range(n):
                    if int(number) in card[i]:
                        card[i][card[i].index(int(number))] = 0
            winner = CheckCardBingo(cards)
            if any(winner):
                sol, = winner
                return Result(sol) * int(number)

    def SolveProblem2():
        N = len(cards)
        lastwinner = []
        for number in calls:
            if not any(lastwinner):
                for card in cards:
                    for i in range(n):
                        if int(number) in card[i]:
                            card[i][card[i].index(int(number))] = 0
                winners = CheckCardBingo(cards)
                if len(winners) + 1 >= N:
                    kards = set([tuple([tuple(e) for e in kard]) for kard in cards])
                    lastwinner, = kards-winners
                    lastwinner = [list(k) for k in lastwinner]
            else:
                for k in lastwinner:
                    if int(number) in k:
                        k[k.index(int(number))] = 0
                winner = CheckCardBingo([lastwinner])
                if any(winner):
                    sol, = winner
                    return Result(sol) * int(number)




    print('Parte 1:', SolveProblem1())
    print('Parte 2:', SolveProblem2())