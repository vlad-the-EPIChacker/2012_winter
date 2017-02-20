import sys

# standard input
# run as
# python yourProgram.py < yourFile.dat
for line in sys.stdin:
    print line.rstrip()

# read from file
#f=open(sys.argv[1])
#file=f.readlines()
#for line in file:
#    print line.rstrip()


