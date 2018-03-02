## Anthony Dike started: 3/2/18
##
## This is VERSION 1 of a program that
## will simulate basketball games like NBA 2k.

import random

'''
Steps:

1) Create team variables. : Complete
2) Assign random int to team variables. : Complete
    - limit scores between 98 and 121
3) When program runs, print team scores.

'''

#initialize team variables
Team1 = random.randint(98, 121)
Team2 = random.randint(98, 121)

print("SCORE: Team1 - " + str(Team1) + " Team2 - " + str(Team2))
