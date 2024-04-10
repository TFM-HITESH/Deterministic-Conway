

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

    def __init__(self):
        pass

    # Returns the number of alive neighbours
    def findSum(self):
        return self.top + self.bottom + self.left + self.right + self.topLeft + self.topRight + self.bottomLeft + self.bottomRight
    
    def updateAlive(self):
        neighbours = self.findSum()

        if(self.isAlive == 1):
            # If cell is alive
            if(neighbours < 2):
                self.isAlive = 0 
                # Dies of underpopulation
            elif(neighbours == 2 or neighbours == 3):
                self.isAlive = 1
                # Lives on
            elif(neighbours > 3):
                self.isAlive = 0
                # Dies of overpopulation
        elif(self.isAlive == 0):
            # If cell is dead
            if(neighbours == 3):
                self.isAlive = 1
                # Comes alive of Reproduction


    



