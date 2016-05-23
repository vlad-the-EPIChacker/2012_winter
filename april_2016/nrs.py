import sys

def serial(s):
    f=[]
    for i in range(0, len(s)):
        x=s[i]
        if i!=0:
            f.append(' ')
        f.append(nmb[x])
    print 'serial number',''.join(f)+'!'


f=open(sys.argv[1])
file=f.readlines()
nmb={}
nmb['0']='zero'
nmb['1']='one'
nmb['2']='two'
nmb['3']='three'
nmb['4']='four'
nmb['5']='five'
nmb['6']='six'
nmb['7']='seven'
nmb['8']='eight'
nmb['9']='nine'

for i in range(1, int(file[0])+1):
    data=file[i].split()
    print 'My name is', data[0], data[1]+',', data[2]+','
    serial(data[3])