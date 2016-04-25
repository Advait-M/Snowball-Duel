import random
#def getMove(roundNum, playerNum, score1, score2, snowballs1, snowballs2, ducksLeft1, ducksLeft2):
def getMove(myPlayerNumber, score1, score2, snowballs1, snowballs2, ducksLeft1, ducksLeft2, movesSoFar1, movesSoFar2):
   if myPlayerNumber == 1:
      if snowballs1 > 0:
         if ducksLeft1 > 0:
            #If you have both ducks and snowballs left then randomly choose from all 3 options
            return random.choice(["THROW", "DUCK", "RELOAD"])
         else:
            #If you don't have ducks left randomly choose from the other options
            return random.choice(["THROW", "RELOAD"])
      else:
         if ducksLeft1 > 0:
            #If you don't have snowballs left randomly choose from the other options
            return random.choice(["DUCK", "RELOAD"])
         else:
            #If you don't have ducks or snowballs left then reload
            return "RELOAD"
   else:
      #Same strategy as above except the variable names are different
      #This is due to being player 2
      if snowballs2 > 0:
         if ducksLeft2 > 0:
            return random.choice(["THROW", "DUCK", "RELOAD"])
         else:
            return random.choice(["THROW", "RELOAD"])
      else:
         if ducksLeft2 > 0: 
            return random.choice(["DUCK", "RELOAD"])
         else:
            return "RELOAD"
