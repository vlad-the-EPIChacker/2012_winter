import sys

def clear(x):
    y=''
    for i in range(0,len(x)):
        if not (x[i]=='\r' or x[i]== ' ' or x[i]== '\n' or x[i]=='\t'):
            y=y+x[i]
    return y
f=open(sys.argv[1])
file=f.readlines()
big=''
y=len(clear(file[0]))
z=False
for i in range(0,len(file)):
    x=len(clear(file[i]))
    if x==y:
        z=True
    else:
        z=False
        break
if z==True:
    print "It's a draw!Everybody wins!"
else:
    for i in range(0,len(file)):
        word=clear(file[i])
        if len(word)>len(big):
           big=word
    print big, "has won!"