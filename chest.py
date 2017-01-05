import sys

def chess(a):
    board=[list('-'*8),list('-'*8),list('-'*8),list('-'*8),list('-'*8),list('-'*8),list('-'*8),list('-'*8)]
    pos=((let[a[0]]-1),int(a[1])-1)
    board[pos[1]][pos[0]]='K'
    x=pos[0]+2
    y=pos[1]-1
    if x>-1 and x<8 and y>-1 and y<8:
        board[y][x]='?'

    x=pos[0]+2
    y=pos[1]+1
    if x>-1 and x<8 and y>-1 and y<8:
        board[y][x]='?'

    x=pos[0]-2
    y=pos[1]+1
    if x>-1 and x<8 and y>-1 and y<8:
        board[y][x]='?'

    x=pos[0]-1
    y=pos[1]+2
    if x>-1 and x<8 and y>-1 and y<8:
        board[y][x]='?'
x
    x=pos[0]+1
    y=pos[1]+2
    if x>-1 and x<8 and y>-1 and y<8:
        board[y][x]='?'

    x=pos[0]-2
    y=pos[1]-1
    if x>-1 and x<8 and y>-1 and y<8:
        board[y][x]='?'

    x=pos[0]+1
    y=pos[1]-2
    if x>-1 and x<8 and y>-1 and y<8:
        board[y][x]='?'

    x=pos[0]-1
    y=pos[1]-2
    if x>-1 and x<8 and y>-1 and y<8:
        board[y][x]='?'


    for nrow in range(len(board)-1,-1,-1):
        print ''.join([i+' ' for i in board[nrow]])

f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])
let={}
let['A']=1
let['B']=2
let['C']=3
let['D']=4
let['E']=5
let['F']=6
let['G']=7
let['H']=8




for i in range(1, nfile+1):
    pos=file[i].rstrip()
    chess(pos)
    print ''