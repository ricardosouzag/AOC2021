def Neighbors(v):
	if v == 'end':
		return set()
	edgy = [e for e in edges if v in e]
	return {next(iter(e - {v})) for e in edgy} - {'start'}


def FindPaths(state):
	n = len(state)
	past, present = list(state.keys()), list(state.values())
	neighborList = [neighborsDict[present[i]] - (set(past[i]) - bigcaves) for i in range(n)]
	if not any(neighborList):
		return {e for e in state if state[e] == 'end'}
	future = {}
	for i in range(n):
		if present[i] == 'end':
			future.update(
					{
						past[i]:present[i]
						}
					)
		for neigh in neighborList[i]:
			future.update(
					{
						tuple(list(past[i]) + [neigh]):neigh
						}
					)
	return FindPaths(future)


def FindPaths2(state):
	n = len(state)
	prev, present = list(state.keys()), list(state.values())
	past, repeated = list(zip(*prev))
	repeated = list(repeated)

	if set(present) == {'end'}:
		return state

	future = {}
	for i in range(n):
		if present[i] == 'end':
			future.update(
					{
						prev[i]:present[i]
						}
					)
			continue

		visited = {k:v for k, v in past[i] if k in smallcaves}
		if not repeated[i]:
			neighbors = neighborsDict[present[i]]
		else:
			neighbors = neighborsDict[present[i]] - visited.keys()

		for neigh in neighbors:
			repeats = repeated[i]
			count = visited.get(neigh, 0) + 1
			if count > 1:
				repeats = True
			future.update(
					{
						((past[i] + ((neigh, count),)), repeats):neigh
						}
					)
	return FindPaths2(future)


with open('day12.txt') as f:
	raw = f.read().splitlines()
	vertices = set(sum([line.split('-') for line in raw], []))
	edges = [set(line.split('-')) for line in raw]

	bigcaves = {v for v in vertices if v.isupper()}
	smallcaves = vertices - bigcaves - {'start', 'end'}
	neighborsDict = {v:Neighbors(v) for v in vertices}

	start = {
		('start',):'start'
		}
	print('Parte 1:', len(FindPaths(start)))

	start2 = {
		((('start', -1),), False):'start'
		}
	print('Parte 2:', len(FindPaths2(start2)))
