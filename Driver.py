from Cell import Cell
import random

def main():
    print("Start Position : ")
    cellGrid = generateGrid(xDim=10, yDim=10, choice=1)
    printGrid(cellGrid)

    startGrid=[[0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,1,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,1,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0]]
    
    print("User updated positions : ")
    generateGridStart(cellGrid=cellGrid, startGrid=startGrid)
    printGrid(cellGrid)


    n = int(input("Enter number of cycles : "))

    for i in range(n):
        print("Cycle Number = ", i)
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

def generateGridStart(cellGrid, startGrid):
    for row in range(len(cellGrid)):
        for col in range(len(cellGrid[row])):
            cellGrid[row][col].isAlive = startGrid[row][col]

def updateGrid(cellGrid):
    pass

def updateGridNeighbours(cellGrid):
    pass

def singleCycle(cellGrid):
    updateGrid(cellGrid=cellGrid)
    updateGridNeighbours(cellGrid=cellGrid)

    return cellGrid


    

if __name__ == "__main__":
    main()