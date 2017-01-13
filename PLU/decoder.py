import sys

f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])

code={}
code['y']='a'
code['a']='e'
code['e']='i'
code['i']='o'
code['o']='u'
code['u']='y'
code['Y']='A'
code['A']='E'
code['E']='I'
code['I']='O'
code['O']='U'
code['U']='Y'

for i in range(1,nfile+1):
    line=file[i].rstrip()
    line=list(line)
    for ii in range(0, len(line)):
        l=line[ii]
        if l in code:
            line[ii]=code[l]
    line=''.join(line)
    print line