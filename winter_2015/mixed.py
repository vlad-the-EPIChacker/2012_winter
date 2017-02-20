import sys

f=open(sys.argv[1])
file=f.readlines()
i=0

while file[i]!='0 0':
    frac=file[i].split()
    num=int(frac[0])
    den=int(frac[1])
    print num/den, num%den, '/', den
    i=i+1