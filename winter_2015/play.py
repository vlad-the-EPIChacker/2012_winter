import sys

def button(n):
    n=int(n)
    s=1
    for i in range(0, n):
        print '*'*s
        s=s+2
    s=s-4
    for ii in range(0, n-1):
        print '*'*s
        s=s-2
    print ''

f=open(sys.argv[1])
inp=f.readlines()[0]
inp=inp.split()

for i in inp:
    button(i)