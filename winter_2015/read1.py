import sys

def aaa(glue):
    glue=glue.split(' ')
    w=len(glue)
    glue=''.join(glue)
    final=len(glue)/w
    if final>=8:
        return 'high'
    elif final<8 and final>=4:
        return 'medium'
    else:
        return 'low'

f=open(sys.argv[1])
file=f.readlines()
q=file[0]
i=1


while i<len(file):
    glue=''
    for ii in range(0, 3):
        line=file[i].rstrip('\r\n\t').lstrip('\r\n\t ')
        glue=glue+line+' '
        i=i+1
    glue=glue.rstrip(' ')
    print aaa(glue)
