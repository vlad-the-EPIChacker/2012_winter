import sys

def answer(line):
    line=line.split()
    final=[]
    for q in range(0, len(line)):
        line[q]=int(line[q])
    a=line[0]
    b=line[1]
    sa=1
    sb=1
    for n in range(0,1000):
        if n==0:
            sa=1
        else:
              sa=sa*a
        sb=1
        for m in range(0, 1000):
            if m==0:
                sb=1
            else:
                sb=sb*b
            s=sa*sb
            if s<100000 and s>=10000:
                final.append(s)
            elif s>=100000:
                break

    for i in range(0, len(final)):
        final[i]=str(final[i])
    final=''.join(final)
    aaa=[i for i in final if i==str(line[2])]

    return len(aaa)


f=open(sys.argv[1])
file=f.readlines()

for i in range(1, int(file[0])+1  ):
    print answer(file[i])
