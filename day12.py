def Neighbors(v):
	if v == 'end':
		return set()
	edgy = [e for e in edges if v in e]
	return {next(iter(e - {v})) for e in edgy} - {'start'}


def FindPaths(state):
	n = len(state)
	past, present = list(state.keys()), list(state.values())
	neighborList = [Neighbors(present[i]) - (set(past[i]) - bigcaves) for i in range(n)]
	if not any(neighborList):
		return {e for e in state if state[e] == 'end'}
	future = {}
	for i in range(n):
		if present[i] == 'end':
			future.update({
				              past[i]:present[i]})
		for neigh in neighborList[i]:
			future.update({
				              tuple(list(past[i]) + [neigh]):neigh})
	return FindPaths(future)


def FindPaths2(state):
	n = len(state)
	past, present = list(state.keys()), list(state.values())
	if set(present) == {'end'}:
		return state
	future = {}
	for i in range(n):
		if present[i] == 'end':
			future.update({
				              past[i]:present[i]})
			continue
		visited = [k for k, v in past[i]]
		toovisitedsmalls = {k for k, v in past[i] if k in smallcaves and v > 1}
		if not any(toovisitedsmalls):
			neighbors = Neighbors(present[i])
		else:
			neighbors = Neighbors(present[i]) - (set(visited).difference(bigcaves))
		for neigh in neighbors:
			small = visited.count(neigh) + 1
			future.update({
				              (past[i] + ((neigh, small),)):neigh})
	return FindPaths2(future)


with open('day12.txt') as f:
	raw = f.read().splitlines()
	vertices = set(sum([line.split('-') for line in raw], []))
	edges = [set(line.split('-')) for line in raw]

	bigcaves = {v for v in vertices if v.isupper()}
	smallcaves = vertices - bigcaves - {'start', 'end'}

	start = {
		('start',):'start'}
	print('Parte 1:', len(FindPaths(start)))

	start2 = {
		(('start', -1),):'start'}
	print('Parte 2:', len(FindPaths2(start2)))
