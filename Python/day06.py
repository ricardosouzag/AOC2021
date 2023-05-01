def Day(fishes):
    aux = fishes[1:] + [fishes[0]]
    aux[6] += fishes[0]
    return aux

with open("day6.txt") as f:
    origfish = f.read().split(',')
    origfish = [int(fish) for fish in origfish]
    fishbuckets = [origfish.count(i) for i in range(9)]

    feesh = fishbuckets

    for i in range(80):
        feesh = Day(feesh)

    print('Parte 1:',sum(feesh))

    feesh = fishbuckets

    for i in range(256):
        feesh = Day(feesh)

    print('Parte 2:',sum(feesh))
