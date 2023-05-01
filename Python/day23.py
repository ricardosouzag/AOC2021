from sympy import Matrix, zeros, pprint

with open('day23.txt') as f:
    raw = f.read().splitlines()
    rooms = []
    for i in range(1, 5):
        rooms.append((raw[3][2 * i + 1], raw[2][2 * i + 1]))

    coords = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 6),
        (0, 7),
        (0, 8),
        (0, 9),
        (0, 10),
        (1, 2),
        (1, 4),
        (1, 6),
        (1, 8),
        (2, 2),
        (2, 4),
        (2, 6),
        (2, 8),
    ]

    state = zeros(3, 11)
    initstate = state.copy()
    for i in range(1, 5):
        initstate[1, 2 * i] = rooms[i - 1][1]
        initstate[2, 2 * i] = rooms[i - 1][0]
    pprint(initstate)
