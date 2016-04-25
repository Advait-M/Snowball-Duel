from random import *
#def getMove(roundNum, playerNum, score1, score2, numSnowballs1, numSnowballs2, numDucks1, numDucks2):
def getMove(myPlayerNumber, score1, score2, snowballs1, snowballs2, ducksLeft1, ducksLeft2, movesSoFar1, movesSoFar2):
    #Find out who the player is
    if myPlayerNumber == 1:
        #Reload until enemy has a score of two
        if score2 != 2:
            return "RELOAD"
        if score2 == 2:
            #If both players have snowballs and you also have ducks then choose randomly between a safe move
            if ducksLeft1 != 0 and snowballs2 > 0 and snowballs1 != 0:
                return choice(["DUCK", "THROW"])
            #Else if it is possible to duck and the enemy has snowballs then duck
            elif ducksLeft1 != 0 and snowballs2 > 0:
                return "DUCK"
            #If you have no ducks, enemy has no snowballs and you have a snowball then throw
            if ducksLeft2 == 0 and snowballs2 == 0 and snowballs1 != 0:
                return "THROW"
            #Else if the enemy has no snowballs then reload
            elif snowballs2 == 0:
                return "RELOAD"
            else:
                #Throw if possible (always safe move)
                if snowballs1 > 0: 
                    return "THROW"
                else:
                    #If you can't throw then try to duck if the enemy has snowballs
                    if snowballs2 != 0 and ducksLeft1 != 0:
                        return "DUCK"
                    else:
                        #Else reload
                        return "RELOAD"
    else:
        #Similar to above except variable names are different (since it is for player 2)
        if score1 != 2:
            return "RELOAD"
        if score1 == 2:
            if ducksLeft2 != 0 and snowballs1 > 0 and snowballs2 != 0:
                return choice(["DUCK", "THROW"])
            elif ducksLeft2 != 0 and snowballs1 > 0:
                return "DUCK"    
            if ducksLeft1 == 0 and snowballs1 == 0 and snowballs2 != 0:
                return "THROW"
            elif snowballs1 == 0:
                return "RELOAD"
            else:
                if snowballs2 > 0: 
                    return "THROW"
                else:
                    if snowballs1 >= 1 and ducksLeft2 != 0:
                        return "DUCK"
                    else:
                        return "RELOAD"
