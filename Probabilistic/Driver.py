from Cell import Cell
import matplotlib.pyplot as plt
import numpy as np
import random
import time

X_DIM = 60
Y_DIM = 60
ALIVE_CELL = Cell(1)
DEAD_CELL = Cell(0)

PROBABILITY_LIVING=[0.99, 0.95, 0.95, 0.95, 0.9, 0.9, 0.85, 0.85, 0.85]

GOL_LIST = []
ALIVE_COUNT_LIST = []

N = 38

def get_pl():
    return PROBABILITY_LIVING

def main():
    print("Start Position : ")
    cellGrid = generateGrid(xDim=X_DIM, yDim=Y_DIM, choice=-1)
    printGrid(cellGrid)

    startGrid = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0],
        [0,0,1,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]
    
    print("User updated positions : ")
   # generateGridStart(cellGrid=cellGrid, startGrid=startGrid)
    printGrid(cellGrid)

    # Preparing the grid and giving info about number of neighbours
    updateGridNeighbours(cellGrid=cellGrid)
    print("The grid is now prepared and we are ready to start the Game of life !")

    # n = int(input("Enter number of cycles : "))

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
    # Plots the scatter points
    plt.plot(range(0,n), ALIVE_COUNT_LIST, marker='o', linestyle='', markersize=8, color='deeppink', label='Scatter Plot')

    # Line of best fit
    theta = np.polyfit(range(0,n), ALIVE_COUNT_LIST, 1)
    yLine = theta[1] + theta[0] * range(0,n)

    print("y = ", round(theta[0],4), "* x +", round(theta[1],4))

    plt.plot(range(0,n), yLine, 'darkorchid')
    
    plt.show()

if __name__ == "__main__":
    main()

