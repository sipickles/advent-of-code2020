
def get_lines():
    with open('input.txt') as f:
        return f.read().splitlines()

def get_range(token):
    return token.split('-')

def get_char(token):
    return token[0]

valid = 0
invalid = 0

lines = get_lines()
for line in lines:
    tokens = line.split()

    p1, p2 = get_range(tokens[0])
    p1 = int(p1)
    p2 = int(p2)

    ch = get_char(tokens[1])
    pw = tokens[2]

    c1 = pw[p1 - 1]
    c2 = pw[p2 - 1]

    

    if (c1 == ch and c2 != ch) or (c1 != ch and c2 == ch):
        print(ch, p1, p2, pw, "VALID")
        valid += 1
    else:
        print(ch, p1, p2, pw, "INVALID")
        invalid += 1

print(valid, invalid)