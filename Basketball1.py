## Anthony Dike started: 3/2/18
##
## This is VERSION 1 of a program that
## will simulate basketball games like NBA 2k.

import random

'''
Steps:

1) Create team variables.
2) Create max and min score values. (min 98 - max 122)
3) Assign random int to team variables.
4) When program runs, print team scores.

'''

# create max and min scores
maxScore = 122
minScore = 98

# initialize team variables
Team1 = random.randint(minScore, maxScore)
Team2 = random.randint(minScore, maxScore)

# print scores
print("SCORE: Team1 - " + str(Team1) + " Team2 - " + str(Team2))
