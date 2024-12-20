class Character:
    def __init__(self, first_name, last_name, age, gender, family, stats=None, title=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.stats = stats
        self.family = family
        self.title = title

    def present_self(self):
        honorifics = ["Father", "Husband", "Son"] if self.gender == "M" else ["Mother", "Wife", "Daughter"]
        parents_names = ", ".join([parent.first_name for parent in self.family.parents]) if self.family.parents else "Unknown"
        kids_names = ", ".join([child.first_name for child in self.family.kids]) if self.family.kids else "Unknown"
        spouse_name = self.family.spouce.first_name if self.family.spouce else "Unknown"
        if self.title is None:
            self.title = f"{honorifics[1]} of the {self.family.spouce.title}"
        print(f"{self.first_name} {self.last_name}, {self.title} of Conqueradia."
                f"{honorifics[2]} of {parents_names}. "
                f"{honorifics[0]} of {kids_names}. "
                f"{honorifics[1]} of {spouse_name}.")