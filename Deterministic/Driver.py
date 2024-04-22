from Cell import Cell
import random
import time


# global variables
X_DIM = 10
Y_DIM = 10
ALIVE_CELL = Cell(1)
DEAD_CELL = Cell(0)


def main():
    print("Start Position : ")
    cellGrid = generateGrid(xDim=X_DIM, yDim=Y_DIM, choice=0)
    printGrid(cellGrid)

    startGrid=[[0,0,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0],
               [0,0,0,0,1,0,0,0,0,0],
               [0,0,1,1,1,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0]]
    
    print("User updated positions : ")
    generateGridStart(cellGrid=cellGrid, startGrid=startGrid
                      )
    printGrid(cellGrid)

    # Preparing the grid and giving info about number of neighbours
    updateGridNeighbours(cellGrid=cellGrid)
    print("The grid is now prepared and we are ready to start the Game of life !")


    n = int(input("Enter number of cycles : "))

    for i in range(n):
        time.sleep(0.4)
        print("Cycle Number = ", i+1)
        cellGrid = singleCycle(cellGrid=cellGrid)
        printGrid(cellGrid=cellGrid)
        
    

def generateGrid(xDim, yDim, choice):
    # The final grid of cells
    cellGrid = []

    for row in range(yDim):
        cellRow = []
        for col in range(xDim):
            if (choice == 0):
                cell = Cell(0)
            elif (choice == 1):
                cell = Cell(1)
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

# Updates the grid with the starting connfiguration provided by the user
def generateGridStart(cellGrid, startGrid):
    for row in range(len(cellGrid)):
        for col in range(len(cellGrid[row])):
            cellGrid[row][col].isAlive = startGrid[row][col]

# Updates the grid, killing off the cells that must die
def updateGrid(cellGrid):
    for row in range(1, len(cellGrid)-1):
        for col in range(1, len(cellGrid[row])-1):
            cellGrid[row][col].updateAlive()

#Updates everyone's neighbours, based on the new grid
def updateGridNeighbours(cellGrid):
    for row in range(len(cellGrid)):
        for col in range(len(cellGrid[row])):
            #top = row--, bottom = row++, left = col--, right = col++
            try:
                topRight = cellGrid[row - 1][col + 1]
            except:
                topRight = DEAD_CELL
            try:
                topLeft = cellGrid[row - 1][col - 1]
            except:
                topLeft = DEAD_CELL
            try:
                bottomRight = cellGrid[row + 1][col + 1]
            except:
                bottomRight = DEAD_CELL
            try:
                bottomLeft = cellGrid[row + 1][col - 1]
            except:
                bottomLeft = DEAD_CELL
            try:
                top = cellGrid[row - 1][col]
            except:
                top = DEAD_CELL
            try:
                bottom = cellGrid[row + 1][col]
            except: 
                bottom = DEAD_CELL
            try:
                left = cellGrid[row][col - 1]
            except:
                left = DEAD_CELL
            try: 
                right = cellGrid[row][col + 1] 
            except:
                right = DEAD_CELL
            
            # Updating the neighbours
            cellGrid[row][col].updateNeighbours(topRightNeighbour=topRight, topLeftNeighbour=topLeft, bottomRightNeighbour=bottomRight, bottomLeftNeighbour=bottomLeft, topNeighbour=top, bottomNeighbour=bottom, rightNeighbour=right, leftNeighbour=left)

def singleCycle(cellGrid):
    updateGrid(cellGrid=cellGrid)
    updateGridNeighbours(cellGrid=cellGrid)

    return cellGrid

if __name__ == "__main__":
    main()