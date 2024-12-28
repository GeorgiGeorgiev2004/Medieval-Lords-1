from Models.Family import Family
from Models.Character import Character
from Common.Constants import Modifiers as md

def generateFighter():
    Viktor = Character(first_name="Viktor",
                       last_name="Victor",
                       age=29,
                       gender="M",
                       family=Family(),
                       title="Emperor")
    spouse = Character(first_name="Ivana",
                       last_name="Manolova",
                       age=22,
                       gender="F",
                       family=Family(kids={}, parents={})
                       )
    Viktor.family.spouse = spouse
    spouse.family.spouse = Viktor

    Viktor.modifiers[md.gold] = 100
    Viktor.modifiers[md.army_morale] = 1
    Viktor.modifiers[md.tax_income_mod] = 1
    Viktor.modifiers[md.traits] = set()
    Viktor.modifiers[md.stats] = {"administrative": 0, "strength": 0, "tactics": 0, "infrastructural": 0, "knowledge": 0}
    Viktor.modifiers[md.upkeep_cost] = 1

    return Viktor