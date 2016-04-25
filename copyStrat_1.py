def getMove(myPlayerNumber, score1, score2, snowballs1, snowballs2, ducksLeft1, ducksLeft2, movesSoFar1, movesSoFar2):
    if myPlayerNumber == 1:
        #Try to get opponent's last move, if its the first round then DUCK
        try: 
            lastMove = movesSoFar2[-1]
        except IndexError:
            return "DUCK"
        #Do last move opponent did if it is legal
        #If it is not legal then RELOAD
        if lastMove == "RELOAD":
            return lastMove
        elif lastMove == "DUCK":
            if ducksLeft1 > 0:
                return "DUCK"
            else:
                return "RELOAD"
        else:
            if snowballs1 > 0:
                return "THROW"
            else:
                return "RELOAD"
    if myPlayerNumber == 2:
        #Same stategy as above except variable names are different (playing as player 2 now)
        try: 
            lastMove = movesSoFar1[-1]
        except IndexError:
            return "DUCK"
        if lastMove == "RELOAD":
            return lastMove
        elif lastMove == "DUCK":
            if ducksLeft2 > 0:
                return "DUCK"
            else:
                return "RELOAD"
        else:
            if snowballs2 > 0:
                return "THROW"
            else:
                return "RELOAD"
