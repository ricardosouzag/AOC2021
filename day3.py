import copy



with open("day3.txt", "r") as f:
    bins = f.read().splitlines()
    # bins = ['00100',
    #         '11110',
    #         '10110',
    #         '10111',
    #         '10101',
    #         '01111',
    #         '00111',
    #         '11100',
    #         '10000',
    #         '11001',
    #         '00010',
    #         '01010']
    size = len(bins)
    gamma = []
    n = len(bins[0])
    for i in range(n):
        aux = [bin[i] for bin in bins]
        gamma += [max(set(aux), key=aux.count)]
    epsilon = int(''.join('1' if x == '0' else '0' for x in gamma), 2)
    gamma = int(''.join(gamma),2)
    print("Parte 1:", gamma*epsilon)

    pos = 0
    O2 = copy.deepcopy(bins)
    m = n
    while n > 1:
        aux = [bin[pos] for bin in O2]
        auxsize = len(aux)
        mode = max(set(aux), key=aux.count)
        if mode != '1':
            if len([x for x in aux if x == mode]) <= auxsize/2:
                mode = '1'
        O2 = [bin for bin in O2 if bin[pos] == mode]
        n = len(O2)
        pos += 1

    pos = 0
    CO2 = copy.deepcopy(bins)
    while m > 1:
        aux = [bin[pos] for bin in CO2]
        auxsize = len(aux)
        mode = min(set(aux), key=aux.count)
        if mode != '0':
            if len([x for x in aux if x == mode]) >= auxsize / 2:
                mode = '0'
        CO2 = [bin for bin in CO2 if bin[pos] == mode]
        m = len(CO2)
        pos += 1

    O2, CO2 = int(''.join(O2),2), int(''.join(CO2),2)

    print('Parte 2:', O2*CO2)

