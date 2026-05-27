import difflib
from random import Random

import helper

board = ['-','-','-','-','-','-','-','-','-']
turn = 0
diff:int = 10

def main():
    initGame()

def initGame():
    global diff
    m = helper.getTextInput("Would you like to play a game of Tic Tac Toe? (y/n)", {0, 1})
    match m:
        case 1:
            diff = helper.getTextInput("Select a difficulty (e/m/h)", {10, 11, 12})
            playerStarting = (helper.getTextInput("Did you want to go first? (y/n/r)", {0, 1, 2}))
            startGame(isPlayerStarting(playerStarting))
        case 0:
            print("Bye! :)")

def isPlayerStarting(starting:int)->bool:
    playerStarting:bool = bool(Random().choice([0, 1])) if starting == 2 else bool(starting)
    return playerStarting

def startGame(playerStarting:bool):
    global turn, board
    turn = 0
    board  = ['-','-','-','-','-','-','-','-','-']
    gameStep(not playerStarting)
    

def gameStep(isTurn:bool):
    global turn, board
    turn += 1
    if isTurn:
        match diff:
            case 10:
                print("happened1")
                i = Random().randint(0, 9 - turn) #9 possible squares, with 0-based indexing. Turn 1 means 0-8. Is inclusive
                for j in range(0,9):
                    if board[j] == '-':
                        if i == 0:
                            board[j] = 'o' if turn % 2 == 1 else 'x'
                            break
                        else: i -= 1
            case 11:
                None
            case 12:
                None
    else:
        printBoard()
        while True:
            x, y = tuple(a-b for a, b in zip(helper.getCoordInput("Where did you want to place your number? (c,r)"), (1, 1)))
            i = x + 3*y
            if board[i] == '-':
                board[i] = 'o' if turn % 2 == 1 else 'x'
                break
    # check if game over
    gameStep(not isTurn)

def printBoard():
    a, b, c = board[0:3], board[3:6], board[6:9]
    print(a, b, c, sep='\n')


main()