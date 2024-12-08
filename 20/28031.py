def f(x,h):
    if x>34 and h==4:
        return 1
    elif x<35 and h==4:
        return 0
    elif x>34 and h<4:
        return 0
    else:
        if h%2!=0:
            return f(x+1, h+1) or f(x+2, h+1) or f(x*2, h+1)
        else:
            return f(x+1, h+1) and f(x+2, h+1) and f(x*2, h+1)
for i in range(1, 34):
    if f(i, 1)==1:
        print(i)
