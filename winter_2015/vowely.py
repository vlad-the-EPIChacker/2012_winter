import sys

def vowel(w):
    v=0
    hs={'a':0,'e':0,'i':0,'o':0,'u':0,'y':0}
    w=w.rstrip('\r\n')
    for i in range(0, len(w)):
        if w[i] in hs:
            v=v+1
    v=float(v)
    if v/len(w)>=0.5:
        return 'YES'
    else:
        return 'NO'

f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])

for i in range(1,nfile+1):
    print vowel(file[i])