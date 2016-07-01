import sys

f=open(sys.argv[1])
file=f.readlines()
n=int(file[0])

def recognize(r):
    if r[0]=='Women':
        if r[1]=='UK':
            r[1]='US'
            n=str(int(r[2])+2)
        else:
            r[1]='UK'
            n=str(int(r[2])-2)
    else:
        if r[1]=='UK':
            r[1]='US'
            n=str(int(r[2])+1)
        else:
            r[1]='UK'
            n=str(int(r[2])-1)
    print r[0], r[1], n

for i in range(1, n+1):
    s=file[i].split()
    recognize(s)