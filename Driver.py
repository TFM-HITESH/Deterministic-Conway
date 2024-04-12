from Cell import Cell
import random
import time

X_DIM = 10
Y_DIM = 10

def main():
    print("Start Position : ")
    cellGrid = generateGrid(xDim=X_DIM, yDim=Y_DIM, choice=1)
    printGrid(cellGrid)

    startGrid=[[0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,1,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0]]
    
    startGrid2=[[0,0,0,0,0,0,0,0,0,0],
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
    generateGridStart(cellGrid=cellGrid, startGrid=startGrid2)
    printGrid(cellGrid)

    # Preparing the grid and giving info about number of neighbours
    updateGridNeighbours(cellGrid=cellGrid)
    print("The grid is now prepared and we are ready to start the Game of life !")


    n = int(input("Enter number of cycles : "))

    for i in range(n):
        time.sleep(1)
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
    for row in range(1, len(cellGrid)-1):
        for col in range(1, len(cellGrid[row])-1):
            #top = row--, bottom = row++, left = col--, right = col++
            topRight = cellGrid[row - 1][col + 1]
            topLeft = cellGrid[row - 1][col - 1]
            bottomRight = cellGrid[row + 1][col + 1]
            bottomLeft = cellGrid[row + 1][col - 1]
            top = cellGrid[row - 1][col]
            bottom = cellGrid[row + 1][col]
            left = cellGrid[row][col - 1]
            right = cellGrid[row][col + 1]

            cellGrid[row][col].updateNeighbours(topRightNeighbour=topRight, topLeftNeighbour=topLeft, bottomRightNeighbour=bottomRight, bottomLeftNeighbour=bottomLeft, topNeighbour=top, bottomNeighbour=bottom, rightNeighbour=right, leftNeighbour=left)

def singleCycle(cellGrid):
    updateGrid(cellGrid=cellGrid)
    updateGridNeighbours(cellGrid=cellGrid)

    return cellGrid

if __name__ == "__main__":
    main()