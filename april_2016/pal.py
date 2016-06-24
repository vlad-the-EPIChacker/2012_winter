import sys

def check(n):
    i=0
    while n != int(''.join(reversed(str(n)))) and i<5:
        n=n+int(''.join(reversed(str(n))))
        i=i+1
    print n


f=open(sys.argv[1])
file=f.readlines()

for ii in range(1, int(file[0])+1):
    n=file[ii]
    n=n.rstrip('\r\n\t')
    n=int(n)
    check(n)
