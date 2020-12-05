def get_lines():
    with open('input.txt') as f:
        return f.read().splitlines()

def bitshift_binary(code, high_ch):
	shift = len(code) - 1
	value = 0
	for ch in code:
		if ch == high_ch:
			value += 1 << shift		
		shift -= 1

	return value

def convert_binary(code):
	code = code.replace('B', '1')
	code = code.replace('F', '0')
	code = code.replace('R', '1')
	code = code.replace('L', '0')
	return int(code, base=2)

codes = get_lines()
#codes = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

maxSeatId = -1

for code in codes:
	rowcode = code[:7]
	colcode = code[7:]

	seatId = convert_binary(rowcode) * 8 + convert_binary(colcode)
	maxSeatId = max(maxSeatId, seatId)

print(maxSeatId)

