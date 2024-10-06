f = open('17/64902.txt')
count=0
maxsum=0
n=[]
for i in f.readlines():
    n.append(int(i))
f.close()
nmax=0
for i in range(len(n)):
    if n[i]%1000==238:
        nmax=max(nmax, n[i])
for i in range(len(n)-2):
    a=n[i]
    b=n[i+1]
    c=n[i+2]
    d=a+b+c
    c2=0
    c3=0
    c5=0
    if 9999<a<100000:
        c2+=1
    if 9999<b<100000:
        c2+=1
    if 9999<c<100000:
        c2+=1
    if c2==1 or c2==2:
        if a%3==0:
            c3+=1
        if b%3==0:
            c3+=1
        if c%3==0:
            c3+=1
        if a%5==0:
            c5+=1
        if b%5==0:
            c5+=1
        if c%5==0:
            c5+=1
        if c3>c5:
            if d>nmax:
                count+=1
                maxsum=max(d, maxsum)
print(count, maxsum)
