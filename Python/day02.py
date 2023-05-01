with open("day2.txt", "r") as f:
    commands = f.read().splitlines()
    commands = [(set(comm.split()[0][0]), int(comm.split()[1])) for comm in commands]
    fTotal = sum([k[1] for k in commands if "f" in k[0]])
    dTotal = sum([k[1] for k in commands if "d" in k[0]])
    utotal = sum([k[1] for k in commands if "u" in k[0]])
    dist = fTotal
    depth = dTotal - utotal


    print("Parte 1:", dist*depth)


    dist = 0
    depth = 0
    aim = 0
    for comm in commands:
        if "f" in comm[0]:
            dist += comm[1]
            depth += aim*comm[1]
        if "d" in comm[0]:
            aim += comm[1]
        if "u" in comm[0]:
            aim -= comm[1]

    print("Parte 2:", dist*depth)