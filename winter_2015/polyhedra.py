import sys

f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    VE=file[i].split()
    V=int(VE[0])
    E=int(VE[1])
    F=E-V+2
    print F