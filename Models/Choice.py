import random


class Choice:
    def __init__(self, text, consequences, flag, func_to_handle=None, other_char=None):
        self.text = text
        self.consequences = consequences
        self.flag = flag
        self.func_to_handle = func_to_handle
        self.other_char = other_char
        self.cons_textified = ""
        if isinstance(consequences, list):
            mutability_gets_me_going = [""]
            self.consequences = chance_the_choice(consequences, mutability_gets_me_going)
            self.cons_textified = mutability_gets_me_going[0]

        else:
            self.consequences = consequences
            self.cons_textified = ", ".join(f"{flag} with this -> {value}" for flag, value in self.consequences.items())

    def __repr__(self):
        person_name = "your"
        if self.other_char is not None:
            person_name = str(self.other_char.first_name) + "\'s"
        return (f"{self.text} : with the consequences of affecting {person_name} \n" + self.cons_textified)


def chance_the_choice(options, field):
    """Takes [(conseq,chance),(conseq,chance),(conseq,chance),...]"""
    arr = list()
    for cons, chance in options:
        temp = ", ".join(f"{flag} with this -> {value}" for flag, value in cons.items())
        arr.append(temp)
    field[0] = field[0] + " or \n".join(arr)
    zto = random.random()
    sum = 0
    for conseq, chance in options:
        sum += chance
        if zto < sum:
            return conseq
    else:
        print("Genuinely lost")
