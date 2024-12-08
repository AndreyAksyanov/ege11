def f(x1, x2, h):
    if (x1+x2)>68 and h==4:
        return 1
    elif (x1+x2)<69 and h==4:
        return 0
    elif (x1+x2)>68 and h<4:
        return 0
    else:
        if h%2!=0:
            return f(x1+1, x2, h+1) or f(x1, x2+1, h+1) or f(x1*2, x2, h+1) or f(x1, x2*3, h+1)
        else:
            return f(x1+1, x2, h+1) and f(x1, x2+1, h+1) and f(x1*2, x2, h+1) and f(x1, x2*3, h+1)
for i in range(1, 59):
    if f(10,i,1)==1:
        print(i)
