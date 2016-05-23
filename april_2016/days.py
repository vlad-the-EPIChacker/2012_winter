import sys

def subtract(date, date2):
    m=int(date2[0])-int(date[0])
    d=int(date2[0])/2-int(date[0])/2+int(date2[1])-int(date[1])
    y=int(date2[2])-int(date[2])
    if y % 4 == 0:
        if y % 100==0:
            if y % 400==0:
                d=d+int(date2[2])/4-int(date[2])/4
        else:
            d=d+int(date2[2])/4-int(date[2])/4
    if m==0:
        if y!=0:
            d=d+365.0/y
    elif y==0:
        d=d+48.0/m
    else:
        d=d+48/m+365/y
    print d

f=open(sys.argv[1])
file=f.readlines()

for i in range(1,int(file[0])*2+1, 2):
    date=file[i].split()
    date2=file[i+1].split()
    subtract(date, date2)
