import sys
f=open(sys.argv[1])
file=f.readlines()

def test(s):
    s=s.split()
    a=int(s[0])
    b=int(s[1])
    c=int(s[2])
    a2=a*a
    b2=b*b
    c2=c*c
    if a2+b2==c2:
        return True
    else:
        return False

def test2(s1, s2):
    s1=s1.split()
    s2=s2.split()
    a1=int(s1[0])
    b1=int(s1[1])
    c1=int(s1[2])
    a2=int(s2[0])
    b2=int(s2[1])
    c2=int(s2[2])
    if not c1==c2:
        return False
    if not a1==b2:
        return False
    if not b1==a2:
        return False
    else:
        return True

for i in range(1, len(file), 2):
    if not test(file[i]):
        print 'NO'
        continue
    if not test(file[i+1]):
        print 'NO'
        continue
    if not test2(file[i], file[i+1]):
        print 'NO'
        continue
    print 'YES'
