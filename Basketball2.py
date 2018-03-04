## Anthony Dike started: 3/3/18
##
## This is VERSION 2 of a program that
## will simulate basketball games like NBA 2k.
##
## In this version I will add a welcome and closing message
## & add a feature that adds an overtime to the game
## if the score is tied after the regulation time.

import random

'''
Steps:
1) print a welcome message
2) modulate using functions
3) add if-else statement that makes a tie continue to an extra round
4) increase max score and allow random int to be added to tie
5) print regulation score and then if tie then print overtime score


'''

def OvertimeTeam1():
    overtimeAdder = random.randint(0,30)
    global Team1
    Team1 += overtimeAdder
    global team1OT
    team1OT = Team1
    return team1OT
    

def OvertimeTeam2():
    overtimeAdder = random.randint(0,30)
    global Team2
    Team2 += overtimeAdder
    global team2OT
    team2OT = Team2
    return team2OT
    


def Game():
    
    # create max and min scores
    maxScore = 122
    minScore = 98

    # initialize team variables
    global Team1
    Team1 = random.randint(minScore, maxScore)
    global Team2
    Team2 = random.randint(minScore, maxScore)

    # if tie trigger overtime
    if Team1 == Team2:
        print("There was an overtime!")
        print("REGULATION: Team1 - " + str(Team1) + " Team 2 - " + str(Team2))
        # prints overtime
        print("OVERTIME: Team 1 - " + str(OvertimeTeam1()) +
              " Team 2 - " + str(OvertimeTeam2()))
        
    else:
        print("SCORE: Team1 - " + str(Team1) + " Team 2 - " + str(Team2))
        


# welcome message
print()
print("----------------------------------------------")
print("| HELLO, WELCOME TO THE BASKETBALL SIMULATOR |")
print("----------------------------------------------")
print()


proceed = False

while proceed == False:
    print("\t Would you like to start a game?")
    print()
    answer = input("(YES or NO): ")
    print()
    
    if answer.lower() == "yes":
        print()
        Game()
        print()
    elif answer.lower() == "no":
        proceed = True
        break
    else:
        print("INVALID INPUT. Try Again.")
        print()

# closing message
print()
print("----------------------------------------------")
print("|       GOODBYE, THANK YOU FOR PLAYING!      |")
print("----------------------------------------------")
print()





