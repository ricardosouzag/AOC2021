with open("day1.txt", 'r') as f:
    readings = [int(r) for r in f.read().splitlines()]
    inc = [1 for a, b in zip(readings, readings[1:]) if b > a]
    threestep = [1 for a, b in zip(readings, readings[3:]) if b > a]

print("Parte 1:", sum(inc))
print("Parte 2:", sum(threestep))
