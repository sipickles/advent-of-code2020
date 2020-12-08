import sys
import copy

# A well-known fact
class SantaHatesInfiniteLoopsException(Exception):
	pass

def get_lines():
    with open('input.txt') as f:
        return f.read().splitlines()

def parse_line(line):
	op, val = line.split()
	val = val.replace('+', '')
	return [op, int(val), False]

def read_line(lines, pointer):
	op, val, executed = lines[pointer]
	if executed:
		raise SantaHatesInfiniteLoopsException()

	lines[pointer][2] = True
	return op, val
	
def process(line, pointer, acc):
	op, val = line
	if op == 'acc':
		acc += val
		pointer += 1
	elif op == 'jmp':
		pointer += val
	elif op == 'nop':
		pointer += 1
	return pointer, acc

# flip the next nop/jmp
def fixLine(lines, corruptLine):
	while True:
		op, val, executed = lines[corruptLine]
		if op == 'acc':
			corruptLine += 1
		elif op == 'jmp':
			lines[corruptLine][0] = 'nop'
			return lines, corruptLine
		elif op == 'nop':
			lines[corruptLine][0] = 'jmp'
			return lines, corruptLine


lines = [parse_line(x) for x in get_lines()]
corruptLine = 0

# Create all possible permutations, each with a different fix
permutations = []
while corruptLine < len(lines):
	linesCopy = copy.deepcopy(lines)
	permutation, corruptLine = fixLine(linesCopy, corruptLine)
	permutations.append(permutation)
	corruptLine += 1

# Iterate until santa is happy
for p in permutations:
	pointer = 0
	acc = 0

	while True:
		try:
			line = read_line(p, pointer)
		except SantaHatesInfiniteLoopsException:
			break
		pointer, acc = process(line, pointer, acc)

		if pointer >= len(p):
			print('Complete', acc)
			sys.exit()
