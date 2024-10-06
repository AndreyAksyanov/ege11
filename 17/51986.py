f = open('17/51986.txt')
count=0
maxsum=0
n=[]
for i in f.readlines():
    n.append(int(i))
f.close()
nmin=0
for i in range(len(n)):
    if n[i]%10==5:
        nmin=min(nmin, n[i])
for i in range(len(n)-1):
    a=n[i]
    b=n[i+1]
    if a**2+b**2<nmin**2:
        if min(a,b)%10==5:
            count+=1
            maxsum=max(a**2+b**2, maxsum)
print(count, maxsum)
