print('x y z w')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if ((w or (not x)) and (w == (not y)) and (w <= z)):
                    print(x, y, z, w)
