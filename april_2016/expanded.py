import sys

def expand(n):
    for i in range(0, len(n)-2):
        if n[i]=='0':
            continue
        x=len(n)-i-3
        print ' '*i+n[i]+'0'*x
    print '+-----'
    print n


f=open(sys.argv[1])
file=f.readlines()

for i in range(1, int(file[0])+1):
    n=file[i].lstrip('/r/n/t').rstrip('/r/n/t')
    expand(n)