import sys

def cosmic(n):

f=open(sys.argv[1])
file=f.readlines()
nmb={}
nmb[1]='one'
nmb[2]='two'
nmb[3]='three'
nmb[4]='four'
nmb[5]='five'
nmb[6]='six'
nmb[7]='seven'
nmb[8]='eight'
nmb[9]='nine'

for i in range(1, int(file[0])+1):
