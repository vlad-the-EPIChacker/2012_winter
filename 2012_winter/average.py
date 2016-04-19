import sys

def percent(tcase):
    ave=0
    n=0
    p=0
    tcase=tcase.split()
    for i in range(1, int(tcase[0])+1):
        ave=ave+int(tcase[i])
    ave=ave/float(tcase[0])
    ave=round(ave, 3)
    for i in range(1, int(tcase[0])+1):
        if int(tcase[i])>ave:
            n=n+1
    x=(float(tcase[0]))
    p=n/x
    p=p*100.0
    p=round(p, 3)
    return p



f=open(sys.argv[1])
file=f.readlines()

for i in range(1, int(file[0])+1):
    print '{0:.3f}'.format(percent(file[i]))+"%"