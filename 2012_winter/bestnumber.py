import sys

def biggest(x):
    final=1
    for i in range(0, len(x)):
        x[i]=float(x[i])
        if x[i]<1:
            x[i]=1/x[i]
        final=x[i]*final
    return final

def smallest(x):
    for i in range(0, len(x)):
        x[i]=float(x[i])
    x.sort()
    final=x[0]
    for i in range(0, len(x)):
        if x[i]<1:
            final=x[i]*final
        else:
           final=final/x[i]
    return final


f=open(sys.argv[1])
file=f.readlines()
if file[1].rstrip()=='biggest':
    print biggest(file[2:int(file[0])+2])
elif file[1].rstrip()=='smallest':
    print smallest(file[2:int(file[0])+2])