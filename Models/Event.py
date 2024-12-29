import Common.Utility as cu

class Event:
    def __init__(self, name, description, choices, meantime=None, chain=None, affected_characters=None):
        self.name = name
        self.description = description
        self.choices = choices
        self.meantime = meantime
        self.chain = chain
        self.affected_characters = []

    def __repr__(self):
        result =  self.name+f"\n "+self.description
        for i, choice in enumerate(self.choices):
            result += f"\n" + cu.int_to_roman(i) + " " + str(choice)
        return result

