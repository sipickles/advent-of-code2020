import re

def get_lines():
    with open('input.txt') as f:
        return f.read().splitlines()

def rule_factory(rule):
	colour = rule.split(' bags contain ')[0]

	pattern = r'(\d|no)\s(\w*\s\w*)'
	matches = re.findall(pattern, rule)
	children = []
	if matches:
		for quantity, child_colour in matches:
			if quantity == 'no':
				return colour, []
			
			children.append(child_colour)

	return colour, children


lines = get_lines()

rules = {}
for line in lines:
	colour, child_colours = rule_factory(line)
	rules[colour] = child_colours


def check_bag(colour):
	if colour == 'shiny gold':
		return True

	children = rules[colour]

	for c in children:
		if check_bag(c):
			return True


valid = []
for colour in rules:
	children = rules[colour]
	for c in children:
		if check_bag(c):
			if colour not in valid: 	
				valid.append(colour)

print(len(valid))
	