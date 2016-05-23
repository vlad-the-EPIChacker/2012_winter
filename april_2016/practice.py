import sys

f=open(sys.argv[1])
file=f.readlines()

for i in range(1, int(file[0])+1):
    data=file[i].split()
    print data[0], "will be", int(data[1])+1, "next year."