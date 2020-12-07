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
			
			children.append((child_colour, int(quantity)))

	return colour, children


lines = get_lines()

rules = {}
for line in lines:
	colour, child_colour_quantities = rule_factory(line)
	rules[colour] = child_colour_quantities


def check_child(colour, count):
	count += 1

	child_quantities = rules[colour]

	for c, q in child_quantities:
		for i in range(q):
			count = check_child(c, count)

	return count


childQuantitiesOfShinyGold = rules['shiny gold']

count = 0
for c, q in childQuantitiesOfShinyGold:
	for i in range(q):
		count = check_child(c, count)

print(count)
	