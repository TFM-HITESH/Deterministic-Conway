# from Cell import Cell
# import random
# import time

# X_DIM = 10
# Y_DIM = 10
# ALIVE_CELL = Cell(1)
# DEAD_CELL = Cell(0)
# pl = [0.99, 0.95, 0.95, 0.95, 0.9, 0.9, 0.85, 0.85, 0.85]
# #c1 is top left cell and then move clockwise 


# def get_pl():
#     return pl
# def main():
#     print("Start Position : ")
#     cellGrid = generateGrid(xDim=X_DIM, yDim=Y_DIM, choice=0)
#     printGrid(cellGrid)

#     startGrid=[[0,0,0,0,0,0,0,0,0,0],
#                [0,0,0,1,0,0,0,0,0,0],
#                [0,0,0,0,1,0,0,0,0,0],
#                [0,0,1,1,1,0,0,0,0,0],
#                [0,0,0,0,0,0,0,0,0,0],
#                [0,0,0,0,0,0,0,0,0,0],
#                [0,0,0,0,0,0,0,0,0,0],
#                [0,0,0,0,0,0,0,0,0,0],
#                [0,0,0,0,0,0,0,0,0,0],
#                [0,0,0,0,0,0,0,0,0,0]]
    
#     print("User updated positions : ")
#     generateGridStart(cellGrid=cellGrid, startGrid=startGrid
#                       )
#     printGrid(cellGrid)

#     # Preparing the grid and giving info about number of neighbours
#     updateGridNeighbours(cellGrid=cellGrid)
#     print("The grid is now prepared and we are ready to start the Game of life !")


#     n = int(input("Enter number of cycles : "))

#     for i in range(n):
#         time.sleep(0.4)
#         print("Cycle Number = ", i+1)
#         cellGrid = singleCycle(cellGrid=cellGrid)
#         printGrid(cellGrid=cellGrid)
        
    

# def generateGrid(xDim, yDim, choice):
#     # The final grid of cells
#     cellGrid = []

#     for row in range(yDim):
#         cellRow = []
#         for col in range(xDim):
#             if (choice == 0):
#                 cell = Cell(0)
#             elif (choice == 1):
#                 cell = Cell(1)
#             else:
#                 cell = Cell(random.choice([0,1]))
#             cellRow.append(cell)
#         cellGrid.append(cellRow)

#     return cellGrid

# # Shows the current state of the grid
# def printGrid(cellGrid):

#     for cellRow in cellGrid:
#         for cell in cellRow:
#             # Invoked cell printer
#             cell.printCell()
#         print()

# # Updates the grid with the starting connfiguration provided by the user
# def generateGridStart(cellGrid, startGrid):
#     for row in range(len(cellGrid)):
#         for col in range(len(cellGrid[row])):
#             cellGrid[row][col].isAlive = startGrid[row][col]

# # Updates the grid, killing off the cells that must die
# def updateGrid(cellGrid):
#     for row in range(1, len(cellGrid)-1):
#         for col in range(1, len(cellGrid[row])-1):
#             cellGrid[row][col].updateAlive()

# #Updates everyone's neighbours, based on the new grid
# def updateGridNeighbours(cellGrid):
#     for row in range(len(cellGrid)):
#         for col in range(len(cellGrid[row])):
        
#             pl=get_pl()
#             #top = row--, bottom = row++, left = col--, right = col++
#             try:
#                 topRight = cellGrid[row - 1][col + 1].findSum(pl)
#             except:
#                 topRight = DEAD_CELL
#             try:
#                 topLeft = cellGrid[row - 1][col - 1].findSum(pl)
#             except:
#                 topLeft = DEAD_CELL
#             try:
#                 bottomRight = cellGrid[row + 1][col + 1].findSum(pl)
#             except:
#                 bottomRight = DEAD_CELL
#             try:
#                 bottomLeft = cellGrid[row + 1][col - 1].findSum(pl)
#             except:
#                 bottomLeft = DEAD_CELL
#             try:
#                 top = cellGrid[row - 1][col].findSum(pl)
#             except:
#                 top = DEAD_CELL
#             try:
#                 bottom = cellGrid[row + 1][col].findSum(pl)
#             except: 
#                 bottom = DEAD_CELL
#             try:
#                 left = cellGrid[row][col - 1].findSum(pl)
#             except:
#                 left = DEAD_CELL
#             try: 
#                 right = cellGrid[row][col + 1].findSum(pl) 
#             except:
#                 right = DEAD_CELL
            
#             # Updating the neighbours
#             cellGrid[row][col].updateNeighbours(topRightNeighbour=topRight, topLeftNeighbour=topLeft, bottomRightNeighbour=bottomRight, bottomLeftNeighbour=bottomLeft, topNeighbour=top, bottomNeighbour=bottom, rightNeighbour=right, leftNeighbour=left)

# def singleCycle(cellGrid):
#     updateGrid(cellGrid=cellGrid)
#     updateGridNeighbours(cellGrid=cellGrid)

#     return cellGrid

# if __name__ == "__main__":
#     main()







from Cell import Cell
import random
import time

X_DIM = 10
Y_DIM = 10
pl=[0.99, 0.95, 0.95, 0.95, 0.9, 0.9, 0.85, 0.85, 0.85]
def get_pl():
    return pl


def main():
    print("Start Position : ")
    cellGrid = generateGrid(xDim=X_DIM, yDim=Y_DIM, choice=0)
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
    generateGridStart(cellGrid=cellGrid, startGrid=startGrid)
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
            if choice == 0:
                cell = Cell(0)
            elif choice == 1:
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
            cellGrid[row][col].updateAlive()

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
            if __name__ == "__main__":
             main()
