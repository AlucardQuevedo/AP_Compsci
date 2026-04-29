import math
import random


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



def randoms(timesGoing,wager,multi,hiddenGridssss,shownGridssss):
    indexOfLists=0
    numOfSafeSpots=0
    RandomChosenSpot=random.sample(range(0,25),timesGoing) #timesgoing = 5
    #Outpit ^ RandomChoseSpot= [1,4,12,21,24]
    while indexOfLists in range (timesGoing):
        if hiddenGridssss[RandomChosenSpot[indexOfLists]]=="$": #If hiddengrid[index[index]] = $
            wager=wager*multi
            shownGridssss[RandomChosenSpot[indexOfLists]]=hiddenGridssss[RandomChosenSpot[indexOfLists]]
            displayGrid(shownGridssss)
            indexOfLists=indexOfLists+1
            numOfSafeSpots=indexOfLists
            print("You have guessed correct,", numOfSafeSpots, "times")
            print("\n\n")

        elif hiddenGridssss[RandomChosenSpot[indexOfLists]]=="💣":
            return 0
    return wager
        
            
            


    
#Telling Instructions

# EXAMPLE
print ("yo wsg dawg")
print ("we have this game to play against a cpu")
print ("theres going to be bombs and dollars")
print ("pick a bomb and you lose money")
print ("pick a dollar and you win money")
print ("You have 100$ to start")


#Asking For Wager and Diff 
keepGoing="Y"
Money=100
while Money > 0 and keepGoing=="Y": 
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
                goAgain=input("Do you want to keep going (Y/N): ")
                    

            elif check(hiddenGridFR, row, column == False):
                print ("\n\n\nYou blew up...")
                print ("You have now only have $", Money)
                displayGrid (hiddenGridFR)
                goAgain="L"
        if goAgain=="N":
            Money=Money+amountWager
            print ("You made $",amountWager, "Now you have a total of $", Money)

    elif choice1=="random":
        amountOfTimes=int(input("How many times do you want to go?: "))
        randomsOutput= randoms(amountOfTimes,amountWager,multiplier,hiddenGridFR,shownGrid)
        if randomsOutput==0:
            print ("You might have done well or done bad but ended up losing \n\nSorry You Lost, Now you only have $", Money)
        else:
            Money=Money+randomsOutput
            print ("YOOOO YOU NOW HAVE, $", Money )
    keepGoing = input ("Do you want to keep wagering (Y/N): ")
print ("THANK YOU FOR PLAYING, YOU ENDED WITH $", Money)





        
            
            

    



