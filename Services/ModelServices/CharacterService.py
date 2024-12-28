import Configuration.CharacterConfiguration
from Common.Constants import Modifiers as ccm

def handle_modifiers(character, key, value):
    modif_type = type(character.modifiers[key])
    if key == ccm.stats:
        _handle_modifiers_stats(character, key, value)
    elif modif_type in [int, float]:
        _handle_modifiers_numerical(character, key, value)
    elif key == ccm.traits:
        _handle_modifiers_trait(character, value)
    elif key == ccm.title:
        _handle_modifiers_trait(character, value)

def _handle_modifiers_stats(character, key, value):
    character.modifiers[ccm.stats][key] += value
    print(character.modifiers[ccm.stats])

def _handle_modifiers_numerical(character, key, value):
    character.modifiers[key] += value

def _handle_modifiers_trait(character, value):
    ans = input(f"Did we gain or lose a trait? : Gain->Y, Lose -> N")
    if ans == "Y" or ans =="y":
        if value in character.modifiers[ccm.traits]:
            print("This trait is already active.")
        else:
            character.modifiers[ccm.traits].add(value)
            print(character.modifiers[ccm.traits])
    elif ans == "N" or ans =="n":
        if value in character.modifiers[ccm.traits]:
            character.modifiers[ccm.traits].remove(value)
        else:
            print("There is no trait to remove.")

def _handle_modifiers_title(character, key, value):
    character.modifiers[key] = value

def display_stats(character):
    tags = {}
    for k, v in character.modifiers[ccm.stats].items():
        tag = k[:3].upper()
        tags[tag] = k
    print(character.modifiers[ccm.stats])

def calculate_modifiers(character):
    character.modifiers[ccm.army_morale] = calc_morale(character)
    character.modifiers[ccm.tax_income_mod] = calc_tax_mod(character)
    character.modifiers[ccm.upkeep_cost] = calc_upkeep(character)
    
def calc_morale(character):
    temp_morale = character.modifiers[ccm.army_morale]
    temp_morale += 0.025 * character.modifiers[ccm.stats][ccm.stats_strength]
    temp_morale += sum([trait.modifier_value[1] for trait in character.modifiers[ccm.traits] if
         trait.modif_flag is ccm.stats_strength])
    return temp_morale

def calc_tax_mod(character):
    temp_adm = character.modifiers[ccm.tax_income_mod]
    temp_adm += 0.015 * character.modifiers[ccm.stats][ccm.stats_administrative]
    temp_adm += sum([trait.modifier_value[1] for trait in character.modifiers[ccm.traits] if
         trait.modif_flag is ccm.stats_administrative])
    return temp_adm

def calc_upkeep(character):
    temp_upk = character.modifiers[ccm.upkeep_cost]
    temp_upk += 0.015 * character.modifiers[ccm.stats][ccm.stats_tactics]
    temp_upk += sum([trait.modifier_value[1] for trait in character.modifiers[ccm.traits] if
         trait.modif_flag is ccm.stats_tactics])
    return temp_upk