def triangle(n):
    return int(n * (n + 1) / 2)


with open("day7.txt") as f:
    crabs = f.read().split(',')
    crabs = [int(crab) for crab in crabs]

    m, M = min(crabs), max(crabs)

    crabbuckets = [crabs.count(i) for i in range(m, M + 1)]

    fuel1 = min([sum([crabbuckets[j] * abs(i - j) for j in range(m, M + 1)]) for i in range(m, M+1)])
    print('Parte 1:', fuel1)

    fuel2 = min([sum([crabbuckets[j] * triangle(abs(i - j)) for j in range(m, M + 1)]) for i in range(m, M+1)])
    print('Parte 2:', fuel2)
