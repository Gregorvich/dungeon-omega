from Sorcery_Functions import Sorcery

class Spellbook:
    "Common base class for a book of magic spells"
    spellbookCount = 1

    def __init__(self, name = None, storage = None):
        # If no name is specified, the default name will be Spellbook i,
        # where i is the number of spellbooks that have been created
        if (name is None):
            self.name = "Spellbook " + str(Spellbook.spellbookCount)
        else:
            self.name = name
        if (storage is None):
            self.storage = []
        else:
            self.storage = storage
        Spellbook.spellbookCount += 1

    def displayCount(self):
        print("Total number of Spellbooks: " + str(Spellbook.spellbookCount))

    def getName(self):
        return self.name

    def getSize(self):
        return len(self.storage)

    def addMagic(self, magicSpell):
        if not (isinstance(magicSpell, Sorcery)):
            print("Error: only magical spells of type Sorcery are" \
            " allowed in magic spellbooks")
            return
        for magicSpell2 in self.storage:
            if (magicSpell2.getName() == magicSpell.getName()):
                print("Error: a magic spell with the same name already" \
                " exists in this Spellbook")
                return
        self.storage.append(magicSpell)
        
    def removeMagic(self, magicalSpellName):
        elementLocation = -1
        for i in range(len(self.storage)):
            magicSpell = self.storage[i]
            if (magicSpell.getName() == magicalSpellName):
                elementLocation = i
                self.storage.pop(elementLocation)
        if (elementLocation == -1):
            print("Error: No such magical spell was found in the Spellbook")

    def getMagicByName(self, magicalSpellName):
        for magicalSpell in self.storage:
            if (magicalSpell.getName() == magicalSpellName):
                return magicalSpell
        print("Error: Unable to locate the magical spell specified.")
        return -1

    def getMagicByIndex(self, magicalSpellIndex):
        if (magicalSpellIndex >= len(self.storage)):
            print("Error: Index out of range")
            return -1
        return self.storage[magicalSpellIndex]

    # The printSpellBook function will print a list of the spells
    # that are in the Spellbook. It will not print the list if
    # the size of the Spellbook is 0. Additionally, the type of
    # output printed will vary depending on whether the Spellbook
    # contains forbidden spells
    def printSpellBook(self):
        hippoSpellName = "Summon Hippopotamus"
        hippoFlag = False
        forbiddenSpellFlag = False
        hippoSpellLocation = None

        if (len(self.storage) <= 0):
            print("The Spellbook is currently empty;")
            print("Please add some spells if you are wanting to print them.")
            return

        print("Checking to see if all spells in the Spellbook are valid...")
        for i in range(len(self.storage)):
            if ((self.storage[i].getName() == hippoSpellName) and self.storage[i].getForbiddenStatus()):
                hippoFlag = True
                hippoSpellLocation = i
                break
            elif(self.storage[i].getForbiddenStatus()):
                forbiddenSpellFlag = True

        self.displayCount()
        if (hippoFlag):
            print("The hippopotamus spell is too powerful. It ")
            print("should not be added to the Spellbook! ")
            print("Here's some info on it anyway: ")
            # The variable hippoSpellLocation should have been initialized
            # before it is used since, after setting the hippoFlag variable
            # to True, we immediately initialize it to a numerical value,
            # and additionally this is the only location it is used. We will
            # still check anyway however just to be safe.
            if (hippoSpellLocation is not None):
                self.getMagicByIndex(hippoSpellLocation).displayMagicAttributes()
            else:
                print("Error: the variable hippoSpellLocation was never set.")

        elif(forbiddenSpellFlag):
            print("Caution: At least one forbidden spell was found.")
            print("Here is a complete list of the forbidden spells")
            print("found in the spell book:")
            for magicSpell in self.storage:
                if (magicSpell.getForbiddenStatus()):
                    magicSpell.displayMagicAttributes()

        else:
            print("Check complete! All spells are valid and hippo free.")
            print("Here is some info on the spells included:")
            for spellBook in self.storage:
                spellBook.displayMagicAttributes()
        return