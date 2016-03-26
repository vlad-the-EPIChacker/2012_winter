import sys
f=open(sys.argv[1])
n=int(f.readline())
pr=1
for i in range(0, n):
    pr=pr*(i+1)
print pr