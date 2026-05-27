
#Accepted positive and negative responses
pos = ['y', 'Y', 'yes', 'YES']
neg = ['n', 'N', 'no', 'NO']

play = input("Would you like to play a game of Tic Tac Toe? (y/n)")
if pos.__contains__(play):
    input("Select a difficulty (easy, medium or hard)")
elif neg.__contains__(play):
    print("Bye! :)")
else:
    print(f"Response: '{play}' is not an accepted response")
