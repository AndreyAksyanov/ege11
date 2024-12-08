for i in range(312614,312652):
    d=[1,i]
    for j in range(2, i//2+1):
        if i%j==0:
            d.append(j)
    if len(d)==6:
        print(d, d.sort())
