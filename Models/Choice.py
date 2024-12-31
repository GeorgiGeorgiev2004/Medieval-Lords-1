import random

class Choice:
    def __init__(self, text, consequences, flag, func_to_handle=None, other_char=None):
        self.text = text
        self.consequences = consequences
        self.flag = flag
        self.func_to_handle = func_to_handle
        self.other_char = other_char

    def __repr__(self):
        return f"{self.text} : with the consequences of maybe affecting your " + ", ".join(f"{flag} with this -> {value}" for flag, value in self.consequences.items())

def chance_the_choice(options):
        """Takes [(conseq,chance),(conseq,chance),(conseq,chance),...]"""
        zto = random.random()
        sum = 0
        for conseq, chance in options:
            sum += chance
            if zto < sum:
                return conseq
        else:
            print("Genuinely lost")