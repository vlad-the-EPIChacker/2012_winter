import sys

f=open(sys.argv[1])
file=f.readlines()

for i in range(1, int(file[0])+1):
    fruits=file[i].split()

