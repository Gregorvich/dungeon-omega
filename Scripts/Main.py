import Sorcery_Functions
import Sorcery_Helper_Functions
from Spellbook import Spellbook

# Testing our SorceryFunctions module

# A function used for testing the Sorcery_Functions
# module
def testSorceries():
    createSpells = Sorcery_Helper_Functions.createSpells
    
    print("Testing a spell book that does not contain")
    print("Forbidden Spells")
    normalSpellbook = Spellbook("Friendly Spellbook")
    listOfMagicalSpells1 = createSpells(False, False)
    for magicalSpell in listOfMagicalSpells1:
        normalSpellbook.addMagic(magicalSpell)
    normalSpellbook.printSpellBook()
    print()
    
    print("Testing a spell book that contains forbidden spells")
    print("but NOT the infamous hippopotamus spell")
    listOfMagicalSpells2 = createSpells(True, False)
    evilSpellbook = Spellbook("Evil Spellbook", listOfMagicalSpells2)
    evilSpellbook.printSpellBook()
    print()
    
    print("Testing a spell book that contains the dreaded and")
    print("spooky hippopotamus spell, but not any other kind of")
    print("forbidden spell")
    listOfMagicalSpells3 = createSpells(False, True)
    overpoweredSpellbook = Spellbook("Overpowered Spellbook", listOfMagicalSpells3)
    overpoweredSpellbook.printSpellBook()
    print()

    print("Testing a spell book that contains some forbidden spells")
    print("and the hippopotamus spell")
    listOfMagicalSpells4 = createSpells(True, True)
    reallyOverpoweredSpellbook = Spellbook("Really Overpowered Spellbook", listOfMagicalSpells4)
    reallyOverpoweredSpellbook.printSpellBook()
    print()

    return

# TestSpellBook is a function used for testing the different
# methods and properties of the Spellbook class
def testSpellbook():
    mySpellbook = Spellbook("Beginner's Guide to Pyromancy")
    mySpellbook.printSpellBook()
    print()
    magicList1 = Sorcery_Helper_Functions.createSpells(0, 0)
    magicList2 = Sorcery_Helper_Functions.createSpells(1, 0)
    magicList3 = Sorcery_Helper_Functions.createSpells(0, 1)
    magicList4 = Sorcery_Helper_Functions.createSpells(1, 1)

    for magicSpell in magicList1:
        mySpellbook.addMagic(magicSpell)

    print("Testing retrieving a sorcery from a Spellbook by name.")
    fireball = mySpellbook.getMagicByName("Fireball")
    fireball.displayMagicAttributes()
    print()
    print("Testing retrieving a sorcery from a Spellbook using")
    print("the sorcery's index.")
    iceStorm = mySpellbook.getMagicByIndex(1)
    iceStorm.displayMagicAttributes()

    print("Testing the printSpellBook() method.")
    mySpellbook.printSpellBook()
    print()
    print("Testing the case where we attempt to remove a nonexistant sorcery")
    print("from the Spellbook.")
    mySpellbook.removeMagic("Arcane Shield")
    mySpellbook.removeMagic("Conjure Sword")
    print("Testing removing the spell Arcane Shield from the Spellbook.")
    mySpellbook.printSpellBook()
    print()

    print("Testing adding a new sorcery to the Spellbook called Ice Wave.")
    iceWave = Sorcery_Functions.Sorcery("Ice Wave", 32, "Frost", False)
    duplicateFireball = Sorcery_Functions.Sorcery("Fireball", 150, "Fire", False)
    mySpellbook.addMagic(iceWave)
    mySpellbook.printSpellBook()
    print()
    print("Testing adding another sorcery called Fireball to the Spellbook")
    mySpellbook.addMagic(duplicateFireball)
    print()

    mySpellbook2 = Spellbook("Spooky Spellbook", magicList2)
    mySpellbook3 = Spellbook("Hippo Spellbook", magicList3)
    mySpellbook4 = Spellbook("Catastrophic Spellbook", magicList4)
    print("Testing the printSpellbook() method using different lists")
    print("of sorceries")
    mySpellbook2.printSpellBook()
    print()
    mySpellbook3.printSpellBook()
    print()
    mySpellbook4.printSpellBook()
    print()
    print("Retrieving the size of Beginner's Guide to Pyromancy and")
    print("Catastrophic Spellbook.")
    print("Size of Spellbook 1: " + str(mySpellbook.getSize()))
    print("Size of Spellbook 4: " + str(mySpellbook4.getSize()))
# Calling our testSorceries function
# testSorceries()

testSpellbook()