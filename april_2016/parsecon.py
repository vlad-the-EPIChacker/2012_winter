import sys

def split(s1):
    final=[]
    s2=''
    for i in range(0, len(s1)-4):
        if s1[i]=='+':
            final.append(s2)
            s2=''
        elif s1[i]=='-':
            final.append(s2)
            s2=''
            s2+=s1[i]
        else:
            s2+=s1[i]
    final.append(s2)
    return final

def find(srt1):
    subs={}
    subs['x^2']=0
    subs['xy']=0
    subs['y^2']=0
    subs['x']=0
    subs['y']=0
    nit=0
    for srt in srt1:
        n=0
        for i in subs:
            if not srt.find(i)==-1 and len(i)+srt.find(i)>=len(srt)-1:
                x=srt.find(i)
                if x==0:
                    subs[i]=1
                else:
                    if srt[0:x]=='-':
                        subs[i]='-1'
                    else:
                        subs[i]=srt[0:x]
                n=1
                break
        if n==0:
            nit=srt
    print subs['x^2'], subs['xy'], subs['y^2'], subs['x'], subs['y'], nit

f=open(sys.argv[1])
file=f.readlines()

for i in range(1, int(file[0])+1):
    find(split(file[i]))
