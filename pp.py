import sys

def answer(line):
    line=line.split()
    for q in range(0, len(line)):
        line[q]=int(line[q])
    for n in range(0,1000):
        for m in range(0, 1000):
    return line

f=open(sys.argv[1])
file=f.readlines()

for i in range(1, int(file[0])+1  ):
    print answer(file[i])
