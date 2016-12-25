import sys
import math

def gorf(abc):
    a=float(abc[0].rstrip())
    b=float(abc[1].rstrip())
    c=float(abc[2].rstrip())
    b2=b*b
    ac4=4*a*c
    deter=b2-ac4
    root=math.sqrt(deter)
    minb=-1*b
    a2=2*a
    x1=minb-root
    x1=x1/a2
    x2=minb+root
    x2=x2/a2
    x=x1-x2
    x=round(x,1)
    print x

f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    gorf(file[i].split())