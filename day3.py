import copy



with open("day3.txt", "r") as f:
    bins = f.read().splitlines()
    size = len(bins)
    gamma = []
    n = len(bins[0])
    for i in range(n):
        CO2aux = sum([int(bin[i]) for bin in bins])
        gamma += ['1' if CO2aux >= size / 2 else '0']
    epsilon = int(''.join('1' if x == '0' else '0' for x in gamma), 2)
    gamma = int(''.join(gamma),2)
    print("Parte 1:", gamma*epsilon)

    O2 = copy.deepcopy(bins)
    CO2 = copy.deepcopy(bins)

    for i in range(n):
        if len(O2) == 1 and len(CO2) == 1:
            break

        if len(O2) > 1:
            O2aux = [int(bin[i]) for bin in O2]
            O2auxsize = len(O2aux)
            O2aux = sum(O2aux)
            O2mode = ['1' if O2aux >= O2auxsize/2 else '0']
            O2 = [bin for bin in O2 if bin[i] == O2mode[0]]

        if len(CO2) > 1:
            CO2aux = [int(bin[i]) for bin in CO2]
            CO2auxsize = len(CO2aux)
            CO2aux = sum(CO2aux)
            CO2mode = ['0' if CO2aux >= CO2auxsize / 2 else '1']
            CO2 = [bin for bin in CO2 if bin[i] == CO2mode[0]]

    O2, CO2 = int(''.join(O2),2), int(''.join(CO2),2)

    print('Parte 2:', O2*CO2)

