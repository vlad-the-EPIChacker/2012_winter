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

f=open(sys.argv[1])
file=f.readlines()

for i in range(1, int(file[0])+1):
    print split(file[i])