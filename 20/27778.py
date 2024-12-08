def f(x, y, h):
    if x+y<41 and h==4:
        return 1
    elif x+y>40 and h==4:
        return 0
    elif x+y<41 and h<4:
        return 0
    else:
        if h%2!=0:
            return f(x-1, y, h+1) or f(x, y-1, h+1) or f(x//2 + x%2, y, h+1) or f(x, y//2 + y%2, h+1)
        else:
            return f(x-1, y, h+1) and f(x, y-1, h+1) and f(x//2 + x%2, y, h+1) and f(x, y//2 + y%2, h+1)
for i in range(20, 1000):
    if f(i,20,1)==1:
        print(i)


