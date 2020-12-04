
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

    count_min, count_max = get_range(tokens[0])
    ch = get_char(tokens[1])
    pw = tokens[2]

    # count of ch in pw
    count = pw.count(ch)

    if count >= int(count_min) and count <= int(count_max):
        print(ch, count_min, count_max, pw, count, "VALID")
        valid += 1
    else:
        print(ch, count_min, count_max, pw, count, "INVALID")
        invalid += 1

print(valid, invalid)