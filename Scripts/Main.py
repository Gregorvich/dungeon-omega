import Sorcery_Functions

# Testing our SorceryFunctions module

# A function used for testing the Sorcery_Functions
# module
def testSorceries():
    createSpells = Sorcery_Functions.createSpells
    printSpellBook = Sorcery_Functions.printSpellBook
    
    print("Testing a spell book that does not contain")
    print("Forbidden Spells")
    normalSpellBook = createSpells(False, False)
    printSpellBook(normalSpellBook)
    print()
    
    print("Testing a spell book that contains forbidden spells")
    print("but NOT the infamous hippopotamus spell")
    evilSpellBook = createSpells(True, False)
    printSpellBook(evilSpellBook)
    print()
    
    print("Testing a spell book that contains the dreaded and")
    print("spooky hippopotamus spell, but not any other kind of")
    print("forbidden spell")
    overpoweredSpellBook = createSpells(False, True)
    printSpellBook(overpoweredSpellBook)
    print()

    print("Testing a spell book that contains some forbidden spells")
    print("and the hippopotamus spell")
    reallyOverpoweredSpellBook = createSpells(True, True)
    printSpellBook(reallyOverpoweredSpellBook)
    print()

    return

# Calling our testSorceries function
testSorceries()