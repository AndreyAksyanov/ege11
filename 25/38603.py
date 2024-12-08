cnt=0
i=700000
while cnt<5:
    i+=1
    nmin=i
    nmax=1
    for j in range(2, i//2+1):
        if i%j==0:
            nmin=min(nmin,j)
            nmax=max(nmax,j)
    if nmin != i and nmax != 1 and nmin != nmax:
        if (nmax+nmin)%10==8:
            cnt+=1
            print(i, nmax+nmin)

