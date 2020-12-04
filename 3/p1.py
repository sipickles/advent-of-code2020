
def get_lines():
    with open('input.txt') as f:
        return f.read().splitlines()

hits = 0
misses = 0

x = 0
dx = 3

tree = '#'

lines = get_lines()
for line in lines:
    x = x % len(line)

    location = line[x]
    print(line, x, location)

    if location == tree:
        hits += 1
    else:
        misses += 1
        
    x += dx


print(hits, misses, hits + misses)