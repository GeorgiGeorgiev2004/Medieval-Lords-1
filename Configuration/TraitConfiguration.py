import Models.Trait as t

def generate_traits():
    return [t.Trait('Brave', ("army-morale",0.05)),
          t.Trait('Generous', ("tax_income_mod",-0.05)),
          t.Trait('Honorable', ("upkeep_cost",-0.07)),
          t.Trait('Great General Blessed by the Heavens', ("army-morale",0.15)),
          t.Trait('Greedy', ("tax_income_mod",0.10))]