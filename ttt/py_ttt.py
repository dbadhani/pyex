
tic_tac = 1
w, h = 3, 3;
gs = [[0 for x in range(w)] for y in range(h)]

def printCurrent(gs):
    for i in range(w):
        for j in range(w):
            if (gs[i][j] == 1):
                print("o"),
            elif (gs[i][j] == 2):
                print("x"),
            else:
                print(" "),
        print
    
def checkDone(gs, x, y, tic_tac):
    ## Check column
    i=0
    while i < 3:
        if ( gs[x][i] != tic_tac ):
            break
        if ( i == 2):
            return 1     
        i += 1

    ## Check row
    i=0
    while i < 3:
        if ( gs[i][y] != tic_tac ):
            break
        if ( i == 2):
            return 1     
        i += 1

    ## Check diag
    i=0
    if ( x == y ):
        while i < 3:
            if( gs[i][i] != tic_tac):
                break
            if ( i == 2):
                return 1     
            i += 1

    ## Check anti-diag
    i=0
    if ( x + y == 2 ):
        while i < 3:
            if( gs[i][2-i] != tic_tac):
                break
            if ( i == 2):
                return 1     
            i += 1
    
    return 0
    
    
def getNext(gs):
    global tic_tac
    print('Enter your move: ')    
    next_move = raw_input().split(",")  
    
    i = int(next_move[0])
    j = int(next_move[1])

    ## validate
    if not ( 1 <= i <= 3):
        return

    if not ( 1 <= j <= 3):
        return
    
    i-=1
    j-=1
    if ( gs[i][j] == 1 or gs[i][j] == 2):
        return

    ## Update game state
    gs[i][j] = tic_tac

    done = 0
    done = checkDone(gs, i, j, tic_tac)

    if done == 1:
        return 1       
    

    if ( tic_tac == 1):
        tic_tac = 2
    else:
        tic_tac = 1

    return 0

    
while 1:
    printCurrent(gs)
    won = getNext(gs)
    if (won == 1):
        printCurrent(gs)
        print "^^^^^^^^^^^^^^"
        print "You win buddy!"
        print "^^^^^^^^^^^^^^"
        exit()
