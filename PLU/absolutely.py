import sys
f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    ns=file[i].split()
    n1=float(ns[0])
    n2=float(ns[1])
    dif=n1-n2
    if dif<0:
        dif=dif*-1
    dif=round(dif,1)
    print dif