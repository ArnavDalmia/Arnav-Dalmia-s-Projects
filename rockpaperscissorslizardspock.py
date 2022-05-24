# This program is a game called Rock Paper Scissors Lizard Spock. This program will run this game as a computer again a user using inputs.

# functions used:

# obtainPlayerMove() --- function verifies the validity of a user input and asks for valid user choice for game. Returns the choice of the player
#   variables used in function:
#       validChoice     boolean variable that is used to verify if the input is validChoice
#       playerChoice    string variable containging the players choice

# obtainComputerMove() --- function that uses random library to determine the computers choice. Returns computer choice
#   variables used in function:
#       choice          interger variable containing random number generated between 1 and 5
#       computerMove    string variable containing the choice of the computer

# winner(computerMove, playerMove) --- function that determines the winner using 2 arguements containing the player's choice and computer's choice. Returns a "0" if the player ties with the computer, or a "1" if the player wins, or a "2" if the computer wins. 
#   variables used in function:
#       computerMove    global string variable, arguement called containing the computers move
#       playerMove      global string variable, arguement called containing the players move

# displayScore() --- function that displays the score between the player and the computer
#   variables used in function:
#       computer_score  global integer variable containing the computers score
#       player_score    global integer variable containing the players score
#       gamesPlayed     global integer variable containing the amount of games that are played
#       ties            global integer variable containing the amount of ties

# displayRules() --- function that displays the rules of the game

# ----------- main program ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# random --- library called that is used to find random numbers. Used to determine the computers move

# variables used:
#   player_score, computer_score, gamesPlayed, ties, referenced in displayScore() function
#   gameOver        boolean variable that is used to ensure that the program runs until the game is over. For example, when it becomes 5-3 or 4-0 or 8-6.
#   computerMove    string variable containing the result of obtainComputerMove() function.
#   playerMove      string varialbe containing the result of obtainPlayerMove() function.
#   output          string variable that holds the output of what happened to the player in the game. For example if the player lost, the value of output = "LOSE"

#initialize function
def obtainPlayerMove():
    validChoice  = True #set boolean variable to True to start looping
    playerChoice = "" # create empty string variable
    #start loop
    while validChoice:
        #prmpt user for input, make input in full caps and check if it of the known options
        playerChoice = input("\nEnter ROCK, PAPER, SCISSORS, LIZARD, or SPOCK ---- ")
        playerChoice = playerChoice.upper()
        playerChoice = playerChoice.strip()
        if (playerChoice == "ROCK") or (playerChoice == "PAPER") or (playerChoice == "SCISSORS") or (playerChoice == "LIZARD") or (playerChoice == "SPOCK"):
            #if the choice is valid, the function will return the choice and terminate the loop
            return playerChoice
            validChoice = False
        else:
            #otherwise the loop continues until a valid input is inpuittted
            validChoice = True

#initialize function
def obtainComputerMove():
    #assign choice to a random number between 1 and 5. Depending on teh number the computers move will be chosen.
    choice = random.randint(1,5)
    if choice == 1:
        computerMove = "ROCK"
    elif choice == 2:
        computerMove = "PAPER"
    elif choice == 3:
        computerMove = "SCISSORS"
    elif choice == 4:
        computerMove = "LIZARD"
    else:
        computerMove = "SPOCK"
        
    return computerMove # returns computers move

#initialize function, takes 2 arguements
def winner(computerMove, playerMove):
    if computerMove == playerMove: #checks for tie
        return 0 #if tie return integer 0
    else:#checks all possabilites and either returns 1 or 2 depending on who wins. 1 if the player wins and 2 if the computer wins.
        if playerMove == "ROCK":
            if computerMove == "LIZARD":
                return 1
            elif computerMove == "SCISSORS":
                return 1 
            else:
                return 2
        elif playerMove == "PAPER":
            if computerMove == "ROCK":
                return 1
            elif computerMove == "SPOCK":
                return 1
            else:
                return 2 
        elif playerMove == "SCISSORS":
            if computerMove == "PAPER":
                return 1
            elif computerMove == "LIZARD":
                return 1
            else:
                return 2
        elif playerMove == "LIZARD":
            if computerMove == "SPOCK":
                return 1
            elif computerMove == "PAPER":
                return 1
            else:
                return 2
        elif playerMove == "SPOCK":
            if computerMove == "SCISSORS":
                return 1
            elif computerMove == "ROCK":
                return 1
            else:
                return 2

#initialize function
def displayScore():
    print("\nComputer SCORE: ", computer_score) #displays the computer score
    print("Player SCORE : ", player_score)#displays the player score
    print("You have played", gamesPlayed, "games so far. There has been",ties, "tie(s).") # dsiplays the amount of games played and the amount of ties

#initialize function, prints rules of game
def displayRules():
    print("Welcome to ROCK PAPER SCISSORS LIZARD SPOCK!")
    print("Rules: ")
    print("\tSCISSORS cuts PAPER, PAPER covers ROCK, ROCK crushes LIZARD, ")
    print("\tLIZARD poisons SPOCK, SPOCK smashes SCISSORS, SCISSORS decapitates LIZARD, ")
    print("\tLIZARD eats PAPER, PAPER disproves SPOCK, SPOCK vaporizes ROCK,")
    print("\tand as it always has, ROCK crushes SCISSORS")

#main program

import random # imports random which will be used in creating the computers move
random.seed()# initialize random number gnerator by selecting a random seed
    
player_score = 0 #assigns the first value of the scores, ties, and amount of games played to 0
computer_score = 0
ties = 0
gamesPlayed = 1


displayRules() #calls function to print rules
print("\n")#creates spacing for organization

gameOver = True # assigns boolean variable to True to be used in while loop
while gameOver: #commences while loop
    
    playersMove = obtainPlayerMove() # calls function obtainPlayerMove and stores return value in playersMove
    computerChoice = obtainComputerMove() # calls function obtainComputerMove and stores return value in computerChoice
    
    # uses winner function to determine the winner, checks the return value for being 0,1,2.
    if winner(computerChoice, playersMove) == 1: #if 1 is returned the player has won and their score will increase
        player_score += 1
        output = "WIN" #assigns output string variable to "WIN" as the player won
    elif winner(computerChoice, playersMove) == 2:#if 2 is returned the computer has won and their score will increase
        computer_score += 1
        output = "LOSE" #assigns output string variable to "LOSE" as the player lost
    else:
        ties += 1
        output = "TIED"#assigns output string variable to "TIED" as the player tied the computer

    print("The computer chooses",computerChoice+". YOU "+output+"!") #uses output variable to print if the player won, lost or tied
    displayScore()#calls function to display all scores
    
    gamesPlayed+=1 #adds to number of games played
    
    #this loop is used to check if the winner has at least achieved 4 points and that they have won by a minimum of 2 points
    if gamesPlayed >= 4: #checks if at least 4 games are played
        if player_score >= 4 or computer_score >= 4: #checks if any of the competitors scores have reached 4 points
            if (player_score > (computer_score + 1)) or (player_score < (computer_score - 1)): # ensures that if they have reached 4 points then they are also at least 2 points above
                gameOver = False # i;f all these conditions are met then the loop will stop and the game is over
            else:
                gameOver = True # if something happens along the way then the program continues to loop until its done






