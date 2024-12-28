import Models.Trait as t
from Common.Constants import Modifiers as ccm
def generate_traits():
    return [t.Trait('Brave', ("army-morale",0.05), ccm.stats_strength),
          t.Trait('Generous', ("tax_income_mod",-0.05), ccm.stats_administrative),
          t.Trait('Honorable', ("upkeep_cost",-0.07), ccm.upkeep_cost),
          t.Trait('Great General Blessed by the Heavens', ("army-morale",0.15), ccm.stats_strength),
          t.Trait('Greedy', ("tax_income_mod",0.10), ccm.tax_income_mod)]