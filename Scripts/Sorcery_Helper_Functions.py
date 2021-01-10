from Sorcery_Functions import Sorcery

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