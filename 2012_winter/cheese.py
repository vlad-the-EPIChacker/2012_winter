import sys
f=open(sys.argv[1])
word=f.readlines()[0]
word1='cheese'
if len(word)<len(word1):
    print word,"needs more cheese!"
    exit()
for i in range(0,6):
    if not word[i]==word1[i]:
        print word,"needs more cheese!"
        exit()
print word,"is cheezy!"