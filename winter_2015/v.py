import sys

def draw(n):
    s=2*n-2
    for i in range(0, n):
        row=[' ',' ',' ',' ',' ',' ',' ',' ']
        row[i]='*'
        if i<n-1:
            row[s-i]='*'
        print ''.join(row)



f=open(sys.argv[1])
file=f.readlines()
inp=file[0].split()

for i in range(0, len(inp)):
    n=int(inp[i])
    draw(n)