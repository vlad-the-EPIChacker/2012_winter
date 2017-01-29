import sys

f=open(sys.argv[1])
l=f.readlines()
i=0
ships={}
sum=0
order=[]

while l[i].rstrip()!='0':
    l[i]=l[i].rstrip()
    if l[i] in ships.keys():
        ships[l[i]]=ships[l[i]]+1
    else:
        order.append(l[i])
        ships[l[i]]=1
    i=i+1

for ship in order:
    sum=sum+ships[ship]
    print ship+':', ships[ship]
print 'GRAND TOTAL:', sum