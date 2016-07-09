import sys

def fcheck(word, lk):
    if not len(word)==len(lk):
        return None
    for i in range(0, len(lk)):
        if not lk[i]=='*':
            if not word[i]==lk[i]:
                return None

    return word
def prnt(r):
    rt=''
    for i in r:
        rt=rt+i+' '
    print rt

f=open(sys.argv[1])
file=f.readlines()
words=file[0:10]
lkfor=file[10:]
for i in range(0, len(lkfor)):
    lkfor[i]=lkfor[i].rstrip('\n')
for i in range(0, len(lkfor)):
    tfinal=[]
    for ii in range(0, len(words)):
        line=words[ii].split()
        for iii in range(0, len(line)):
            word=line[iii]
            x=fcheck(word, lkfor[i])
            if not None==x:
                tfinal.append(x)
    if len(tfinal)!=0:
        prnt(tfinal)
    else:
        print 'NO MATCH'