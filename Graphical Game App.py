#####################################
#                                   #
#    SNOWBALL FIGHT GAME PLAYER     #
#   By: Advait, Amy, Dennis, Lina   #
#   Last updated: 11 December, 2015 #
#####################################

#Imports (that are constant)
import time
from tkinter import *
from random import *
import Tree
import random
import math
import winsound

###### EDITABLE VARIABLES (MAIN GAME RUNNER) ######
s = 1 #Player animation speed (reduce to have it go faster)
snowballSpeed = 0.001 #Snowball speed (quite slow at school - reduce this speed or make it 0)
particlesSpeed = 0.02 #Particles speed (reduce to have it go faster)
snowFlakes = 1000 #Snow flakes in background
cloudNum = 40 #Clouds in the background
frameCount = 10 #Amount of frames explosion runs for
pauseBetweenMoves = False #Whether there should be a pause between player 1's move and player 2's move
maxRounds = 200 #Max amount of round after which it raises an error (declared a draw)

#Assign strategy names to variables
strat1Name = "recognitionStrat2" #Change to desired program name (.py is not needed). Must be in same directory. 
strat2Name = "AdStrat1" #Change to desired program name (.py is not needed). Must be in same directory. 

####### FIREWORKS (WINNING ANIMATION) EDITABLE VARIABLES ######
numFireworks = 35 #Number of fireworks
minXV = 15 #Minimum horizontal velocity for fireworks
maxXV = 25 #Maximum horizontal velocity for fireworks
minYV = 75 #Minimum vertical velocity for fireworks
maxYV = 110 #Maximum vertical velocity for fireworks
minR = 5 #Minimum radius for fireworks
maxR = 15 #Maximum radius for fireworks

###### MAIN PROGRAM ######

#Import the two strategies
strat1 = __import__(strat1Name)
strat2 = __import__(strat2Name)

#Initialize tkinter graphics
tk = Tk()
screen = Canvas(tk, width=1000,height=800, background="#b3e6ff")
screen.pack()

#Import player images
#Player 1 images
p1Img = PhotoImage(file = "p1-1.gif")
p1duck = PhotoImage(file = "p1-2.gif")
p1load = PhotoImage(file = "p1-3.gif")
p1throw = [PhotoImage(file = "p1-4.gif"), PhotoImage(file = "p1-5.gif"), PhotoImage(file = "p1-6.gif")]

#Player 2 images
p2Img = PhotoImage(file = "p2-1.gif")
p2duck = PhotoImage(file = "p2-2.gif")
p2load = PhotoImage(file = "p2-3.gif")
p2throw = [PhotoImage(file = "p2-4.gif"), PhotoImage(file = "p2-5.gif"), PhotoImage(file = "p2-6.gif")]

def snowBackground():
    """Make the background filled with snow flakes"""
    for e in range(0, snowFlakes):
        r = randint(1, 5)
        x = randint(0, 1000)
        y = randint(0, 800)
        screen.create_oval(x-r, y-r, x+r, y+r, fill = "white", outline = "white")


def drawPlayer():
    """Draw the regular player stance and text information above each player"""
    global p1, p2
    p1Text = screen.create_text(200, 500, font = "Helvetica 20 bold", text="Player 1", fill = "#33bcff")
    p1Strat = screen.create_text(200, 525, font = "Helvetica 15 bold", text="(" + strat1Name + ")", fill = "#33bcff")
    p2Text = screen.create_text(800, 500, font = "Helvetica 20 bold", text="Player 2", fill = "#33bcff")
    p2Strat = screen.create_text(800, 525, font = "Helvetica 15 bold", text="(" + strat2Name + ")", fill = "#33bcff")
    p1 = screen.create_image(200,650, image = p1Img)
    p2 = screen.create_image(800,650, image = p2Img)

def bothThrow():
    """Animates both players throwing and the snowballs colliding in the air"""
    global p1Draw, p2Draw
    #Initialize arrays
    xP = []
    yP = []
    particles = []
    angles = []
    xSizes = []
    ySizes = []
    r = []
    rSpeeds = []
    counter = []
    
    #Fill particle arrays
    for particleNum in range(0, 100):
        xP.append(0)
        yP.append(0)
        dAngle = random.randint(1, 360)
        rAngle = math.radians(dAngle)
        angles.append(rAngle)
        r.append(random.randint(-15, 15))
        xSizes.append(random.randint(3, 7))
        ySizes.append(random.randint(3, 7))
        rSpeeds.append(random.randint(-15, 15))
        while rSpeeds[particleNum] == 0:
            rSpeeds[particleNum] = random.randint(-15, 15)
        particles.append(0)
        
    #Animate the three positions of the players throwing 
    for i in range(0,3):
        p1Draw = screen.create_image(200,650, image = p1throw[i])
        p2Draw = screen.create_image(800,650, image = p2throw[i])
        screen.update()
        time.sleep(s/4)
        if i < 2:
            screen.delete(p1Draw, p2Draw)
            screen.delete(p1, p2)
            
    #Initialize variables
    #Uses velocity formulas to create a parabolic trajectory
    x = 200
    y = 650
    vix = 70
    viy = 50
    ft = -2 * viy/-9.8
    fx = vix * ft + 200
    x2 = 800
    y2 = 650
    vix2 = -70
    viy2 = 50
    ft2 = -2 * viy2/-9.8
    fx2 = 800 - vix2 * ft2
    
    #Animates the snowballs' trajectory
    for i in range(0, int(fx) + 1):
        #Snowball from player 1
        if x <= 500:
            t = ft/fx * i
            x = vix * t + 200
            y = -1*(viy * t + 0.5*-9.8*t**2) + 650
            snowball = screen.create_oval(x-10, y-10, x+10, y+10, fill = "white", outline = "black")
        #Snowball from player 2
        if x2 >= 500:
            t2 = ft2/fx2 * i
            x2 = vix2 * t + 800
            y2 = -1*(viy2 * t2 + 0.5*-9.8*t2**2) + 650
            snowball2 = screen.create_oval(x2-10, y2-10, x2+10, y2+10, fill = "white", outline = "black")
        else:
            break
        #Update screen, sleep for some time, and delete particles 
        screen.update()
        time.sleep(snowballSpeed)
        screen.delete(snowball, snowball2)
        
    for f in range(0, frameCount):
        for q in range(0, 100):
            #Calculate x and y values of each particle
            xP[q] = 500 + r[q] * math.cos(angles[q])
            yP[q] = 550 - r[q] * math.sin(angles[q])
            r[q] = r[q] + rSpeeds[q]
            
            #Create a rectangle or oval representing the particle
            if q % 2 == 0:
                particles[q] = screen.create_oval(xP[q], yP[q], xP[q] + xSizes[q], yP[q] + ySizes[q], fill = "white", outline = "black")
            else:
                particles[q] = screen.create_rectangle(xP[q], yP[q], xP[q] + xSizes[q], yP[q] + ySizes[q], fill = "white", outline = "black")
        #Update screen and sleep for some time
        screen.update()
        time.sleep(particlesSpeed)
        #Delete particles using a for loop
        for q in range(0, 100):
            screen.delete(particles[q])
        
def drawPlayer1(move):
    """Draw player 1 based on move"""
    #Make sure default image for the player is deleted
    screen.delete(p1)
    global p1Draw
    #Choose image to display depending on move
    if move == "DUCK":
        p1Draw = screen.create_image(200,650, image = p1duck)
    elif move == "RELOAD":
        p1Draw = screen.create_image(200,650, image = p1load)
    else:
        #Animate player by looping through three images
        for i in range(0,3):
            p1Draw = screen.create_image(200,650, image = p1throw[i])
            screen.update()
            time.sleep(s/4)
            if i < 2:
                screen.delete(p1Draw)
        #Call the function to animate throwing snowballs
        snowBallThrow(1, curMove1, curMove2)

def drawPlayer2(move):
    """Draw player 2 based on move"""
    #Make sure default image for the player is deleted
    screen.delete(p2)
    global p2Draw
    #Choose image to display depending on move
    if move == "DUCK":
        p2Draw = screen.create_image(800,650, image = p2duck)
    elif move == "RELOAD":
        p2Draw = screen.create_image(800,650, image = p2load)
    else:
        #Animate player by looping through three images
        for i in range(0,3):
            p2Draw = screen.create_image(800,650, image = p2throw[i])
            screen.update()
            time.sleep(s/4)
            if i < 2:
                screen.delete(p2Draw)
        #Call the function to animate throwing snowballs
        snowBallThrow(2, curMove1, curMove2)

def background():
    """Creates the general background scenery"""
    #Creates random clouds in the sky
    for r in range(0,cloudNum):
        #Initialize variables
        x = randint(-100,1200)
        y = randint(-20,100)
        width = randint(60,90)
        height = randint(20,50)
        cloudColor = choice(["gray92","gray95","gray98"])
        
        #Create lots of ovals to represent clouds
        for i in range(0,20):
            x1 = x - randint(1, width)
            y1 = y - randint(1, height)
            x2 = x + randint(1, width)
            y2 = y + randint(1, height)
            oval = screen.create_oval(x1, y1, x2, y2, fill=cloudColor, outline=cloudColor)
        
    #Ground behind the trees
    screen.create_oval(-100,320,1100,600, fill ="gainsboro", outline ="gainsboro")

    #Trees from Tree.py
    Tree.tree(screen)
    
    #Snowy Ground
    screen.create_rectangle (0,500,1000,800,fill="snow",outline="snow")
    screen.create_polygon (0,500,50,500,100,450,250,470,400,430,500,450,650,420,700,450,800,460,1020,470,1000,600, fill="snow",outline="snow",smooth="true")

    #Scorebox
    screen.create_rectangle( 320,100,680,350, fill="#80d5ff", outline="white", width="8")


def snowBallThrow(playerNum, move1, move2):
    #Initialize variables
    y = 0
    x = 0

    #Check who is throwing
    if playerNum == 1:
        #Check opponent move
        if move2 == "RELOAD":
            #Since opponent is reloading, have a lower initial y velocity
            #Initialize variables 
            vix = 70
            viy = 40
            xP = []
            yP = []
            particles = []
            angles = []
            xSizes = []
            ySizes = []
            r = []
            rSpeeds = []
            counter = []
            
            #Fill particle arrays
            for particleNum in range(0, 100):
                xP.append(0)
                yP.append(0)
                dAngle = random.randint(1, 360)
                rAngle = math.radians(dAngle)
                angles.append(rAngle)
                r.append(random.randint(-15, 15))
                xSizes.append(random.randint(3, 7))
                ySizes.append(random.randint(3, 7))
                rSpeeds.append(random.randint(-15, 15))
                while rSpeeds[particleNum] == 0:
                    rSpeeds[particleNum] = random.randint(-15, 15)
                particles.append(0)
        else:
            #If other person is ducking or throwing have these initial velocities
            vix = 70
            viy = 50
        #Use velocity formulas to calculate information
        ft = -2 * viy/-9.8
        drawPlayer2(curMove2) #Make sure player 2 is drawn 
        fx = vix * ft + 200
        #Animate snowball throwing
        for i in range(0, int(fx) + 1):
            #Check opponent move
            if move2 == "RELOAD":
                #Animate until hitting person
                if x <= 1020:
                    #Update current time in terms of parabola and calculate x/y
                    t = ft/fx * i
                    x = vix * t + 200
                    y = -1*(viy * t + 0.5*-9.8*t**2) + 650
                    #Create snowball
                    snowball = screen.create_oval(x-10, y-10, x+10, y+10, fill = "white", outline = "black")
                    #Update, sleep, delete
                    screen.update()
                    time.sleep(snowballSpeed)
                    screen.delete(snowball)
                
            if move2 == "DUCK":
                #Animate until off the screen
                if x <= 1010:
                    #Use velocity formulas and animate snowball 
                    t = ft/fx * i
                    x = vix * t + 200
                    y = -1*(viy * t + 0.5*-9.8*t**2) + 650
                    snowball = screen.create_oval(x-10, y-10, x+10, y+10, fill = "white", outline = "black")
                    screen.update()
                    time.sleep(snowballSpeed)
                    screen.delete(snowball)
        if move2 == "RELOAD":
            #Make explosion of snowball
            for f in range(0, frameCount): #Frames explosion runs for 
                for q in range(0, 100):
                    #Calculate x and y values of each particle
                    xP[q] = 775 + r[q] * math.cos(angles[q])
                    yP[q] = 650 - r[q] * math.sin(angles[q])
                    r[q] = r[q] + rSpeeds[q]
                    
                    #Create a rectangle or oval representing the particle
                    if q % 2 == 0:
                        particles[q] = screen.create_oval(xP[q], yP[q], xP[q] + xSizes[q], yP[q] + ySizes[q], fill = "white", outline = "black")
                    else:
                        particles[q] = screen.create_rectangle(xP[q], yP[q], xP[q] + xSizes[q], yP[q] + ySizes[q], fill = "white", outline = "black")
                #Update, sleep, delete    
                screen.update()
                time.sleep(particlesSpeed)
                for q in range(0, 100):
                    screen.delete(particles[q])
    else:
        #Similar procedure as above except the offset is different and now it is throwing for player 2 (player 1 is the enemy)
        #Also, initial x velocity is negative since snowball is going the other way
        if move1 == "RELOAD":
            vix = -70
            viy = 40
            xP = []
            yP = []
            particles = []
            angles = []
            xSizes = []
            ySizes = []
            r = []
            rSpeeds = []
            counter = []
            for particleNum in range(0, 100):
                xP.append(0)
                yP.append(0)
                dAngle = random.randint(1, 360)
                rAngle = math.radians(dAngle)
                angles.append(rAngle)
                r.append(random.randint(-15, 15))
                xSizes.append(random.randint(3, 7))
                ySizes.append(random.randint(3, 7))
                rSpeeds.append(random.randint(-15, 15))
                while rSpeeds[particleNum] == 0:
                    rSpeeds[particleNum] = random.randint(-15, 15)
                particles.append(0)
        else:
            vix = -70
            viy = 50
        ft = -2 * viy/-9.8
        drawPlayer1(curMove1)
        fx = 800 - vix*ft
        for i in range(0, int(fx) + 1):
            if move1 == "RELOAD":
                if x >= -20:
                    t = ft/fx * i
                    x = vix * t + 800
                    y = -1*(viy * t + 0.5*-9.8*t**2) + 650
                    snowball = screen.create_oval(x-10, y-10, x+10, y+10, fill = "white", outline = "black")
                    screen.update()
                    time.sleep(snowballSpeed)
                    screen.delete(snowball)
            
            if move1 == "DUCK":
                if x >= -10:
                    t = ft/fx * i
                    x = vix * t + 800
                    y = -1*(viy * t + 0.5*-9.8*t**2) + 650
                    snowball = screen.create_oval(x-10, y-10, x+10, y+10, fill = "white", outline = "black")
                    screen.update()
                    time.sleep(snowballSpeed)
                    screen.delete(snowball)
        if move1 == "RELOAD":
            for f in range(0, frameCount):
                for q in range(0, 100):
                    #Calculate x and y values of each particle
                    xP[q] = 250 + r[q] * math.cos(angles[q])
                    yP[q] = 650 - r[q] * math.sin(angles[q])
                    r[q] = r[q] + rSpeeds[q]
                    
                    #Create a rectangle or oval representing the particle
                    if q % 2 == 0:
                        particles[q] = screen.create_oval(xP[q], yP[q], xP[q] + xSizes[q], yP[q] + ySizes[q], fill = "white", outline = "black")
                    else:
                        particles[q] = screen.create_rectangle(xP[q], yP[q], xP[q] + xSizes[q], yP[q] + ySizes[q], fill = "white", outline = "black")
                    
                screen.update()
                time.sleep(particlesSpeed)
                for q in range(0, 100):
                    screen.delete(particles[q])
                
                
def gameApp():
    global curMove1, curMove2
    
    #Add snowflakes to the background
    snowBackground()
    
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

    #Draw starting graphics
    background()
    drawPlayer()
    
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
                
            #Draw statistics to screen
            roundNumber = screen.create_text(500,150,font="Helvetica 48 bold",text="Round " + str(roundNum), fill = "white")
            scoreDraw = screen.create_text(500,205,font="Helvetica 24",text="Score: " + str(score1) + " : " + str(score2), fill = "white")
            snowballNumDraw = screen.create_text(500,250,font="Helvetica 24", text="Snowballs: " + str(snowballs1) + " : " + str(snowballs2), fill = "white")
            ducksNumDraw = screen.create_text(500,300,font="Helvetica 24",text="Ducks left: " + str(ducksLeft1) + " : " + str(ducksLeft2), fill = "white")

            #Update, sleep
            screen.update()
            time.sleep(s)

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


            #GRAPHICS
                
            #Draw players based on move (If any one player is throwing then players will be draw later)
            if curMove1 == "DUCK":
                if curMove2 != "THROW":
                    drawPlayer1("DUCK")
            elif curMove1 == "RELOAD":
                if curMove2 != "THROW":
                    drawPlayer1("RELOAD")
            else:
                if curMove2 != "THROW":
                    drawPlayer1("THROW")
                    
            #If user wants a pause between the two moves of the players then insert it        
            if pauseBetweenMoves:
                screen.update()
                time.sleep(s/2)
                
            #Draw players based on move (If any one player is throwing then players will be draw later)
            if curMove2 == "DUCK":
                if curMove1 != "THROW":
                    drawPlayer2("DUCK")
            elif curMove2 == "RELOAD":
                if curMove1 != "THROW":
                    drawPlayer2("RELOAD")
            else:
                if curMove1 != "THROW":
                    drawPlayer2("THROW")
                    
            #If both players are throwing then call bothThrow() which handle this case
            if curMove1 == "THROW" and curMove2 == "THROW":
                bothThrow()

            #Update, sleep, delete
            screen.update()
            time.sleep(s/2)
            screen.delete(p1Draw, p2Draw)
            
            #Revert back to default player
            drawPlayer()
            
            #If no one threw then no one got hit
            if not throwC1 and not throwC2:
                summary = "No one got hit."

            #If any person reloaded that means they got hit (since the other person has thrown as we didn't pass the above if-statement)
            #Also adjusts the scores for the player that scored the hit
            elif reloadC1 or reloadC2:
                if reloadC1:
                    summary = "Player 1 got hit!"
                    score2 += 1
                else:
                    summary = "Player 2 got hit!"
                    score1 += 1

            #If both people threw then snowballs collide and no one gets hit        
            elif throwC1 and throwC2:
                summary = "Snowballs collide in the air."

            #If none of the above happened then one of the players missed
            #Saves who missed their snowball
            else:
                if throwC1:
                    summary = "Player 1 missed!"
                elif throwC2:
                    summary = "Player 2 missed!"

            #Draw Summary Text
            summaryText = screen.create_text(500,750, font = "Helvetica 18 bold", text=summary, fill = "#33bcff")

            #Update, sleep, delete
            screen.update()
            time.sleep(s*2)
            screen.delete(roundNumber, scoreDraw, snowballNumDraw, ducksNumDraw, summaryText)

            #Raise warning if going into infinite loop
            if roundNum > maxRounds:
                raise Warning("Going into infinite loop! It is a draw!")
            
    #Find the winner and draw on the screen     
    if score1 == 3:
        screen.create_text(500,180, font = "Helvetica 48 bold", text = "Player 1", fill = "white")
        screen.create_text(500,240, font = "Helvetica 18", text = "(" + strat1Name + ")", fill = "white")
        screen.create_text(500,280, font = "Helvetica 24", text = "Won the snowball fight!", fill = "white")
    else:
        screen.create_text(500,180, font = "Helvetica 48 bold", text = "Player 2", fill = "white")
        screen.create_text(500,240, font = "Helvetica 18", text = "(" + strat2Name + ")", fill = "white")
        screen.create_text(500,280, font = "Helvetica 24", text = "Won the snowball fight!", fill = "white")
        
#Call the main procedure to start the game
gameApp()

########## FIREWORKS WINNNING ANIMATION ##########

# IMPORT SOUND AND PICTURE FILES
fireworksSound = "Firework sound.wav"
crowdSound = "Crowd sound.wav"

# MAKE GRID OVERLAY (only enable if developing)
gridOverlay = False
if gridOverlay:
    spacing = 50
    for x in range(0, 800, spacing): 
        screen.create_line(x, 10, x, 800, fill="black")
        screen.create_text(x, 0, text=str(x), font="Times 8", anchor = N)

    for y in range(0, 800, spacing):
        screen.create_line(20, y, 800, y, fill="black")
        screen.create_text(4, y, text=str(y), font="Times 8", anchor = W)


# HEXADECIMAL FUNCTION - creates a random string that is a hexadecimal value 
def hexadecimal():
    hexadecimals = "#"
    for i in range(0, 6):
        a = random.randint(48, 70)
        while 58 <= a <= 64:
            a = random.randint(48,70)
        hexadecimals += chr(a)
    return hexadecimals

# RUNS ANIMATION ONCE (BREAKS AFTER ONE RUN)
while True:
    #Initialize variables related to fireworks
    counterA = False
    counterB = False
    counterEnd = [] 
    xStart = []
    yStart = []
    x = []
    y = []
    vix = []
    viy = []
    firework = []
    fireworkColours = []
    particlesAmount = []
    ft = []
    finalX = []
    m = []
    radii = []
    endNow = False

    #Initialize variables related to the particles
    xP = []
    yP = []
    particles = []
    angles = []
    xSizes = []
    ySizes = []
    r = []
    rSpeeds = []
    counter = []
    fCur = []
    stayInSkyFrames = []
        
    #Fill the firework variables
    for fireworkNum in range(0, numFireworks):
        counterEnd.append(True)
        radii.append(random.randint(minR, maxR))
        finalX.append(0)
        firework.append(0)
        m.append(0)
        ft.append(0)
        x.append(0)
        y.append(0)
        xStart.append(random.randint(100, 700))
        yStart.append(random.randint(600, 700))
        vix.append(random.randint(minXV, maxXV))
        viy.append(random.randint(minYV, maxYV))
        fireworkColours.append(hexadecimal())
        
        #Fill the particle variables
        #(Use temporary lists that will be appended onto the main list later in order to have nested lists)
        rTemp = []
        xSizesTemp = []
        ySizesTemp = []
        rSpeedsTemp = []
        particlesTemp = []
        anglesTemp = []
        xPTemp = []
        yPTemp = []
        counter.append(True)
        fCur.append(0)
        stayInSkyFrames.append(radii[fireworkNum] * 3)

        #Loop through number of particles and fill temporary lists (number of particles depends of size of firework - radius * 10)
        #Speed of particles depends on size of firework (randint between negative and postive value of radius since bigger fireworks have faster particles
        for particleNum in range(0, radii[fireworkNum] * 10):
            xPTemp.append(0)
            yPTemp.append(0)
            dAngle = random.randint(1, 360)
            rAngle = math.radians(dAngle)
            anglesTemp.append(rAngle)
            rTemp.append(random.randint(-15, 15))
            xSizesTemp.append(random.randint(3, 7))
            ySizesTemp.append(random.randint(3, 7))
            rSpeedsTemp.append(random.randint(-radii[fireworkNum], radii[fireworkNum]))
            while rSpeedsTemp[particleNum] == 0:
                rSpeedsTemp[particleNum] = random.randint(-15, 15)
            particlesTemp.append(0)

        #Append temporary lists to main lists
        r.append(rTemp)
        xSizes.append(xSizesTemp)
        ySizes.append(ySizesTemp)
        rSpeeds.append(rSpeedsTemp)
        particles.append(particlesTemp)
        angles.append(anglesTemp)
        xP.append(xPTemp)
        yP.append(yPTemp)

    #Play initial cheering sound
    winsound.PlaySound(crowdSound, winsound.SND_FILENAME| winsound.SND_ASYNC)     

    #Play animation for 500 frames
    for f in range(0, 500):
        #Play explosion and clapping sound after first explosion
        if counterA and counterB:
            counterB = False
            winsound.PlaySound(fireworksSound, winsound.SND_FILENAME| winsound.SND_ASYNC)

        #Animate fireworks
        for i in range(0, numFireworks):
            #Use velocity formulas to find x and y values of the fireworks
            ft[i] = -2 * viy[i] / -9.8
            finalX[i] = vix[i] * ft[i]
            m[i] += 1
            
            #If at the peak of the parabola (technically minimum since tkinter y values are upside down)
            #start explosions
            if m[i] >= finalX[i]/2:
                #Change counters (counters give info on whether a specific event has happened)
                if not counterA:
                    counterA = True
                    counterB = True
                if counter[i]:
                    fCur[i] = f
                    counter[i] = False

                #Animate particles
                for q in range(0, radii[i] * 10):
                    #Calculate x and y values of each particle
                    xP[i][q] = x[i] + r[i][q] * math.cos(angles[i][q])
                    yP[i][q] = y[i] - r[i][q] * math.sin(angles[i][q])
                    r[i][q] = r[i][q] + rSpeeds[i][q]
                    
                    #Create a rectangle or oval representing the particle
                    if q % 2 == 0 and f - fCur[i] < stayInSkyFrames[i]:
                        particles[i][q] = screen.create_oval(xP[i][q], yP[i][q], xP[i][q] + xSizes[i][q], yP[i][q] + ySizes[i][q], fill = fireworkColours[i])
                    elif f - fCur[i] < stayInSkyFrames[i]:
                        particles[i][q] = screen.create_rectangle(xP[i][q], yP[i][q], xP[i][q] + xSizes[i][q], yP[i][q] + ySizes[i][q], fill = fireworkColours[i])
                    else:
                        #counterEnd keeps track of if the firework has finished exploding
                        counterEnd[i] = False
            #If not at peak of parabola then animate fireworks
            else:
                #Calculate current time (in terms of the parabola)
                t = ft[i]/finalX[i] * m[i]
                #Either have the parabola go from left to right or right to left
                if i % 2 == 0:
                    x[i] = vix[i] * t + xStart[i]
                else:
                    x[i] = xStart[i] - vix[i] * t
                #Calculate y value (velocity formula)
                y[i] = -1*(viy[i] * t + 0.5*-9.8*t**2) + yStart[i]
                #Create firework
                firework[i] = screen.create_oval(x[i] - radii[i], y[i] - radii[i], x[i]+ radii[i], y[i]+radii[i], fill = fireworkColours[i])

        #Update screen and sleep (so user can watch animation)
        screen.update()
        time.sleep(0.02)
        
        #Delete fireworks (for animation effect)
        for d in range(0, numFireworks):
            screen.delete(firework[d])
            #Delete particles (for animation effect)
            for q in range(0, radii[d] * 10):
                screen.delete(particles[d][q])
        #Checks if animation is over
        for v in range(0, numFireworks):
            if counterEnd[v]:
                break
            if v == numFireworks-1:
                endNow = True
        #Breaks animation for loop
        if endNow:
            break
    #Breaks animation infinite loop
    if endNow:
        break

