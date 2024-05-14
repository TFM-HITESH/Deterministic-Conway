from Cell import Cell
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import statistics

X_DIM = 60
Y_DIM = 60
ALIVE_CELL = Cell(1)
DEAD_CELL = Cell(0)

PROBABILITY_LIVING=[0.99, 0.95, 0.95, 0.95, 0.9, 0.9, 0.85, 0.85, 0.85]

GOL_LIST = []
ALIVE_COUNT_LIST = []

N = 38

X_VALS = []
C_VALS = []
CYCLES = 1000

def main():
    for i in range(CYCLES):
        fullCycle()

    slopeMean = round(statistics.mean(X_VALS),4)
    interceptMean = round(statistics.mean(C_VALS),4)
    slopeVariance = round(statistics.variance(X_VALS,4))
    interceptVariance = round(statistics.variance(C_VALS,4))
    slopeSD = round(statistics.stdev(X_VALS,4))
    interceptSD = round(statistics.stdev(C_VALS,4))

    cor = statistics.correlation(X_VALS,C_VALS)

    print("========================================")
    print("Mean of slopes =", slopeMean)
    print("Mean of intercepts =", interceptMean)
    print("Variance of slopes =", slopeVariance)
    print("Variance of intercepts =", interceptVariance)
    print("Standard Deviation of slopes =", slopeSD)
    print("Standard Deviation of intercepts =", interceptSD)
    print("Correlation between m and c values =", cor)

    fig, (pl1, pl2) = plt.subplots(2,1)
    fig.suptitle('Values of slope and intercept of population regression over 1000 Cycles')
    fig.supxlabel("Number of Trials")
    

    pl1.plot(range(0,CYCLES), X_VALS, marker='o', linestyle='', markersize=8, color='deeppink', label='Scatter Plot' )
    # thetaX = np.polyfit(range(0,CYCLES), X_VALS, 1)
    yLineX = [slopeMean] * len(X_VALS)
    # print("y = ", round(thetaX[0],4), "* x +", round(thetaX[1],4))
    pl1.set_title("Values of Slope(m) for regression obtained over the results from PCAECGOL")
    pl1.set_ylabel("Value of Slope for PCAECGOL Population")
    pl1.plot(range(0,CYCLES), yLineX, 'darkorchid')
    pl1.legend(['Slope value for nth trial', 'Mean'])
    # slopeText = "Mean of slopes = " + str(slopeMean)
    # pl1.text(0.9, 0.1, slopeText, horizontalalignment='center', verticalalignment='center', transform=pl1.transAxes)

    pl2.plot(range(0,CYCLES), C_VALS, marker='o', linestyle='', markersize=8, color='orange', label='Scatter Plot' )
    # thetaC = np.polyfit(range(0,CYCLES), C_VALS, 1)
    yLineC = [interceptMean] * len(X_VALS)
    # print("y = ", round(thetaC[0],4), "* x +", round(thetaC[1],4))
    pl2.set_title("Values of Intercept(c) for regression obtained over the results from PCAEGOL")
    pl2.set_ylabel("Value of Intercept for PCAECGOL Population")
    pl2.plot(range(0,CYCLES), yLineC, 'r')
    pl2.legend(['Intercept value for nth trial', 'Mean'])
    # interceptText = "Mean of intercepts = " + str(interceptMean)
    # pl2.text(0.9, 0.1, interceptText, horizontalalignment='center', verticalalignment='center', transform=pl2.transAxes)

    plt.show()

def get_pl():
    return PROBABILITY_LIVING

def fullCycle():
    print("Start Position : ")
    cellGrid = generateGrid(xDim=X_DIM, yDim=Y_DIM, choice=-1)
    printGrid(cellGrid)
    
    print("User updated positions : ")
    printGrid(cellGrid)

    # Preparing the grid and giving info about number of neighbours
    updateGridNeighbours(cellGrid=cellGrid)
    print("The grid is now prepared and we are ready to start the Game of life !")

    print(aliveNumber(cellGrid))

    for i in range(N):
        # time.sleep(0.05)
        print("Cycle Number = ", i+1)
        cellGrid = singleCycle(cellGrid=cellGrid)
        GOL_LIST.append(cellGrid)
        printGrid(GOL_LIST[i])
        ALIVE_COUNT_LIST.append(aliveNumber(GOL_LIST[i]))
        print("Number of alive cells in this generation = ", aliveNumber(cellGrid=cellGrid))

    # Finally draw the graph of population over time
    drawGraph(N)
        
def generateGrid(xDim, yDim, choice):
    # The final grid of cells
    cellGrid = []

    for row in range(yDim):
        cellRow = []
        for col in range(xDim):
            if choice == 0:
                cell = DEAD_CELL
            elif choice == 1:
                cell = ALIVE_CELL
            else:
                cell = Cell(random.choice([0,1]))
            cellRow.append(cell)
        cellGrid.append(cellRow)

    return cellGrid

# Shows the current state of the grid
def printGrid(cellGrid):
    for cellRow in cellGrid:
        for cell in cellRow:
            # Invoked cell printer
            cell.printCell()
        print()

def singleCycle(cellGrid):
    updateGrid(cellGrid=cellGrid)
    updateGridNeighbours(cellGrid=cellGrid)
    return cellGrid

def generateGridStart(cellGrid, startGrid):
    for row in range(len(cellGrid)):
        for col in range(len(cellGrid[row])):
            cellGrid[row][col].isAlive = startGrid[row][col]

def updateGrid(cellGrid):
    for row in range(1, len(cellGrid)-1):
        for col in range(1, len(cellGrid[row])-1):
            cellGrid[row][col].updateAlive(get_pl())

def updateGridNeighbours(cellGrid):
    pl = get_pl()  # Get the probability list
    for row in range(len(cellGrid)):
        for col in range(len(cellGrid[row])):
            # Calculate row and column indices for neighbors
            top_row = row - 1
            bottom_row = row + 1
            left_col = col - 1
            right_col = col + 1

            # Check boundaries to handle edge cases
            if top_row < 0:
                top_row = 0
            if bottom_row >= len(cellGrid):
                bottom_row = len(cellGrid) - 1
            if left_col < 0:
                left_col = 0
            if right_col >= len(cellGrid[row]):
                right_col = len(cellGrid[row]) - 1

            # Get neighbors
            topNeighbour = cellGrid[top_row][col]
            bottomNeighbour = cellGrid[bottom_row][col]
            leftNeighbour = cellGrid[row][left_col]
            rightNeighbour = cellGrid[row][right_col]
            topLeftNeighbour = cellGrid[top_row][left_col]
            topRightNeighbour = cellGrid[top_row][right_col]
            bottomLeftNeighbour = cellGrid[bottom_row][left_col]
            bottomRightNeighbour = cellGrid[bottom_row][right_col]

            # Updating the neighbors
            cellGrid[row][col].updateNeighbours(topNeighbour, bottomNeighbour, leftNeighbour, rightNeighbour,topLeftNeighbour, topRightNeighbour, bottomLeftNeighbour,bottomRightNeighbour, pl)
            
def aliveNumber(cellGrid):
    aliveCount = 0
    for row in range(len(cellGrid)):
        for col in range(len(cellGrid[row])):
            if(cellGrid[row][col].isAlive == 1):
                aliveCount +=1 
    
    return aliveCount

def drawGraph(n):
    # Line of best fit
    theta = np.polyfit(range(0,n), ALIVE_COUNT_LIST, 1)

    X_VALS.append(theta[0])
    C_VALS.append(theta[1])

    ALIVE_COUNT_LIST.clear()
    GOL_LIST.clear()

    print("y = ", round(theta[0],4), "* x +", round(theta[1],4))

if __name__ == "__main__":
    main()

