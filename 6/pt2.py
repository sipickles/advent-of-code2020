def get_blocks():
    with open('input.txt') as f:
        return f.read().split('\n\n')

def get_lines(src: str):
	return src.splitlines()

def get_chars(src: str):
	return [char for char in src if char != '\n']


groups = get_blocks()
total = 0

for group in groups:
	current = None
	people = get_lines(group)
	for person in people:
		answer_list = get_chars(person)
		if current == None:
			current = set(answer_list)
			continue

		# Intersection of 2 sets
		current = current & set(answer_list)

	total += len(current)

print(total)
