#
#       Authors: Angelina Parker, Hayden Thai
#
#       Date Created: 3/18/2022
#
#       Program Description: The program is intended to simulate tic tac toe between two players. 
#
#

# Global Variables
isNoWinner = 0
gameBoard = [   ['_','_','_'],
                ['_','_','_'],
                ['_','_','_'] ]
count = 0


# Function definitons

def displayGameboard():
    for i in range(3):
        print("| ", end = " ")
        for(j) in range(3):
            print (gameBoard[i][j], " | ", end =" ")
        print()



def checkWinnerO():
    # check rows    
    for i in range(3):
        win = True
        for j in range(3):
            if gameBoard[i][j] != 'O':
                win = False
                break
        if win:
            return 1

    # check columns
    for i in range(3):
        win = True
        for j in range(3):
            if gameBoard[j][i] != 'O':
                win = False
                break
        if win:
            return 1

    # check \ diagonal
    win = True
    for i in range(3):
        if gameBoard[i][i] != 'O':
                win = False
                break
    if win:
            return 1

    #check / diagonal 
    win = True
    for i in range(3):
        if gameBoard[i][3-i-1] != 'O':
                win = False
                break
    if win:
            return 1
    return 0

def checkWinnerX():
    # check rows    
    for i in range(3):
        win = True
        for j in range(3):
            if gameBoard[i][j] != 'X':
                win = False
                break
        if win:
            return 1

    # check columns
    for i in range(3):
        win = True
        for j in range(3):
            if gameBoard[j][i] != 'X':
                win = False
                break
        if win:
            return 1

    # check \ diagonal
    win = True
    for i in range(3):
        if gameBoard[i][i] != 'X':
                win = False
                break
    if win:
            return 1

    #check / diagonal 
    win = True
    for i in range(3):
        if gameBoard[i][3-i-1] != 'X':
                win = False
                break
    if win:
            return 1
    return 0
    

# Main program is run
#
#   The main logic of the program goes as follows:
#
#   1. get input from the user and check if it's a valid placement
#   2. check if there's a winner
#   3. if no winner, switch players and keep playing
#
while isNoWinner == 0 and count < 9: 
        for x in range(5):
            print()
        displayGameboard()
        if count % 2 == 0 :
            print("User 1's turn")
            flag = True
            # get input from the user until its valid
            while flag:
                row = input ("enter row\n")
                col = input ("enter col\n")
                
                if gameBoard[int(row)][int(col)] == '_':
                    flag = False
                else:
                    print("Choose new space dumbass")
            
            # insert an X into our gameBoard if the cell value is empty
            gameBoard[int(row)][int(col)] = 'X'

            isNoWinner = checkWinnerX()
            # print("Is winner: ", isNoWinner, " ")

        elif(count % 2 == 1):
            print("User 2's turn")
            flag = True
            while flag:
                # get input from user
                row = input ("enter row\n")
                col = input ("enter col\n")
                
                if gameBoard[int(row)][int(col)] == '_':
                    flag = False
                else:
                    print("Choose new space dumbass")

            gameBoard[int(row)][int(col)] = 'O' 
            isNoWinner = checkWinnerO()

            
        count = count + 1
    
    
print()
print()
print()
print("Final Board")
displayGameboard()
for i in range(3):
    print()
print("User", (count+1)%2 + 1, " Wins!"    )