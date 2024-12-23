import Common.Constants

class Character:
    def __init__(self, first_name, last_name, age, gender, family, title=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.family = family
        self.title = title
        self.modifiers = dict()
        if self.gender == 'M':
           self.modifiers["honorifics"] = ["Father", "Husband", "Son"]
        else:
            self.modifiers["honorifics"] = ["Mother", "Wife", "Daughter"]
        self.modifiers["gold"] = 0
        self.modifiers["army_morale"] = 1
        self.modifiers["tax_income_mod"] = 1

    def present_self(self):
        parents_names = ", ".join(
            [parent.first_name for parent in self.family.parents]) if self.family.parents else "Unknown"
        kids_names = ", ".join([child.first_name for child in self.family.kids]) if self.family.kids else "Unknown"
        spouse_name = self.family.spouce.first_name if self.family.spouce else "Unknown"

        honorifics = self.modifiers.get("honorifics", Common.Constants.DefaultValues.def_honorifics)

        if self.title is None:
            self.title = f"{honorifics[1]} of the {self.family.spouce.title}"
        print(f"{self.first_name} {self.last_name}, {self.title} of Conqueradia. "
              f"{honorifics[2]} of {parents_names} "
              f"{honorifics[0]} of {kids_names} "
              f"{honorifics[1]} of {spouse_name} ")


