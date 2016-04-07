import sys

def diamond(l):
    space=l-1
    star=1
    e=' '
    s='*'
    while star < l+1:
        print e*(space/2)+s*(star)+e*(space/2)
        space=space-2
        star=star+2
######bottom#########
    space=2
    star=l-2
    while space < l:
        print e*(space/2)+s*(star)+e*(space/2)
        space=space+2
        star=star-2


f=open(sys.argv[1])
file=f.readlines()
x = int(file[0])
for i in range(1, x+1):
    diamond(int(file[i]))