class Sorcery:
    'Common base class for magic spells'
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

# Creates some basic spells and returns a
# list of them
def createSpells(forbiddenSpellFlag, hippoFlag):
    spellBook = []
    fireBall = Sorcery("Fireball", 5, "Fire", False)
    iceStorm = Sorcery("Ice Storm", 20, "Frost", False)
    shadowDagger = Sorcery("Shadow Dagger", 7, "Dark", False)
    arcaneShield = Sorcery("Arcane Shield", 12, "Arcane", False)

    spellBook.append(fireBall)
    spellBook.append(iceStorm)
    spellBook.append(shadowDagger)
    spellBook.append(arcaneShield)

    if (forbiddenSpellFlag):
        chaosFireball = Sorcery("Chaos Fireball", 20, "Fire", True)
        raiseUndead = Sorcery("Raise Undead", 15, "Unholy", True)
        shadowLance = Sorcery("Shadow Lance", 30, "Dark", True)
        spellBook.append(chaosFireball)
        spellBook.append(raiseUndead)
        spellBook.append(shadowLance)

    if (hippoFlag):
        summonHippo = Sorcery("Summon Hippopotamus", 50, "Arcane", True)
        spellBook.append(summonHippo)

    return spellBook

# The printSpellBook function takes in a spell book and
# will print a list of the spells in the spell book. It
# will not print the list if the size of the spell book
# is 0. Additionally, the type of output printed will vary
# depending on whether the spell book contains forbidden
# spells
def printSpellBook(spellBook):
    hippoSpellName = "Summon Hippopotamus"
    hippoFlag = False
    forbiddenSpellFlag = False
    hippoSpellLocation = None

    if (len(spellBook) <= 0):
        print("The spell book is currently empty;")
        print("Please add some spells if you are wanting to print them.")
        return

    print("Checking to see if all spells in the spell book are valid...")
    for i in range(len(spellBook)):
        if ((spellBook[i].getName() == hippoSpellName) and spellBook[i].getForbiddenStatus()):
            hippoFlag = True
            hippoSpellLocation = i
            break
        elif(spellBook[i].getForbiddenStatus()):
            forbiddenSpellFlag = True

    spellBook[0].displayCount()
    if (hippoFlag):
        print("The hippopotamus spell is too powerful. It ")
        print("should not be added to the spellBook! ")
        print("Here's some info on it anyway: ")
        # The variable hippoSpellLocation should have been initialized
        # before it is used since, after setting the hippoFlag variable
        # to True, we immediately initialize it to a numerical value,
        # and additionally this is the only location it is used. We will
        # still check anyway however just to be safe.
        if (hippoSpellLocation is not None):
            spellBook[hippoSpellLocation].displayMagicAttributes()
        else:
            print("Error: the variable hippoSpellLocation was never set.")

    elif(forbiddenSpellFlag):
        print("Caution: At least one forbidden spell was found.")
        print("Here is a complete list of the forbidden spells")
        print("found in the spell book:")
        for spell in spellBook:
            if (spell.getForbiddenStatus()):
                spell.displayMagicAttributes()

    else:
        print("Check complete! All spells are valid and hippo free.")
        print("Here is some info on the spells included:")
        for i in range(len(spellBook)):
            spellBook[i].displayMagicAttributes()
    return
