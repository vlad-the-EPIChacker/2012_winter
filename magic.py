import sys

def fun(rows, nex):
    a=[]
    sum=0
    sum1=0
    b={}
    for i in range(0, nex):
        a.append([int(ii) for ii in rows[i].split()])
    for i in a:
        for ii in i:
            if ii in b:
                print "not a magic square"
                return
            b[ii]=1
    for i in range(0, nex):
        sum=sum+a[0][i]
    for ii in range(0, nex):
        sum1=0
        for i in range(0, nex):
            sum1=sum1+a[ii][i]
        if sum1!=sum:
            print "not a magic square"
            return
    for ii in range(0, nex):
        sum1=0
        for i in range(0, nex):
            sum1=sum1+a[i][ii]
        if sum1!=sum:
            print "not a magic square"
            return
    sum1=0
    for i in range(0, nex):
        sum1=sum1+a[i][i]
    if sum1!=sum:
        print "not a magic square"
        return
    sum1=0
    for i in range(nex-1, -1, -1):
        sum1=sum1+a[i][i]
    if sum1!=sum:
        print "not a magic square"
        return
    print "magic square"

f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])
i=1
ii=0

while ii<nfile:
    nex=int(file[i])
    fun(file[i+1:i+nex+1], nex)
    i=i+nex+1
    ii=ii+1