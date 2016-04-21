import sys

def tcase(fline, i):
    nmb={}
    x=0
    r=fline.split()
    if fline=='0 0':
        exit()
    ii=int(r[0])+int(r[1])
    for g in range(0,int(r[0])):
        if file[g+i+1] in nmb.keys():
            nmb[file[g+i+1]]+=1
        else:
            nmb[file[g+i+1]]=1

    for g in range(0,int(r[1])):
        if file[g+i+int(r[0])+1] in nmb.keys():
            nmb[file[g+i+int(r[0])+1]]+=1
        else:
            nmb[file[g+i+int(r[0])+1]]=1
    for h in nmb.keys():
        if nmb[h]>1:
            x=x+1


    return (ii+1,x)

f=open(sys.argv[1])
file=f.readlines()
i=0

while i<len(file):
    f=tcase(file[i], i)
    i=f[0]+i
    print f[1]
