from Cell import Cell
import random
import matplotlib.pyplot as plt
import numpy as np
import time
import statistics

X_DIM = 60
Y_DIM = 60
ALIVE_CELL = Cell(1)
DEAD_CELL = Cell(0)

GOL_LIST = []
ALIVE_COUNT_LIST = []

N = 38

X_VALS = []
C_VALS = []
CYCLES = 10

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
    fig.suptitle('Values of slope and intercept of population regression over 10000 Cycles')
    fig.supxlabel("Number of Trials")
    

    pl1.plot(range(0,CYCLES), X_VALS, marker='o', linestyle='', markersize=8, color='darkcyan', label='Scatter Plot' )
    # thetaX = np.polyfit(range(0,CYCLES), X_VALS, 1)
    yLineX = [slopeMean] * len(X_VALS)
    # print("y = ", round(thetaX[0],4), "* x +", round(thetaX[1],4))
    pl1.set_title("Values of Slope(m) for regression obtained over the results from CGOL")
    pl1.set_ylabel("Value of Slope for CGOL Population")
    pl1.plot(range(0,CYCLES), yLineX, 'b')
    pl1.legend(['Slope value for nth trial', 'Mean'])
    slopeText = "Mean of slopes = " + str(slopeMean)
    pl1.text(0.9, 0.1, slopeText, horizontalalignment='center', verticalalignment='center', transform=pl1.transAxes)

    pl2.plot(range(0,CYCLES), C_VALS, marker='o', linestyle='', markersize=8, color='orange', label='Scatter Plot' )
    # thetaC = np.polyfit(range(0,CYCLES), C_VALS, 1)
    yLineC = [interceptMean] * len(X_VALS)
    # print("y = ", round(thetaC[0],4), "* x +", round(thetaC[1],4))
    pl2.set_title("Values of Intercept(c) for regression obtained over the results from CGOL")
    pl2.set_ylabel("Value of Intercept for CGOL Population")
    pl2.plot(range(0,CYCLES), yLineC, 'r')
    pl2.legend(['Intercept value for nth trial', 'Mean'])
    interceptText = "Mean of intercepts = " + str(interceptMean)
    pl2.text(0.9, 0.1, interceptText, horizontalalignment='center', verticalalignment='center', transform=pl2.transAxes)

    plt.show()

def fullCycle():
    # Display start position
    print("Start Position:")
    cellGrid = generateGrid(xDim=X_DIM, yDim=Y_DIM, choice=-1)  # Random initial state
    printGrid(cellGrid)

    print("User updated positions:")
    printGrid(cellGrid)

    # Preparing the grid and giving info about number of neighbours
    updateGridNeighbours(cellGrid=cellGrid)
    print("The grid is now prepared and we are ready to start the Game of life !")

    print(aliveNumber(cellGrid))

    for i in range(N):
        time.sleep(0.05)
        print("Cycle Number = ", i+1)
        cellGrid = singleCycle(cellGrid=cellGrid)
        GOL_LIST.append(cellGrid)
        printGrid(GOL_LIST[i])
        ALIVE_COUNT_LIST.append(aliveNumber(GOL_LIST[i]))
        print("Number of alive cells in this generation = ", aliveNumber(cellGrid=cellGrid))

    # Finally draw the graph of population over time
    drawGraph(N)

def generateGrid(xDim, yDim, choice):
    """Generate the initial grid of cells."""
    cellGrid = []

    for row in range(yDim):
        cellRow = []
        for col in range(xDim):
            if choice == 0:
                cell = Cell(0)  # Dead cells
            elif choice == 1:
                cell = Cell(1)  # Alive cells
            else:
                cell = Cell(random.choice([0, 1]))  # Random state
            cellRow.append(cell)
        cellGrid.append(cellRow)

    return cellGrid

def printGrid(cellGrid):
    """Print the current state of the grid."""
    for cellRow in cellGrid:
        for cell in cellRow:
            cell.printCell()
        print()

def generateGridStart(cellGrid, startGrid):
    """Initialize the grid according to a custom start grid."""
    for row in range(len(cellGrid)):
        for col in range(len(cellGrid[row])):
            cellGrid[row][col].isAlive = startGrid[row][col]

def updateGridNeighbours(cellGrid):
    """Update the state of each cell's neighbors in the grid."""
    for row in range(len(cellGrid)):
        for col in range(len(cellGrid[row])):
            currentCell = cellGrid[row][col]

            # Determine the positions of neighbors
            topNeighbor = cellGrid[row - 1][col] if row > 0 else None
            bottomNeighbor = cellGrid[row + 1][col] if row < len(cellGrid) - 1 else None
            leftNeighbor = cellGrid[row][col - 1] if col > 0 else None
            rightNeighbor = cellGrid[row][col + 1] if col < len(cellGrid[row]) - 1 else None
            topLeftNeighbor = cellGrid[row - 1][col - 1] if row > 0 and col > 0 else None
            topRightNeighbor = cellGrid[row - 1][col + 1] if row > 0 and col < len(cellGrid[row]) - 1 else None
            bottomLeftNeighbor = cellGrid[row + 1][col - 1] if row < len(cellGrid) - 1 and col > 0 else None
            bottomRightNeighbor = cellGrid[row + 1][col + 1] if row < len(cellGrid) - 1 and col < len(cellGrid[row]) - 1 else None

            # Update the current cell's neighbors using the updateNeighbours method
            currentCell.updateNeighbours(
                topNeighbor if topNeighbor else Cell(0),
                bottomNeighbor if bottomNeighbor else Cell(0),
                leftNeighbor if leftNeighbor else Cell(0),
                rightNeighbor if rightNeighbor else Cell(0),
                topLeftNeighbor if topLeftNeighbor else Cell(0),
                topRightNeighbor if topRightNeighbor else Cell(0),
                bottomLeftNeighbor if bottomLeftNeighbor else Cell(0),
                bottomRightNeighbor if bottomRightNeighbor else Cell(0)
            )

def singleCycle(cellGrid):
    """Perform a single cycle of the cellular automata."""
    # First, update the neighbors of each cell in the grid
    updateGridNeighbours(cellGrid)

    # Then, update the state of each cell in the grid
    for row in range(len(cellGrid)):
        for col in range(len(cellGrid[row])):
            cell = cellGrid[row][col]
            cell.updateAlive()  

    return cellGrid

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