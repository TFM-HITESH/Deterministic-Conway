import random

class Cell:
    def __init__(self, isAlive: int):
        self.isAlive = isAlive
    
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

        self.topEnergy = 0
        self.bottomEnergy = 0
        self.leftEnergy = 0
        self.rightEnergy = 0
        self.topLeftEnergy = 0
        self.topRightEnergy = 0
        self.bottomLeftEnergy = 0
        self.bottomRightEnergy = 0

    def printCell(self):
        """Prints the cell state for visualization."""
        if self.isAlive:
            print("■", end=" ")
        else:
            print("□", end=" ")

    def findSum(self):
        """Calculates the total number of living neighbors around the cell."""
        return self.top + self.bottom + self.left + self.right + self.topLeft + self.topRight + self.bottomLeft + self.bottomRight

    def findEnergySum(self):
        """Calculates the total energy from neighbours around the cell."""
        energySum = 0
        if(self.top):
            energySum -= self.topEnergy
        else:
            energySum += self.topEnergy
        if(self.bottom):
            energySum -= self.bottomEnergy
        else:
            energySum += self.bottomEnergy
        if(self.left):
            energySum -= self.leftEnergy
        else:
            energySum += self.leftEnergy
        if(self.right):
            energySum -= self.rightEnergy
        else:
            energySum += self.rightEnergy
        if(self.topLeft):
            energySum -= self.topLeftEnergy
        else:
            energySum += self.topLeftEnergy
        if(self.topRight):
            energySum -= self.topRightEnergy
        else:
            energySum += self.topRightEnergy
        if(self.bottomLeft):
            energySum -= self.bottomLeftEnergy
        else:
            energySum += self.bottomLeftEnergy
        if(self.bottomRight):
            energySum -= self.bottomRightEnergy
        else:
            energySum += self.bottomRightEnergy

        return energySum
        # return self.topEnergy*self.top*-1 + self.bottomEnergy*self.bottom*-1 + self.leftEnergy*self.left*-1 + self.rightEnergy*self.right*-1 + self.topRightEnergy*self.topRight*-1 + self.topLeftEnergy*self.topLeft*-1 + self.bottomLeftEnergy*self.bottomLeft*-1 + self.bottomRightEnergy*self.bottomRight*-1
    
    
    def updateAlive(self):
     """Updates the cell's state based on the number of living neighbors and axonal number."""
     neighbors = self.findSum()
     neighborEnergy = self.findEnergySum()
    
     # Check if the cell is alive and has a positive axonal number
     if self.isAlive:
        # Decrease energy for a living cell (sink)
        self.energy -= random.randint(10,15)  # Amount of energy consumed per cycle (you can adjust this value)
        if self.energy <= 0:
            self.isAlive = 0
            self.energy = 0  # The cell dies due to energy exhaustion
        elif neighbors < 2 or neighbors > 3:
            # Cell dies of underpopulation or overpopulation
            self.isAlive = 0
            self.energy = 0
        # Cell remains alive otherwise
     elif not self.isAlive:
        # Check if energy is sufficient to come back to life
        if self.energy >= 100:
            self.isAlive = 1
            self.energy = 100  # Reset energy level for new alive cell
        elif neighborEnergy >= 20:
            # Cell becomes alive due to reproduction
            self.isAlive = 1
            self.energy = 100  # Set energy to maximum for new alive cell
        else:
            # Increase energy for a dead cell (source)
            self.energy += random.randint(15,30)  # Amount of energy produced per cycle (adjust this value as needed)
    

      

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

        self.topEnergy = topNeighbour.energy
        self.bottomEnergy = bottomNeighbour.energy
        self.leftEnergy = leftNeighbour.energy
        self.rightEnergy = rightNeighbour.energy
        self.topLeftEnergy = topLeftNeighbour.energy
        self.topRightEnergy = topRightNeighbour.energy
        self.bottomLeftEnergy = bottomLeftNeighbour.energy
        self.bottomRightEnergy = bottomRightNeighbour.energy