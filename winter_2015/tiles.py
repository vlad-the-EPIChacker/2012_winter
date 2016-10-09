import sys

def math5(x):
    x=x.split()
    l=int(x[0])
    w=int(x[1])
    a=l*w
    a=a+a/10
    if  a%10==0:
        return a
    else:5
        return int(a)+1

f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])+1

for i in range(1, nfile):
    print math5(file[i])