from tempfile import SpooledTemporaryFile

from Models.Family import Family
from Models.Character import Character
from Common.Constants import Modifiers as md

#region Papadopolu
Papadopolu = Character(first_name="Papadopolu",
                   last_name="Kirlipopodopolus",
                   age=55,
                   gender="M",
                   family=Family(),
                   title="Emperor")
Asta = Character(first_name="Asta",
                   last_name="Kirlipopodopolus",
                   age=45,
                   gender="F",
                   family=Family()
                   )
Papadopolu.family.spouse = Asta
Asta.family.spouse = Papadopolu

Simona = Character(first_name="Simona",
                   last_name="Kirlipopodopolus",
                   age=12,
                   gender="F",
                   family=Family(parents=[Papadopolu,Asta])
                   )
Papadopolu.family.kids.append(Simona)
Asta.family.kids.append(Simona)

Papadopolu.modifiers[md.gold] = 300
Papadopolu.modifiers[md.army_morale] = 2.7
Papadopolu.modifiers[md.tax_income_mod] = 3.2
Papadopolu.modifiers[md.traits] = set()
Papadopolu.modifiers[md.stats] = {"administrative": 3, "strength": 3, "tactics": 4, "infrastructural": 5, "knowledge": 6}
Papadopolu.modifiers[md.upkeep_cost] = 0.7

#endregion


def generateFighter():
    Viktor = Character(first_name="Viktor",
                       last_name="Victor",
                       age=29,
                       gender="M",
                       family=Family(),
                       title="Emperor")
    spouse = Character(first_name="Ivana",
                       last_name="Manolova",
                       age=24,
                       gender="F",
                       family=Family()
                       )
    Viktor.family.spouse = spouse
    spouse.family.spouse = Viktor

    child = Character(first_name="Milen",
                       last_name="Cvetkov",
                       age=6,
                       title="Heir",
                       gender="M",
                       family=Family(kids={}, parents={Viktor,spouse})
                       )
    Viktor.family.spouse = spouse
    spouse.family.spouse = Viktor

    Viktor.modifiers[md.gold] = 80
    Viktor.modifiers[md.army_morale] = 1.2
    Viktor.modifiers[md.tax_income_mod] = 0.7
    Viktor.modifiers[md.traits] = set()
    Viktor.modifiers[md.stats] = {"administrative": 2, "strength": 6, "tactics": 4, "infrastructural": 2, "knowledge": 1}
    Viktor.modifiers[md.upkeep_cost] = 1

    return Viktor

def generateAdministrator():
    smort = Character(first_name="Thinker",
                       last_name="Smartovich",
                       age=33,
                       gender="M",
                       family=Family(),
                       title="Duke")
    spouse = Simona
    smort.family.spouse = spouse
    spouse.family.spouse = smort

    smort.modifiers[md.gold] = 170
    smort.modifiers[md.army_morale] = 0.7
    smort.modifiers[md.tax_income_mod] = 1.2
    smort.modifiers[md.traits] = set()
    smort.modifiers[md.stats] = {"administrative": 6, "strength": 1, "tactics": 2, "infrastructural": 4, "knowledge": 3}
    smort.modifiers[md.upkeep_cost] = 0.8

    return smort

ch = generateAdministrator()
ch.present_self()
pap = ch.family.spouse
pap.present_self()