from os.path import commonpath
import Common.Constants

class Character:
    def __init__(self, first_name, last_name, age, gender, family, title=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.family = family
        self.modifiers = dict()
        if self.gender == 'M':
           self.modifiers["honorifics"] = Common.Constants.DefaultValues.def_honorifics_M
        else:
            self.modifiers["honorifics"] = Common.Constants.DefaultValues.def_honorifics_F
        self.modifiers["gold"] = 0
        self.modifiers["army_morale"] = 1
        self.modifiers["tax_income_mod"] = 1
        self.modifiers["title"] = title
        self.modifiers["traits"] = set()
        self.modifiers["stats"] = {"administrative":0, "strength":0, "tactics":0, "infrastructural": 0, "knowledge":0}
        self.modifiers["army_morale"] = 1
        self.modifiers["upkeep_cost"] = 1

    def present_self(self):
        parents_names = ", ".join(
            [parent.first_name for parent in self.family.parents]) if self.family.parents else "Unknown"
        kids_names = ", ".join([child.first_name for child in self.family.kids]) if self.family.kids else "Unknown"
        spouse_name = self.family.spouce.first_name if self.family.spouce else "Unknown"
        honorifics = self.modifiers.get("honorifics", Common.Constants.DefaultValues.def_honorifics_M)
        title = self.modifiers.get("title", Common.Constants.DefaultValues.title)

        if title is None:
            partner_title = self.family.spouce.modifiers.get("title", Common.Constants.DefaultValues.title)
            self.modifiers["title"] = f"{honorifics[1]} of the {partner_title}"
            title = self.modifiers.get("title", Common.Constants.DefaultValues.title)
        print(f"{self.first_name} {self.last_name}, {title} of Conqueradia. "
              f"{honorifics[2]} of {parents_names} "
              f"{honorifics[0]} of {kids_names} "
              f"{honorifics[1]} of {spouse_name} ")


