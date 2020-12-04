import sys

with open('input.txt') as f:
    data = f.read().splitlines()

    for sx in data:
        x = int(sx)
        for sy in data:
            y = int(sy)
            for sz in data:
                z = int(sz)

        
                # if x == y || : 
                #     continue

                if (x + y + z) == 2020:
                    print(x, y, z, x * y * z)
                    #sys.exit(x*y)