with open('day10.txt') as f:
	lines = f.read().splitlines()

	size = len(lines)

	opens = {
		'{': 1197,
		'[': 57,
		'(': 3,
		'<': 25137}
	closes = {
		'}': 1197,
		']': 57,
		')': 3,
		'>': 25137}

	glitches = []
	glitchedLines = []
	for i in range(size):
		line = lines[i]
		stack = []
		for char in line:
			if char in opens.keys():
				stack.append(char)
			elif char in closes.keys():
				if closes[char] == opens[stack[-1]]:
					stack.pop()
				else:
					glitchedLines.append(i)
					glitches.append(closes[char])
					break

	print('Parte 1:', sum(glitches))

	opens = {
		'{':3,
		'[':2,
		'(':1,
		'<':4}
	closes = {
		'}':3,
		']':2,
		')':1,
		'>':4}

	completions = []
	for i in range(size):
		if i in glitchedLines: continue
		line = lines[i]
		stack = []
		for char in line:
			if char in opens.keys():
				stack.append(char)
			elif char in closes.keys():
				stack.pop()
		completions.append(stack)

	completionScores = []
	for comp in completions:
		comp.reverse()
		score = 0
		for char in comp:
			score = score * 5 + opens[char]
		completionScores.append(score)

	completionScores.sort()

	print('Parte 2:', completionScores[int(len(completionScores)/2)])
