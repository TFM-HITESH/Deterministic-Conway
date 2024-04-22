# global variables
MIN_POPULATION = 2
MAX_POPULATION = 3
REVIVE_POPULATION = 3


class Cell:

    # Current State of Cell (0-Dead, 1-Alive)
    isAlive = 0

    # Dead Cells all around current cell
    top = 0
    bottom = 0
    left = 0
    right = 0
    topLeft = 0
    topRight = 0
    bottomLeft = 0
    bottomRight = 0

    # Creating a new cell
    def __init__(self, isAlive : int):
        self.isAlive = isAlive

        self.top = 0
        self.bottom = 0 
        self.left = 0 
        self.right = 0 
        self.topLeft = 0 
        self.topRight = 0 
        self.bottomLeft = 0 
        self.bottomRight = 0

    def printCell(self):
        if(self.isAlive == 1):
            print("■ ", sep = "", end = "")
        else:
            print("□ ", sep = "", end = "")

    # Returns the number of alive neighbours
    def findSum(self):
        return self.top + self.bottom + self.left + self.right + self.topLeft + self.topRight + self.bottomLeft + self.bottomRight
    
    def updateAlive(self):
        neighbours = self.findSum()

        if(self.isAlive == 1):
            # If cell is alive
            if(neighbours < MIN_POPULATION):
                self.isAlive = 0 
                # Dies of underpopulation
            elif(neighbours >= MIN_POPULATION and neighbours <= MAX_POPULATION):
                self.isAlive = 1
                # Lives on
            elif(neighbours > MAX_POPULATION):
                self.isAlive = 0
                # Dies of overpopulation
        elif(self.isAlive == 0):
            # If cell is dead
            if(neighbours == REVIVE_POPULATION):
                self.isAlive = 1
                # Comes alive of Reproduction

    def updateNeighbours(self, topNeighbour, bottomNeighbour, leftNeighbour, rightNeighbour, topLeftNeighbour, topRightNeighbour, bottomLeftNeighbour, bottomRightNeighbour):
        # Taking objects of all the neighbours that surround the current cell and updating the values of current cell in case theyre alive

        if(topNeighbour.isAlive == 1):
            self.top = 1
        else:
            self.top = 0
        if(bottomNeighbour.isAlive == 1):
            self.bottom = 1
        else:
            self.bottom = 0
        if(leftNeighbour.isAlive == 1):
            self.left = 1
        else:
            self.left = 0
        if(rightNeighbour.isAlive == 1):
            self.right = 1
        else:
            self.right = 0
        if(topLeftNeighbour.isAlive == 1):
            self.topLeft = 1
        else:
            self.topLeft = 0
        if(topRightNeighbour.isAlive == 1):
            self.topRight = 1
        else:
            self.topRight = 0
        if(bottomLeftNeighbour.isAlive == 1):
            self.bottomLeft = 1
        else:
            self.bottomLeft = 0
        if(bottomRightNeighbour.isAlive == 1):
            self.bottomRight = 1
        else:
            self.bottomRight = 0


    



