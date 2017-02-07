import sys

f=open(sys.argv[1])
file=f.readlines()

for i in range(0, len(file)):
    n=int(file[i])
    line=[n, 'degrees', '=', float(n/180.0), 'PI radians']
    if int(line[3])==line[3]:
        line[3]=int(line[3])
    elif int(line[3]*10)==line[3]*10:
        line[3]=str(line[3])+'0'
    if line[3]==1:
        line[3]=''
    line[3]=str(line[3])
    print line[0], line[1], line[2], line[3]+line[4

