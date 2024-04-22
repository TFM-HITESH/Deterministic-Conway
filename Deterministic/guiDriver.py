from Cell import Cell
import random
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


# global variables
X_DIM = 80
Y_DIM = 80
ALIVE_CELL = Cell(1)
DEAD_CELL = Cell(0)


GOL_LIST = []


def main():
    cellGrid = generateGrid(xDim=X_DIM, yDim=Y_DIM, choice=-1)

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
    

    # generateGridStart(cellGrid=cellGrid, startGrid=startGrid)

    # Preparing the grid and giving info about number of neighbours
    updateGridNeighbours(cellGrid=cellGrid)

    # cellGrid = singleCycle(cellGrid=cellGrid)
    # printGrid(cellGrid=GOL_LIST[0])

    n = int(input("Enter the number of cycles :"))

    generateGOLLIST(n, cellGrid=cellGrid)
    
    currentStep = 0
    generateGUI(currentStep=currentStep)
    
    

    
        

def generateGUI(currentStep):
    GOLApp = QApplication([])
    GOLWindow = QWidget()

    # Modifying the window
    GOLWindow.setGeometry(480, 135, 960, 810)
    # (x_offset, y_offset, x_width, y_height)

    GOLWindowWidth = GOLWindow.width()
    GOLWindowHeight = GOLWindow.height()

    GOLWindow.setWindowTitle("CGOL")
    GOLWindow.setStyleSheet("background-color: #434343;")

    GOLLayout = QVBoxLayout() 
    
    # Create and configure the title label
    titleLabel = QLabel(GOLWindow)
    titleLabel.setText("CONWAY'S GAME OF LIFE")
    titleLabel.setFont(QFont("Arial", 24))

    GOLButtonLayout = QHBoxLayout()

    stepBackwardButton = QPushButton("<- Step Backward")
    stepBackwardButton.setFont(QFont("Arial", 16))
    stepBackwardButton.setStyleSheet(
        "QPushButton {"
        "background-color: #4CAF50; /* Green */"
        "border: none;"
        "color: white;"
        "padding: 15px 32px;"
        "text-align: center;"
        "text-decoration: none;"
        "font-size: 1rem;"
        "border-radius: 10px;"
        "}"
        "QPushButton:hover {"
        "background-color: #45a049; /* Darker green */"
        "}"
    )


    stepForwardButton = QPushButton("Step Forward ->")
    stepForwardButton.setFont(QFont("Arial", 16))
    # stepForwardButton.setStyleSheet("background-color: red; color: white; font-size: 16px; font-weight: bold; border: 2px solid black;")
    stepForwardButton.setStyleSheet(
        "QPushButton {"
        "background-color: #4CAF50; /* Green */"
        "border: none;"
        "color: white;"
        "padding: 15px 32px;"
        "text-align: center;"
        "text-decoration: none;"
        "font-size: 1rem;"
        "border-radius: 10px;"
        "}"
        "QPushButton:hover {"
        "background-color: #45a049; /* Darker green */"
        "}"
    )

    GOLButtonLayout.addWidget(stepBackwardButton)
    GOLButtonLayout.addWidget(stepForwardButton)

    GOLBoardLayout = generateGridLayout(GOL_LIST[currentStep], GOLWindow=GOLWindow, GOLWindowWidth=GOLWindowWidth, GOLWindowHeight=GOLWindowHeight)


    GOLLayout.addWidget(titleLabel)
    GOLLayout.addLayout(GOLBoardLayout)
    GOLLayout.addLayout(GOLButtonLayout)

    GOLWindow.setLayout(GOLLayout)
    


    GOLWindow.show()
    GOLApp.exec_()

def generateGridLayout(cellGrid, GOLWindow, GOLWindowWidth, GOLWindowHeight):
    GOLBoardLayout = QVBoxLayout()
    GOLBoardLayout.setSpacing(0)
    
    for i in range(len(cellGrid)):
        GOLBoardRowLayout = QHBoxLayout()
        GOLBoardRowLayout.addSpacing(0)
        for j in range(len(cellGrid[0])):
            if(cellGrid[i][j].isAlive == 1):
                WhiteBox = QLabel(GOLWindow)
                WhiteBox.setGeometry(0, 0, 10, 10)  # Set position and size of the box
                WhiteBox.setFixedWidth(int((GOLWindowHeight/len(cellGrid))*0.8))
                WhiteBox.setFixedHeight(int((GOLWindowHeight/len(cellGrid))*0.8))
                WhiteBox.setStyleSheet(
                    "QLabel {"
                        "background-color: #ffffff;"
                        # "border: 1px solid #343434;"
                        "border-radius: 0px;"
                    "}"
                    "QLabel:hover {"
                        "background-color: #dddddd;"
                    "}"
                ) 
                GOLBoardRowLayout.addWidget(WhiteBox)
            else:
                BlackBox = QLabel(GOLWindow)
                BlackBox.setGeometry(0, 0, 10, 10)  # Set position and size of the box
                BlackBox.setFixedWidth(int((GOLWindowHeight/len(cellGrid))*0.8))
                BlackBox.setFixedHeight(int((GOLWindowHeight/len(cellGrid))*0.8))
                BlackBox.setStyleSheet(
                    "QLabel {"
                        "background-color: #000000;"
                        # "border: 1px solid #9a9a9a;"
                        "border-radius: 0px;"
                    "}"
                    "QLabel:hover {"
                        "background-color: #222222;"
                    "}"
                ) 
                GOLBoardRowLayout.addWidget(BlackBox)
            
        GOLBoardLayout.addLayout(GOLBoardRowLayout)
        GOLBoardLayout.addSpacing(0)  # Add spacing between row layouts

    return(GOLBoardLayout)


def updateGUI():
    pass

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

    GOL_LIST.append(cellGrid)
    return cellGrid

def generateGOLLIST(n, cellGrid):
    for i in range(n):
        # time.sleep(0.4)
        print("Cycle Number = ", i+1)
        cellGrid = singleCycle(cellGrid=cellGrid)
        printGrid(cellGrid=cellGrid)

if __name__ == "__main__":
    main()