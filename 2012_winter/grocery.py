import sys

f=open(sys.argv[1])
file=f.readlines()
n=int(file[0])+1
x={}
for i in range(1, len(file)):
    if i==n:
        continue
    word=file[i].rstrip().lstrip()
    if file[i] in x.keys():
        print 'Tomatoes for youza!'
    else:
        x[word]=0
