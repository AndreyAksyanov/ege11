a=0
b=0
for i in range(568023,569231):
    cnt=2
    for j in range(2, i//2+1):
        if i%j==0:
            cnt+=1
    if cnt>a:
        a=cnt
        b=i
print(a,b)
