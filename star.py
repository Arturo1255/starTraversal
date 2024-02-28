class Star:
    def __init__(self, ID, name, distance, x, y, z):
        self.ID = ID
        self.name = name
        self.distance = distance
        self.x = x
        self.y = y
        self.z = z
        self.found = False

    def setFound(self, value):
        self.found = value

    def getFound(self):
        return self.found

    def getName(self):
        return self.name

    def getDistance(self):
        return self.distance

    def getXYZ(self):
        return self.x, self.y, self.z

    def getID(self):
        return self.ID

    def printInfo(self):
        print("ID:", self.ID)
        print("Name:", self.name)
        print("Distance:", self.distance)
        print("X:", self.x)
        print("Y:", self.y)
        print("Z:", self.z)