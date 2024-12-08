a=(2*216**6+3*36**9-432)
s=''
while a>0:
    s=str(a%6)+s
    a=a//6
print(s.count('5'))
