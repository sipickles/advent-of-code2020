def get_blocks():
    with open('input.txt') as f:
        return f.read().split('\n\n')

def get_chars(src: str):
	return [char for char in src if char != '\n']

groups = get_blocks()

total = 0
for group in groups:
	answers = get_chars(group)
	total += len(set(answers))

print(total)
