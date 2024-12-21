from Models.Family import Family
from Models.Character import Character


def generateFighter():
    Viktor = Character(first_name="Viktor",
                       last_name="Victor",
                       age=29,
                       gender="M",
                       stats={4, 9},
                       family=Family(),
                       title="Emperor")
    spouce = Character(first_name="Ivana",
                       last_name="Manolova",
                       age=22,
                       gender="F",
                       family=Family(kids={}, parents={})
                       )
    Viktor.family.spouce = spouce
    spouce.family.spouce = Viktor
    return Viktor


char = generateFighter()

char.present_self()
char.family.spouce.present_self()
