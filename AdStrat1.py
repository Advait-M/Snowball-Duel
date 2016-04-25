#def getMove(roundNum, playerNum, score1, score2, numSnowballs1, numSnowballs2, numDucks1, numDucks2):
def getMove(myPlayerNumber, score1, score2, snowballs1, snowballs2, ducksLeft1, ducksLeft2, movesSoFar1, movesSoFar2):
    roundNum = len(movesSoFar1) + 1
    if myPlayerNumber == 1:
        if score2 != 2:
            #Keep on reloading until enemy reaches score of 2
            return "RELOAD"
        if score2 == 2:
            #Initially duck 5 times (don't duck if enemy has 0 snowballs)
            if ducksLeft1 > 0 and snowballs2 > 0:
                return "DUCK"
            #If enemy has no snowballs then reload
            elif snowballs2 == 0:
                return "RELOAD"
            else:
                #If you have snowballs then throw
                if snowballs1 > 0: 
                    return "THROW"
                #Else, reload
                else:
                    return "RELOAD"
    else:
        #Same strategy as above except the variable names are different
        #This is due to being player 2
        if score1 != 2:
            return "RELOAD"
        if score1 == 2:
            if ducksLeft2 > 0 and snowballs1 > 0:
                return "DUCK"
            elif snowballs1 == 0:
                return "RELOAD"
            else:
                if snowballs2 > 0: 
                    return "THROW"
                else:
                    return "RELOAD"
