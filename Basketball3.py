## Anthony Dike started: 3/8/18
##
## This is VERSION 3 of a program that
## will simulate basketball games like NBA 2k.
##
## In this version I will add
## 1) More Overtime and Sportcasting (announcers and stuff)
## 2) Notifier that says when team is blown out or a close game
## 3) Win Counter
##
## abbreviations:
## ffv: for future versions

"""
NOTES FOR PRE PUblISHING REFERENCES
- should probs make 1 game score print (ie if OT played, oly print OT)
"""

import random

'''
Steps:
1) add more emotive print statement
    - for ots, for close games
    - make a random function that causes events based on random ints
    (snow, rain, winter, summer, celebrities, etc) and make sportscasters
    react to that news while talking. DONE
2) 
3) make function that counts how many ots occur and if one doesnt
    happen after a certain number of times (maybe make that counter # random 1-10)
    then an ot game is played
4) 
5) 
'''

# EVENT SPEECH TRIGGER FUNCTIONS
#def RandomizeEventTriggers():
    # use dictionary or list to store event functions

    # randomize selection from the container
    



    
def WeatherTrigger():
    # weather list
    weather = ['rain', 'snow', 'sunny']

    #randommize index int
    weatherToday = weather[random.randint(0,(len(weather) - 1))]

    #choose random weather
    return weatherToday

def RainTalk():
    # commentary list on rain
    rainTalk = [
        "I hope you all have your umbrellas tonight, sports fans, 'cuz it'll be raining all night!",
        "It's raining cats and dogs outside tonight, sports fans!",
        "It's been so hot lately, glad we got some rain to cool things down!"
        ]
    
    # randomize index int
    rainTalkChoice = rainTalk[random.randint(0,(len(rainTalk) - 1))]

    # choose random commentary choice
    return rainTalkChoice

def SnowTalk():
    # commentary list on rain
    snowTalk = [
        "Stay warm sports fans, it's freezing outside today!",
        "It is absolutely frigid outside today in the city, hope y'all are warm!",
        "Lets all enjoy this game, while the temperatures drop outside!"
        ]

    # randomize index int
    snowTalkChoice = snowTalk[random.randint(0,(len(snowTalk) - 1))]

    # choose random commentary choice
    return snowTalkChoice

def SunnyTalk():
    # commentary list on rain
    sunnyTalk = [
        "It's a beautiful sunny day out today, sports fans!",
        "Wouldn't it be great if this game was played outside in the nice weather, sports fans? If only!",
        "Such a lovely sunny day for sports!"
        ]

    # randomize index int
    sunnyTalkChoice = sunnyTalk[random.randint(0,(len(sunnyTalk) - 1))]

    # choose random commentary choice
    return sunnyTalkChoice




    
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
    

def SportscastingIntro():
    # intro
    print("\nWelcome back sports fans! Time for another day of basketball!\n")
    #ffv: create team name variables

    # weather commentary
    weatherToday = WeatherTrigger()

    if weatherToday == 'rain':
        print(RainTalk())
        print()
        
    elif weatherToday == 'snow':
        print(SnowTalk())
        print()

    elif weatherToday == 'sunny':
        print(SunnyTalk())
        print()

    


    
# where the team points calc takes place 
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
        otScore1 = OvertimeTeam1()
        otScore2 = OvertimeTeam2()
        print("There was an overtime!")
        # prints overtime
        print("OVERTIME: Team 1 - " + str(otScore1) +
              " Team 2 - " + str(otScore2))
        print()
        if otScore1 == otScore2:
            Team1 = otScore1
            Team2 = otScore2
            dotScore1 = OvertimeTeam1()
            dotScore2 = OvertimeTeam2()
            print("After a well fought regulation and a grueling two overtimes, Team 1 finished with " +
             str(dotScore1) + " and Team 2 ended up with " + str(dotScore2))
            
        
    else:
         print("\nREGULATION: Team1 - " + str(Team1) + " Team 2 - " + str(Team2))
        


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
        SportscastingIntro()
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
