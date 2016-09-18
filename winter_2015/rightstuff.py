import sys

def solution(s):
    s=s.split()
    f=float(s[0])
    s=s[1:]
    ave=0.0
    big=0.0
    p=False
    pr=False
    smll=float(s[0])
    for i in s:
        i=float(i)
        ave=i+ave
    ave=ave/len(s)
    for ii in s:
        ii=float(ii)
        if ii>big:
            big=ii
        if ii<smll:
            smll=ii
    rng=big-smll
    if (abs(ave-f)/f)*100.0<=5:
        p=True
    if rng<=0.1*ave:
        pr=True
    if p and pr:
        return "Both"
    elif not p and not pr:
        return "Neither"
    elif p:
        return "Accurate"
    else:
        return "Precise"



f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    print solution(file[i])