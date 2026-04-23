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

def check (hiddenGridss, rows, columns):
    rows = (rows -1)*5
    indexOfChoose=rows+columns-1
    if hiddenGridss[indexOfChoose]=="$":
        return True
    if hiddenGridss[indexOfChoose]=="💣":
        return False

def updateGrid (hiddenGridsss, shownGridsss, rowss, columnss):
    rowss= (rowss-1) *5 
    indexOfCHOOSE=rowss+columnss-1
    shownGridsss[indexOfCHOOSE]=hiddenGridsss[indexOfCHOOSE]
    return shownGridsss


def displayGrid(gridDisplayed):
    for i in range (0,25,5): #goes (start,stop,step)
        print(gridDisplayed[i:i+5]) #go from 0->6 but doesn't do 6 only 5
#Telling Instructions

# EXAMPLE
print ("yo wsg dawg")
print ("we have this game to play against a cpu")
print ("theres going to be bombs and dollars")
print ("pick a bomb and you lose money")
print ("pick a dollar and you win money")
print ("You have 100$ to start")


#Asking For Wager and Diff 
Money=100
amountWager= int(input("How much do you want to wager: "))
Money=Money-amountWager
difficulty= int(input("How difficult do you want it 1-20?"))
difficultyForMult = difficulty * 0.25
multiplier=1.1+difficultyForMult
hiddenGridFR= changeGrid (hiddenGrid,difficulty)
#testing displayGrid(hiddenGridFR)


#underContruction
goAgain="Y"


choice1=input ("Do you want to do choose or random: ")

if choice1=="choose":
    while goAgain=="Y":
        displayGrid(shownGrid)
        row=int(input("Please pick a row: "))
        column=int(input("Please pick a column: "))

        if check(hiddenGridFR, row, column) == True:
            amountWager= amountWager * multiplier
            print("You earned $", amountWager,)
            shownGrid=updateGrid (hiddenGridFR, shownGrid, row, column)
            displayGrid(shownGrid)
            goAgain==input("Do you want to keep going (Y/N): ")
                

        elif check(hiddenGridFR, row, column == False):
            print ("\n\n\nYou blew up...")
            print ("You have now only have $", Money)
            displayGrid (hiddenGridFR)
            goAgain="L"
    if goAgain=="N":
        Money=Money+amountWager
        print ("You made $",amountWager, "Now you have a total of $", Money)


        
            
            

    



