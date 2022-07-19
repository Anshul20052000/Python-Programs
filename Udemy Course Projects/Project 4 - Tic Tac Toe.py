board = [' ' for x in range(10)]

def insertLetter(pos,letter):
    board[int(pos)] = letter

def printBoard(board):
    print("\n\t###################")
    print("\t#     |     |     #")
    print("\t#  " + board[1] + "  |  " + board[2] + "  |  " + board[3] + "  #")
    print("\t#     |     |     #")
    print("\t###################")
    print("\t#     |     |     #")
    print("\t#  " + board[4] + "  |  " + board[5] + "  |  " + board[6] + "  #")
    print("\t#     |     |     #")
    print("\t###################")
    print("\t#     |     |     #")
    print("\t#  " + board[7] + "  |  " + board[8] + "  |  " + board[9] + "  #")
    print("\t#     |     |     #")
    print("\t###################\n")

def isFreeSpace(pos):
    return board[pos] == ' '

def isBoardFull(board):
    if board.count(" ") > 0:
        return False
    else:
        return True

def isWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or (b[4] == l and b[5] == l and b[6] == l) or (b[7] == l and b[8] == l and b[9] == l) or (b[1] == l and b[4] == l and b[7] == l) or (b[2] == l and b[5] == l and b[8] == l) or (b[3] == l and b[6] == l and b[9] == l) or (b[1] == l and b[5] == l and b[9] == l) or (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True
    while run:
        move = input(" Please Select a Position to Enter the X between 1 to 9 : ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isFreeSpace(move):
                    run = False
                    insertLetter(move,psy)
                else:
                    print(" Sorry! This Space is Occupied...!")
            else:
                print(" Plese Type a Number between 1 and 9...")
        except:
            print(" Plese Type a Number...")

def computerMove():
    possibleMoves = [x for x,letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0
    for let in [csy,psy]:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy,let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,5,7]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
    return move

def selectRandom(li):
    for i in li:
        boardcopy = board[:]
        boardcopy[i] = csy 
        if isWinner(boardcopy,csy):
            move1 = int(i)
            return move1
        
    import random
    le = len(li)
    r = random.randrange(0,le)
    return li[r]

def main():
    print(" Tic Tac Toe Game...!")
    printBoard(board)
    while not(isBoardFull(board)):
        if not(isWinner(board,csy)):
            playerMove()
            printBoard(board)
        else:
            print("\n Sorry! You Lose...")
            break
        if not(isWinner(board, psy)):
            move = computerMove()
            if move == 0:
                print(" Game Tie")
                break
            else:
                insertLetter(move, csy)
                print(" Computer Placed an", csy,"on Position",move,".")
                printBoard(board)  
        else:
            print(" You Win!...")
            break
        if isBoardFull(board):
            print(" Game Tie")
            break

print("\n==================================================")
print("\n\t#################################")
print("\t#                               #")
print("\t#       ~~~~~~~~~~~~~~~~~       #")
print("\t#       #  TIC TAC TOE  #       #")
print("\t#       ~~~~~~~~~~~~~~~~~       #")
print("\t#                               #")
print("\t#################################")
name = input("\n Enter your Name : ")
print(" Welcome",name,"to the Tic Tac Toe Game , Designed by Anshul Verma ")
print("\n Rules :- ")
print("\t1. Follow the Instructions as you move Forward in the Game.")
print("\t2. Whenever you were asked to Input Number from 1 to 9 then please follow it. ")
print("\t3. Do not write any False Input in the Game.")
print("\n Board Numbers :- ")
print("\n\t###################")
print("\t#     |     |     #")
print("\t#  1  |  2  |  3  #")
print("\t#     |     |     #")
print("\t###################")
print("\t#     |     |     #")
print("\t#  4  |  5  |  6  #")
print("\t#     |     |     #")
print("\t###################")
print("\t#     |     |     #")
print("\t#  7  |  8  |  9  #")
print("\t#     |     |     #")
print("\t###################")
print("\n Let's Play the Game...\n")
print(" Which Symbol do you want to Choose...[1,2]...")
print(" \t1. ''X'' ")
print(" \t2. ''O'' ")
temp = input(" => ")
while True:
    if temp == '1':
        psy = 'X'
        csy = 'O'
        break
    elif temp == '2':
        psy = 'O'
        csy = 'X'
        break
    else:
        print("Please Enter a valid Input!...")    
main()
while True:
    x = input(" Do you want to Play Again...[Y/N]... : ")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print("-------------------------")
        main()
    else:
        print("\n\tThank You")
        break

        
            