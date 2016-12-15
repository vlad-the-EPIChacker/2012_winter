import sys

def  tag(a):
    for i in range(0, len(a)):
        a[i]=a[i].rstrip('\n')
    jail={}
    stand={}
    for i in range(0, len(a)):
        s=a[i].split()
        for ii in jail:
            if len([True for iii in jail[ii] if iii==s[0]])>0:
                print 'INVALID GAME'
                return
        if s[2] in jail:
            for i in jail[s[2]]:
                stand[i]=1
            jail[s[2]]=[]
        stand[s[2]]=0
        if not s[0] in jail.keys():
            jail[s[0]]=[]
        jail[s[0]].append(s[2])
        stand[s[0]]=1
    z=[ii for ii in stand if stand[ii]==1]
    if len(z)>1:
        print 'VALID GAME'
        print 'Unfinished'
    else:
        print 'VALID GAME'
        print z[0]
#    print stand
#    print jail

f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])
sh=0

for i in range(1, nfile+1):
    start=int(file[i+sh])
    tag(file[i+sh+1:i+sh+start+1])
    sh=sh+start