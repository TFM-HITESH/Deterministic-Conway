import random

AXONAL_LOWER = 15
AXONAL_UPPER = 20

NO_DEGENERATION_CHANCE = 0.02
DOUBLE_DEGENERATION_CHANCE = 0.02

class Cell:
    def __init__(self, isAlive: int):
        self.isAlive = isAlive
        # Initialize axonal number for each cell
        self.axonalNumber = random.randint(AXONAL_LOWER, AXONAL_UPPER)
        # Initialize energy level
       
        self.top = 0
        self.bottom = 0
        self.left = 0
        self.right = 0
        self.topLeft = 0
        self.topRight = 0
        self.bottomLeft = 0
        self.bottomRight = 0

    def printCell(self):
        """Prints the cell state for visualization."""
        if self.isAlive:
            print("■", end=" ")
        else:
            print("□", end=" ")

    def findSum(self):
        """Calculates the total number of living neighbors around the cell."""
        return self.top + self.bottom + self.left + self.right + self.topLeft + self.topRight + self.bottomLeft + self.bottomRight

    def decayAxonalNumber(self):
        """Performs the decay of the cell's axonal number with probabilistic chance."""
        chance = random.random()
        if chance < DOUBLE_DEGENERATION_CHANCE:
            # Decrease by 2 with 2% chance
            self.axonalNumber -= 2
        elif chance >1- NO_DEGENERATION_CHANCE:
            # No change with 2% chance
            pass
        else:
            # Decrease by 1
            self.axonalNumber -= 1
        self.axonalNumber = max(self.axonalNumber, 0)
    
    def updateAlive(self):
        """Updates the cell's state based on the axonal number."""
        neighbors = self.findSum()
        # Check if the cell is alive and has a positive axonal number
        if self.isAlive and self.axonalNumber > 0:
            # Decrease energy for a living cell (sink)
          
            if neighbors < 2 or neighbors > 3:
                # Cell dies of underpopulation or overpopulation
                self.isAlive = 0
               
            # Cell remains alive otherwise
        elif not self.isAlive and neighbors == 3 and self.axonalNumber > 0:
            # Cell becomes alive due to reproduction
            self.isAlive = 1
            
        self.decayAxonalNumber()

    def updateNeighbours(self, topNeighbour, bottomNeighbour, leftNeighbour, rightNeighbour, topLeftNeighbour, topRightNeighbour, bottomLeftNeighbour, bottomRightNeighbour):
        """Updates the neighbor information for the current cell."""
        self.top = topNeighbour.isAlive if topNeighbour else 0
        self.bottom = bottomNeighbour.isAlive if bottomNeighbour else 0
        self.left = leftNeighbour.isAlive if leftNeighbour else 0
        self.right = rightNeighbour.isAlive if rightNeighbour else 0
        self.topLeft = topLeftNeighbour.isAlive if topLeftNeighbour else 0
        self.topRight = topRightNeighbour.isAlive if topRightNeighbour else 0
        self.bottomLeft = bottomLeftNeighbour.isAlive if bottomLeftNeighbour else 0
        self.bottomRight = bottomRightNeighbour.isAlive if bottomRightNeighbour else 0