import sys

f=open(sys.argv[1])
file=f.readlines()

for ii in range(1, int(file[0])+1):
    x=4
    n=file[ii]
    n=n.rstrip('\r\n\t')
    if ii>1 and ii<int(file[0]):
        x=5
    for i in range(0, x):
        z=int(n)
        n=str(n)
        n=''.join(reversed(list(n)))
        x=int(n)
        n=x+z
    print n