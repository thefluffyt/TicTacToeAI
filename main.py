
#Accepted responses
pos = ['y', 'yes']
neg = ['n','no']

dif: dict[str, int] = {'e': 1, 'easy': 1, 'm': 2, 'medium': 2, 'h': 3, 'hard': 3}
board = ['-','-','-','-','-','-','-','-','-']
turn = 0

def main():
    play = input("Would you like to play a game of Tic Tac Toe? (y/n)").lower()
    if pos.__contains__(play):
        diffInput = input("Select a difficulty (easy, medium or hard)").lower()
        if not dif.__contains__(diffInput): print(f"Response: '{diffInput}' is not an accepted response"); return
        diff = dif[diffInput]
        startingInput = input("Did you want to go first? (y/n/r)")
        startGame(diff)


    elif neg.__contains__(play): print("Bye! :)"); return
    else: print(f"Response: '{play}' is not an accepted response"); return

def startGame(diff:int):
    turn = 0
    board  = ['-','-','-','-','-','-','-','-','-']
    gameStep(not starting)
    

def gameStep(isTurn:bool):
    turn += 1




main()