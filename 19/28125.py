def f(x,h):
    if x>365 and h==3:
        return 1
    elif x<366 and h==3:
        return 0
    elif x>365 and h<3:
        return 0
    else:
        if h%2==0:
            return f(x+1, h+1) or f(x*6, h+1)
        else:
            return f(x+1, h+1) or f(x*6, h+1)
for i in range(1,366):
    if f(i,1)==1:
        print(i)
        break






