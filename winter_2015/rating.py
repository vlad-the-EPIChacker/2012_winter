import sys

f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])
m=[]
x=100000

for i in range(1, nfile+1):
    m.append(int(file[i]))
m=sorted(m)
for i in range(0, len(m)/2):
    m[i]=m[i]+m[len(m)-i-1]
for i in range(0, len(m)/2):
    if m[i]<x:
        x=m[i]

print x