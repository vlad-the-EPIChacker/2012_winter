import sys

f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    inp=file[i].split()
    x=int(inp[0])
    y=int(inp[1])
    m=int(inp[2])

    c=0
    d=0
    d1=0
    while d1+x<m:
        c=c+1
        d1=d1+x
        d1=d1-y
        d=d+x
        d=d+y
    c=c+1
    q=m-d1
    d=d+q
    print c, d