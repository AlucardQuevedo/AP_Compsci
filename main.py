import math
import random


hiddenGrid= ["$","$","$","$","$",
             "$","$","$","$","$",
             "$","$","$","$","$",
             "$","$","$","$","$",
             "$","$","$","$","$"]

shownGrid= ["x","x","x","x","x",
            "x","x","x","x","x",
            "x","x","x","x","x",
            "x","x","x","x","x",
            "x","x","x","x","x"]

def changeGrid (hiddenGrids,difficultie):
    indexCount=0
    listOfIndex=random.sample(range (0,24), difficultie) #gets random list 0-24 inclusive and difficulty amount of times
    while indexCount < len(listOfIndex):
        hiddenGrids[listOfIndex[indexCount]]= "💣"
        indexCount = indexCount + 1
    return hiddenGrids



#Telling Instructions

# EXAMPLE
print ("yo wsg dawg")
print ("we have this game to play against a cpu")
print ("theres going to be bombs and dollars")
print ("pick a bomb and you lose money")
print ("pick a dollar and you win money")
print ("You have 100$ to start")

for i in range (0,25,5): #goes (start,stop,step)
    print(shownGrid[i:i+5]) #go from 0->6 but doesn't do 6 only 5


#Asking For Wager and Diff 
amountWager= int(input("How much do you want to wager: "))
difficulty= int(input("How difficult do you want it 1-20?"))
difficultyForMult = difficulty * 0.25
multiplier=1.1+difficultyForMult

hiddenGridFR= changeGrid (hiddenGrid,difficulty)

print (hiddenGridFR)


choice1=input ("Do you want to do choose or random: ")

if choice1=="choose":
    row=int(input("Please pick a row: "))
    column=int(input("Please pick a column: "))


