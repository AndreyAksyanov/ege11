def f(x, h):
    if x>67 and (h==3 or h==5):
        return 1
    elif x<68 and h==5:
        return 0
    elif x>67 and h<5:
        return 0
    else:
        if h%2!=0:
            return f(x+1, h+1) and f(x+4, h+1) and f(x*5, h+1)
        else:
            return f(x+1, h+1) or f(x+4, h+1) or f(x*5, h+1)
for i in range(1, 68):
    if f(i, 1)==1:
        print(i)
def n(x, h):
    if x>67 and h==3:
        return 1
    elif x<68 and h==3:
        return 0
    elif x>67 and h<3:
        return 0
    else:
        if h%2!=0:
            return n(x+1, h+1) and n(x+4, h+1) and n(x*5, h+1)
        else:
            return n(x+1, h+1) or n(x+4, h+1) or n(x*5, h+1)
for i in range(1, 68):
    if n(i, 1)==1:
        print(i)


