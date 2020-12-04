import re

def get_blocks():
    with open('input.txt') as f:
        return f.read().split('\n\n')

def validate_year(src, key, minYear, maxYear):
    pattern = key + r':(\d{4})'
    match = re.search(pattern, src)   
    if match: 
        x = int(match.group(1))
        return x >= minYear and x <= maxYear

def validate_byr(src):
    return validate_year(src, 'byr', 1920, 2002)

def validate_iyr(src):
    return validate_year(src, 'iyr', 2010, 2020)

def validate_eyr(src):
    return validate_year(src, 'eyr', 2020, 2030)

def validate_hgt(src):
    pattern = r'hgt:(\d+)(cm|in)'
    match = re.search(pattern, src)   
    if match: 
        h = int(match.group(1))
        unit = match.group(2)
        if unit == 'cm':
            return h >= 150 and h <= 193
        elif unit == 'in':
            return h >= 59 and h <= 76

def validate_hcl(src):
    pattern = r'hcl:#[0-9a-f]{6}'
    return re.search(pattern, src) != None 
    
def validate_ecl(src):
    pattern = r'ecl:(amb|blu|brn|gry|grn|hzl|oth)'
    return re.search(pattern, src) != None 
    
def validate_pid(src):
    pattern = r'pid:\d{9}'
    return re.search(pattern, src) != None
        
valid = 0
invalid = 0

blocks = get_blocks()
for block in blocks:
    byr_ok = validate_byr(block) 
    iyr_ok = validate_iyr(block)
    eyr_ok = validate_eyr(block)
    hgt_ok = validate_hgt(block)
    hcl_ok = validate_hcl(block)
    ecl_ok = validate_ecl(block)
    pid_ok = validate_pid(block)
    
    block_valid = byr_ok and iyr_ok and eyr_ok and hgt_ok and hcl_ok and ecl_ok and pid_ok
    print(block)
    print('>', block_valid)
    if block_valid:
        valid += 1
        #x = input('next?')
    else:
        invalid += 1
        print(byr_ok, iyr_ok, eyr_ok, hgt_ok, hcl_ok, ecl_ok, pid_ok)

    print('---')


print(valid, invalid, valid + invalid)
