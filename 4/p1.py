
def get_blocks():
    with open('input.txt') as f:
        return f.read().split('\n\n')

def get_fields(block):
    return block.split()

def get_field_name(field):
    return field[:3]

valid = 0
invalid = 0
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
required.sort()


blocks = get_blocks()
for block in blocks:
    fields = map(lambda f : get_field_name(f), get_fields(block))
    sortedFields = list(fields)
    sortedFields.sort()
    print(sortedFields)

    # ignore 'cid'
    if 'cid' in sortedFields:
        sortedFields.remove('cid')

    if (sortedFields == required):
        print('valid')
        valid += 1
    else:
        print('invalid')
        invalid += 1

    print('---')


print(valid, invalid, valid + invalid)
