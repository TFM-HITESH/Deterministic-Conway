import random

class Cell:
    def __init__(self, isAlive: int):
        self.isAlive = isAlive
        # Initialize axonal number for each cell
        self.axonal_number = random.randint(17, 23)
        # Initialize energy level
        self.energy = 100 if self.isAlive else 0  # Starting energy for alive cells
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
        if chance < 0.02:
            # Decrease by 2 with 2% chance
            self.axonal_number -= 2
        elif chance > 0.98:
            # No change with 2% chance
            pass
        else:
            # Decrease by 1
            self.axonal_number -= 1
        self.axonal_number = max(self.axonal_number, 0)

    
    def updateAlive(self):
        """Updates the cell's state based on the number of living neighbors and axonal number."""
        neighbors = self.findSum()
        # Check if the cell is alive and has a positive axonal number
        if self.isAlive and self.axonal_number > 0:
            # Decrease energy for a living cell (sink)
            self.energy -= 10  # Amount of energy consumed per cycle (you can adjust this value)
            if self.energy <= 0:
                self.isAlive = 0
                self.energy = 0  # The cell dies due to energy exhaustion
            elif neighbors < 2 or neighbors > 3:
                # Cell dies of underpopulation or overpopulation
                self.isAlive = 0
                self.energy = 0
            # Cell remains alive otherwise
        elif not self.isAlive and neighbors == 3 and self.axonal_number > 0:
            # Cell becomes alive due to reproduction
            self.isAlive = 1
            self.energy = 100  # Reset energy level for new alive cell
        elif not self.isAlive:
            # Increase energy for a dead cell (source)
            self.energy += 5  # Amount of energy produced per cycle (adjust this value as needed)
        # Decay axonal number after updating cell state
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