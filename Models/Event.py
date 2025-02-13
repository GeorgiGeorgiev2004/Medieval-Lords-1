import common.utility as cu


class Event:
    def __init__(self, name, description, choices, meantime=None, chain=None, affected_characters=[], available=True,
                 available_on_turn=-2, cooldown=2):
        self.name = name
        self.description = description
        self.choices = choices
        self.meantime = meantime
        self.chain = chain
        self.affected_characters = affected_characters
        self.available = available
        self.available_on_turn = available_on_turn
        self.cooldown = cooldown

    def __repr__(self):
        result = self.name + f"\n " + self.description
        for i, choice in enumerate(self.choices):
            result += f"\n" + cu.int_to_roman(i) + " " + str(choice)
        return result

    def __setattr__(self, key, value):
        if key == "available" and value is False:
            self.available_on_turn += self.cooldown
        super().__setattr__(key, value)
