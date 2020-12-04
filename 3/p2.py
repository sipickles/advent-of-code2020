from functools import reduce



def get_lines():
    with open('input.txt') as f:
        return f.read().splitlines()

hits = [0, 0, 0, 0, 0]
misses = [0, 0, 0, 0, 0]

deltas = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree = '#'

lines = get_lines()
stride = len(lines[0])

i = 0
while i < len(deltas):
    x = 0
    y = 0
    dx, dy = deltas[i]

    while y < len(lines):
        x = x % stride

        location = lines[y][x]
        #print(lines[y], x, location)

        if location == tree:
            hits[i] += 1
        else:
            misses[i] += 1
            
        x += dx
        y += dy


    print(hits[i], misses[i], hits[i] + misses[i])
    i += 1

answer = reduce(lambda x, y: x*y, hits)

print(answer)