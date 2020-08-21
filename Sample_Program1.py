class Sorcery:
    'Common base class for magic spells'
    sorceryCount = 0

    def __init__(self, name, MPCost, element):
        self.name = name
        self.MPCost = MPCost
        self.element = element
        Sorcery.sorceryCount += 1

    def displayCount(self):
        print("Total Sorceries: %d" % Sorcery.sorceryCount)

    def displayMagicAttributes(self):
        print("Name: " + self.name + '\n' + "MP Cost: %d" % self.MPCost)
        print("Element: " + self.element)

    def getName(self):
        return self.name

# Creates some basic spells and returns a
# list of them
def createSpells(hippoFlag):
    spellBook = []
    fireBall = Sorcery("Fireball", 5, "Fire")
    iceStorm = Sorcery("Ice Storm", 20, "Frost")
    shadowDagger = Sorcery("Shadow Dagger", 7, "Dark")

    spellBook.append(fireBall)
    spellBook.append(iceStorm)
    spellBook.append(shadowDagger)

    if (hippoFlag):
        summonHippo = Sorcery("Summon Hippopotamus", 50, "Arcane")
        spellBook.append(summonHippo)

    return spellBook

#The printSpellBook function takes in a boolean and
#will print a list of spells depending on what the boolean
#is initialized to. It will not print the list if the
#size of the spell list is 0, or if forbidden spells
#are allowed.
def printSpellBook(includeForbiddenSpells):
    hippoSpellName = "Summon Hippopotamus"
    hippoFlag = False
    forbiddenSpellLocation = -1
    spellBook = createSpells(includeForbiddenSpells)

    if (len(spellBook) <= 0):
        print("The spell book is currently empty;")
        print("Please add some spells if you are wanting to print them.")
        return

    print("Checking to see if all spells in the spell book are valid...")
    for i in range(len(spellBook)):
        if (spellBook[i].getName() == hippoSpellName):
            hippoFlag = True
            forbiddenSpellLocation = i

    spellBook[0].displayCount()
    if (hippoFlag):
        print("The hippopotamus spell is too powerful. It")
        print("should not be added to the spellBook!")
        print("Here's some info on it anyway:")
        spellBook[forbiddenSpellLocation].displayMagicAttributes()
        return

    print("Check complete! All spells are valid and hippo free.")
    print("Here is some info on the spells included:")
    for i in range(len(spellBook)):
        spellBook[i].displayMagicAttributes()
    return
