import sys

def match1(w):
    x='No'
    if len(w)==0:
        return 'Yes'
    for i in symbols:
        if (w[0]).upper()==i:
            x=match1(w[1:])
            if x=='Yes':
                return 'Yes'
    if len(w)>1:
        for i in symbols:
            if (w[0]).upper()+w[1]==i:
                x=match1(w[2:])
                if x=='Yes':
                    return 'Yes'
    return 'No'


f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[4])
symbols=file[0].rstrip("\r\n\t")+' '+file[1].rstrip("\r\n\t")+' '+file[2].rstrip("\r\n\t")+' '+file[3].rstrip("\r\n\t")
symbols=symbols.split()

for i in range(5, nfile+5):
    w=file[i].rstrip("\r\n\t")
    print match1(w)
