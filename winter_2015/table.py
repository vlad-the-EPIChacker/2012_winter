import sys

def table(n):
    n=int(n)
    for i in range(1, 11):
        print n,'X',i,'=',n*i

f=open(sys.argv[1])
file=f.readlines()

for i in range(1, int(file[0])+1):
    table(file[i])
    print ' '