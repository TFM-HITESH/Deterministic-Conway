import random

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
        if self.isAlive == 1:
            print("■ ", sep="", end="")
        else:
            print("□ ", sep="", end="")

    # Returns the number of alive neighbours
    def findSum(self, pl):
        sum = 0
        probabilities = [random.random() for _ in range(8)]  # Generate random numbers for each neighbor
        # Check probability for each neighbor and add to sum if it meets the criteria
        sum += self.top if probabilities[0] <= pl[0] else 0
        sum += self.bottom if probabilities[1] <= pl[1] else 0
        sum += self.left if probabilities[2] <= pl[2] else 0
        sum += self.right if probabilities[3] <= pl[3] else 0
        sum += self.topLeft if probabilities[4] <= pl[4] else 0
        sum += self.topRight if probabilities[5] <= pl[5] else 0
        sum += self.bottomLeft if probabilities[6] <= pl[6] else 0
        sum += self.bottomRight if probabilities[7] <= pl[7] else 0
        return sum
    
    def updateAlive(self, pl):
        neighbours = self.findSum(pl)

        if self.isAlive == 1:
            # If cell is alive
            if neighbours < 2:
                self.isAlive = 0 
                # Dies of underpopulation
            elif neighbours == 2 or neighbours == 3:
                self.isAlive = 1
                # Lives on
            elif neighbours > 3:
                self.isAlive = 0
                # Dies of overpopulation
        elif self.isAlive == 0:
            # If cell is dead
            if neighbours == 3:
                self.isAlive = 1
                # Comes alive of Reproduction

    def updateNeighbours(self, topNeighbour, bottomNeighbour, leftNeighbour, rightNeighbour, topLeftNeighbour, topRightNeighbour, bottomLeftNeighbour, bottomRightNeighbour, pl):
        # Taking objects of all the neighbours that surround the current cell and updating the values of current cell in case they're alive

        if topNeighbour.isAlive == 1:
            self.top = 1
        else:
            self.top = 0
        if bottomNeighbour.isAlive == 1:
            self.bottom = 1
        else:
            self.bottom = 0
        if leftNeighbour.isAlive == 1:
            self.left = 1
        else:
            self.left = 0
        if rightNeighbour.isAlive == 1:
            self.right = 1
        else:
            self.right = 0
        if topLeftNeighbour.isAlive == 1:
            self.topLeft = 1
        else:
            self.topLeft = 0
        if topRightNeighbour.isAlive == 1:
            self.topRight = 1
        else:
            self.topRight = 0
        if bottomLeftNeighbour.isAlive == 1:
            self.bottomLeft = 1
        else:
            self.bottomLeft = 0
        if bottomRightNeighbour.isAlive == 1:
            self.bottomRight = 1
        else:
            self.bottomRight = 0
