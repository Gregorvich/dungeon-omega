import Sorcery_Functions

# Testing our SorceryFunctions module

# The below if statement is added in case we want to input
# arguments in the command line for testing the Sorcery function.
# So it's mainly added for convenience, since an alternative
# would be to manually edit this script. When command line
# arguments are used, the Main function expects the first
# argument to be a boolean, although if this is not the case
# it will type cast the argument to type "bool"
# if (__name__ == "__main__"):
#     import sys
#     includeForbiddenSpells = bool(sys.argv[1])
#     createSpells = Sorcery_Functions.createSpells
#     printSpellBook = Sorcery_Functions.printSpellBook

#    spellBook = createSpells(includeForbiddenSpells)
#    printSpellBook(spellBook)

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
