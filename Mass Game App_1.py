#Import time module
import time

#Assign strategy names to variables
strat1Name = "recognitionStrat2"
strat2Name = "AdStrat2"

#Import the two strategies
strat1 = __import__(strat1Name)
strat2 = __import__(strat2Name)

def game():
    #Initialize variables
    score1 = 0
    score2 = 0
    
    snowballs1 = 1
    snowballs2 = 1
    
    ducksLeft1 = 5
    ducksLeft2 = 5
    
    movesSoFar1 = []
    movesSoFar2 = []
    
    roundNum = 0
    i = -1

    #Runs until someone wins (reaches score of 3)
    while score1 != 3 and score2 != 3:
        #Increment i
        i += 1
        
        #Use i to find out whos turn it is 
        if i % 2 == 0:
            #Reset booleans
            duckC1 = False
            duckC2 = False
            throwC1 = False
            throwC2 = False
            reloadC1 = False
            reloadC2 = False

            #Increase round number
            roundNum += 1

            #If not round 1, then add both moves that the players did to their specific arrays
            if roundNum > 1:
                movesSoFar1.append(curMove1)
                movesSoFar2.append(curMove2)

            #Set player number (which player is currently playing)
            myPlayerNumber = 1

            #Ask player for move and assign it to a variable
            curMove1 = strat1.getMove(myPlayerNumber, score1, score2, snowballs1, snowballs2, ducksLeft1, ducksLeft2, movesSoFar1, movesSoFar2)

            #If move is duck then change duckC1 (boolean)
            if curMove1 == "DUCK":
                #If player 1 is trying to use ducks when they have none then player 2 wins (also stops the game)
                if ducksLeft1 == 0:
                    raise Warning("Player 1 is trying to use ducks when they have no ducks left (Error in function), therefore player 2 wins!")
                duckC1 = True

            #If move is reload then change reloadC1 (boolean)
            elif curMove1 == "RELOAD":
                reloadC1 = True

            #If move is throw then change throwC1 (boolean)
            elif curMove1 == "THROW":
                #If player 1 is trying to use snowballs when they have none then player 2 wins (also stops the game)
                if snowballs1 == 0:
                    raise Warning("Player 1 is trying to use snowballs when they have no snowballs left (Error in function), therefore player 2 wins!")
                throwC1 = True
            else: #If any other move then return error
                raise Warning("Player 1 has tried to do an invalid move therefore player 2 wins!")
        else:
            myPlayerNumber = 2

            #Ask player for move and assign it to a variable
            curMove2 = strat2.getMove(myPlayerNumber, score1, score2, snowballs1, snowballs2, ducksLeft1, ducksLeft2, movesSoFar1, movesSoFar2)
            #print("Player " + str(myPlayerNumber) + "'s turn")
            #print("Chosen move: " + str(curMove2))

            #If move is duck then change duckC2 (boolean) and decrease player amount of ducks left by 1
            if curMove2 == "DUCK":
                #If player 2 is trying to use ducks when they have none then player 1 wins (also stops the game)
                if ducksLeft2 == 0:
                    raise Warning("Player 2 is trying to use ducks when they have no ducks left (Error in function), therefore player 1 wins!")
                duckC2 = True
                ducksLeft2 -= 1
                
            #If move is reload then change reloadC2 (boolean) and increase player snowballs by 1
            elif curMove2 == "RELOAD":
                snowballs2 += 1
                reloadC2 = True
                
            #If move is throw then change throwC2 (boolean) and reduce player snowballs by 1
            elif curMove2 == "THROW":
                #If player 2 is trying to use snowballs when they have none then player 1 wins (also stops the game)
                if snowballs2 == 0:
                    raise Warning("Player 2 is trying to use snowballs when they have no snowballs left (Error in function), therefore player 1 wins!")
                throwC2 = True
                snowballs2 -= 1
            else: #If any other move then return error
                raise Warning("Player 2 has tried to do an invalid move therefore player 1 wins!")
            
            #Adjust snowballs1 and ducksLeft1 (done later so player 2 doesn't know)
            if throwC1:
                snowballs1 -= 1
            if reloadC1:
                snowballs1 += 1
            if duckC1:
                ducksLeft1 -= 1

            #If no one threw then no one got hit
            if not throwC1 and not throwC2:
                pass

            #If any person reloaded that means they got hit (since the other person has thrown as we didn't pass the above if-statement)
            #Also adjusts the scores for the player that scored the hit
            elif reloadC1 or reloadC2:
                if reloadC1:
                    score2 += 1
                else:
                    score1 += 1


    #Find out who won and print it to the screen         
    if score1 == 3:
        return 1
    else:
        return 2

#Initialize amount of games won 
wonGames1 = 0
wonGames2 = 0
n = 10000

#Test the strategies n times
for i in range(0, n):
    #Call game function and assign what is returned to "result" variable
    result = game()
    
    #Adjust amount of games won depending on result of game
    if result == 1:
        wonGames1 += 1
    else:
        wonGames2 += 1
        
#Print out how many games each player won
print("Player 1 (" + strat1Name + ") won", wonGames1)
print("Player 2 (" + strat2Name + ") won", wonGames2)
