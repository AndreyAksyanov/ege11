f=open('24/27421.txt')
n=f.readline()
f.close()
maxs=0
s=1
for i in range(1, len(n)):
    if n[i]!=n[i-1]:
        s+=1
    else:
        s=1
    maxs=max(maxs, s)
print(maxs)

