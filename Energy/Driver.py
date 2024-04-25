from Cell import Cell
import matplotlib.pyplot as plt
import numpy as np
import random
import time

X_DIM = 80
Y_DIM = 80
ALIVE_CELL = Cell(1)
DEAD_CELL = Cell(0)

GOL_LIST = []
ALIVE_COUNT_LIST = []

N = 38

def main():
    # Display start position
    print("Start Position:")
    cellGrid = generateGrid(xDim=X_DIM, yDim=Y_DIM, choice=-1)  # Random initial state
    printGrid(cellGrid)

    # Optional: Specify a custom initial grid configuration
    startGrid = [
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 1, 1, 1, 0]
    ]
    print("User updated positions:")
    # generateGridStart(cellGrid=cellGrid, startGrid=startGrid2)
    printGrid(cellGrid)

    # Number of cycles to simulate


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
            cell.updateAlive()  # This now includes energy dynamics

    return cellGrid

def aliveNumber(cellGrid):
    aliveCount = 0
    for row in range(len(cellGrid)):
        for col in range(len(cellGrid[row])):
            if(cellGrid[row][col].isAlive == 1):
                aliveCount +=1 
    
    return aliveCount

def drawGraph(n):
    # Plots the scatter points
    plt.plot(range(0,n), ALIVE_COUNT_LIST, marker='o', linestyle='', markersize=8, color='r', label='Scatter Plot')

    # Line of best fit
    theta = np.polyfit(range(0,n), ALIVE_COUNT_LIST, 1)
    yLine = theta[1] + theta[0] * range(0,n)

    plt.plot(range(0,n), yLine, 'b')
    
    plt.show()

if __name__ == "__main__":
    main()