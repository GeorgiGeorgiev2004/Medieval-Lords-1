class Family:
    def __init__(self, spouse=None, kids=None, parents=None):
        self.spouse = spouse
        self.kids = kids if kids is not None else []
        self.parents = parents if parents is not None else []
        self.heir = None

    def set_heir(self):
        if self.kids is not None:
            self.heir = self.kids[0]