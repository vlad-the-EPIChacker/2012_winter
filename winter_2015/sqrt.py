
def mysqrt(n):
    if n<0:
        return 'ERROR'
    n1=n/2
    acc=0.01
    if n<acc:
        return 0
    while abs((n/n1)-n1)>acc:
        q=n/n1
        if q>n1:
            n1=n1*1.5
        if q<n1:
            n1=n1*0.5
    return n1

print mysqrt(2)
print mysqrt(24)
print mysqrt(-1)
print mysqrt(0)
