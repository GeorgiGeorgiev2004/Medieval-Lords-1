def Event():
    def __init__(self, name, description, choices_and_chances, meantime, chain):
        self.name = name
        self.description = description
        self.choices_perc = choices_and_chances
        self.meantime = meantime
        self.chain = chain