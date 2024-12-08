for i in range(210235,210301):
    d=[]
    for j in range(2, i//2+1):
        if i%j==0:
            d.append(j)
    if len(d)==4:
        print(d, d.sort())
