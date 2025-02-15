from os.path import commonpath
from models import territory

import common.constants as cc


class Character:
    def __init__(self, first_name, last_name, age, gender, family, title=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.family = family
        self.modifiers = dict()
        if self.gender == 'M':
            self.modifiers["honorifics"] = cc.DefaultValues.def_honorifics_M
        else:
            self.modifiers["honorifics"] = cc.DefaultValues.def_honorifics_F
        self.modifiers[cc.Modifiers.gold] = 0
        self.modifiers[cc.Modifiers.army_morale] = 1
        self.modifiers[cc.Modifiers.tax_income_mod] = 1
        self.modifiers[cc.Modifiers.title] = title
        self.modifiers[cc.Modifiers.traits] = set()
        self.modifiers[cc.Modifiers.stats] = {"administrative": 0, "strength": 0, "tactics": 0,
                                                            "infrastructural": 0, "knowledge": 0}
        self.modifiers[cc.Modifiers.upkeep_cost] = 1
        self.governed_territory = territory.Territory()

    def present_self(self):
        parents_names = " and ".join(
            [parent.first_name for parent in self.family.parents]) if self.family.parents else "Unknown"
        if not isinstance(self.family.kids, list):
            self.family.kids = [self.family.kids]
        kids_names = ", ".join([child.first_name for child in self.family.kids]) if self.family.kids else "Unknown"
        spouse_name = self.family.spouse.first_name if self.family.spouse else "Unknown"
        honorifics = self.modifiers.get("honorifics", cc.DefaultValues.def_honorifics_M)
        title = self.modifiers.get(cc.Modifiers.title, cc.DefaultValues.title)

        if title is None:
            partner_title = self.family.spouse.modifiers.get(cc.Modifiers.title,
                                                             cc.DefaultValues.title)
            self.modifiers[cc.Modifiers.title] = f"{honorifics[1]} of the {partner_title}"
            title = self.modifiers.get(cc.Modifiers.title, cc.DefaultValues.title)
        print(f"{self.first_name} {self.last_name}, {title} of {self.governed_territory}. "
              f"{honorifics[2]} of {parents_names}, "
              f"{honorifics[0]} of {kids_names}, "
              f"{honorifics[1]} of {spouse_name}.")
        for key, value in self.modifiers.items():
            print(str(key) + ": " + str(value))
