class Sorcery:
    'Common base class for Sorceries'
    sorceryCount = 0

    def __init__(self, name, MPCost, element, isForbidden):
        self.name = name
        self.MPCost = MPCost
        self.element = element
        self.forbidden = isForbidden
        Sorcery.sorceryCount += 1

    def displayCount(self):
        print("Total Sorceries: %d" % Sorcery.sorceryCount)

    def displayMagicAttributes(self):
        print("Name: " + self.name + '\n' + "MP Cost: %d" % self.MPCost)
        print("Element: " + self.element)

    def getName(self):
        return self.name

    def getMPCost(self):
        return self.MPCost
        
    def getElementalAlignment(self):
        return self.element

    def getForbiddenStatus(self):
        return self.forbidden