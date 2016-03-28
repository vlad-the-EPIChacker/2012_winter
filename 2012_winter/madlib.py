import sys

def replace(x,z,y):
    f=''
    for i in range(0, len(x)):
        if x[i]==z:
            x[i]=y
    for i in range(0, len(x)):
        if i==0:
            f=f+x[i]
        else:
            f=f+' '+x[i]
    return f
#            print 'found'

f=open(sys.argv[1])
file=f.readlines()
sent=file[0].rstrip(' \r\n\t').lstrip(' \r\n\t')
verb=file[1].rstrip(' \r\n\t').lstrip(' \r\n\t')
noun=file[2].rstrip(' \r\n\t').lstrip(' \r\n\t')
#print sent, verb, noun
sent1=replace(sent.split(), 'VERB', verb)
print replace(sent1.split(), 'NOUN', noun)