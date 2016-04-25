def getMove(myPlayerNumber, score1, score2, snowballs1, snowballs2, ducksLeft1, ducksLeft2, movesSoFar1, movesSoFar2):
    #Checks to see which player is playing (affects variable names)
    if myPlayerNumber:
        #Cycles through reload, throw and duck (if it can't do a move according to the pattern then it reloads)
        if len(movesSoFar1) % 6 == 0 or len(movesSoFar1) % 6 == 1:
            return "RELOAD"
        elif len(movesSoFar1) % 6 == 2 or len(movesSoFar1) % 6 == 3:
            if snowballs1 > 0:
                return "THROW"
            else:
                return "RELOAD"
        elif len(movesSoFar1) % 6 == 4 or len(movesSoFar1) % 6 == 5:
            if ducksLeft1 != 0:
                return "DUCK"
            else:
                return "RELOAD"
    else:
        #Same as above except variable names are different since its for player 2 now
        if len(movesSoFar1) % 6 == 0 or len(movesSoFar1) % 6 == 1:
            return "RELOAD"
        elif len(movesSoFar1) % 6 == 2 or len(movesSoFar1) % 6 == 3:
            if snowballs2 > 0:
                return "THROW"
            else:
                return "RELOAD"
        elif len(movesSoFar1) % 6 == 4 or len(movesSoFar1) % 6 == 5:
            if ducksLeft2 != 0:
                return "DUCK"
            else:
                return "RELOAD"
