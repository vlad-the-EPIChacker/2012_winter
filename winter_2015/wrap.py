import sys

def crypt(m):
    final=[]
    for l in m:
        if l==' ':
            final.append(l)
        if ord(l)>=ord('a') and ord(l)<=ord('z'):
            base=ord('a')
            a=ord(l)-base+8
            b=a%26
            c=b+base
            d=chr(c)
            final.append(d)
        elif ord(l)>=ord('A') and ord(l)<=ord('Z'):
            base=ord('A')
            a=ord(l)-base-4
            if a+base>base:
                a=a+26
            b=a%26
            c=b+base
            d=chr(c)
            final.append(d)
        else:
            s=list(',.?!')
            for ii in range(0, len(s)):
                if s[ii]==l:
                    final.append(s[(ii+2)%4])

    return ''.join(final)

f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    file[i]=file[i].rstrip('\n\r\t')
    print crypt(file[i])