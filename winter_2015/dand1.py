import sys

def calculate(a, d, r):
    a=[int(g) for g in a.split()]
    d=int(d)
    r=[int(g) for g in r.split()]
    f=[]

    for ii in range(0, len(r)):
        if r[ii]==19 or r[ii]==20:
            f.append('critical hit')
        elif r[ii]==1:
            f.append('miss')
        elif r[ii]+a[0]+a[1]>d:
            f.append('hit '+str(a[2]+a[0])+' point(s) damage')
        else:
            f.append('miss')
    return f


f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])
i=1


while i<nfile*3+1:
    a=file[i]
    d=file[i+1]
    r=file[i+2]
    f=calculate(a, d, r)
    for g in f:
        print g
    print ''
    i=i+3