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
		raise RuntimeError('Santa hates infinite loops')

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

pointer = 0
acc = 0
lines = [parse_line(x) for x in get_lines()]

while True:
	try:
		line = read_line(lines, pointer)
	except RuntimeError as e:
		print(e)
		print(acc)
		break
	pointer, acc = process(line, pointer, acc)



