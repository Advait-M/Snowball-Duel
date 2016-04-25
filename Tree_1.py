#Imports
from tkinter import *
from random import *

def tree(s):
    # Base triangle array
    numTri = []
    height = []
    deltaHeight = []
    treeBase1 = []
    treeBase2 = []
    xValue = []
    yValue = []
    colour = []

    numTrees = 15
    m1 = -50
    treeC = (["#29a329", "#1f7a1f", "#145214"])
    stumpC = (["#ac7339", "#86592d", "#604020"])
    
    # Tree
    for i in range(0, numTrees):
        # Base triangle calculations
        treeColour = treeC[i % len(treeC)]
        stumpColour = stumpC[i % len(stumpC)]
        # Number of triangles going up
        startNumTri = randint(4, 6)
        # Height of triangle in each tree
        startDeltaHeight = randint(75, 100)

        m2 = m1 + randint(0,50)
        # x1
        startXValue = randint(m1, m2)
        # y1
        startYValue = randint(250, 350)
        startBase = randint(100, 120)
        # x2
        startBase1 = startXValue + startBase 
        # y2
        startBase2 = startXValue - startBase 
        startHeight = startYValue + startDeltaHeight
        # translates the tree in the y-axis
        m1 = m1 + randint(100, 200)

        numTri.append(startNumTri)
        deltaHeight.append(startDeltaHeight)
        colour.append(treeColour)
        
        height.append(startHeight)
        xValue.append(startXValue)
        yValue.append(startYValue)
        treeBase1.append(startBase1)
        treeBase2.append(startBase2)

        # Stump calculations
        stumpWidth1 = xValue[i] - int(startBase/randint(3,4))
        stumpWidth2 = xValue[i] + int(startBase/randint(3,4))
        stumpHeight1 = yValue[i] + deltaHeight[i]
        stumpHeight2 = yValue[i] + deltaHeight[i] + randint(50, 75)

        # Limits stump to 440 pixels
        if stumpHeight2 >= 440:
            stumpHeight2 = 440
        # Actual creations of triangles and stumps
        for n in range(0, numTri[i]):
            # changes x2 and x3 to be close each time a triangle goes up
            x1 = xValue[i]
            y1 = yValue[i] - (deltaHeight[i] - 20) * n
            x2 = treeBase1[i] - (15*(n+1)) 
            x3 = treeBase2[i] + (15*(n+1))
            y2 = height[i] - (deltaHeight[i] - 20) * n
            b = s.create_rectangle(stumpWidth1, stumpHeight1, stumpWidth2, stumpHeight2, fill=stumpColour, outline=stumpColour)
            x = s.create_polygon(x1, y1, x2, y2, x3, y2, fill=colour[i])
