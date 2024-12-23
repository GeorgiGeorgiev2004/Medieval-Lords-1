import Configuration.CharacterConfiguration
from Common.Constants import Modifiers as m

def handle_modifiers(character, key, value):
    modif_type = type(character.modifiers[key])
    if key == m.stats:
        _handle_modifiers_stats(character, key, value)
    elif modif_type in [int, float]:
        _handle_modifiers_numerical(character, key, value)
    elif key == m.traits:
        _handle_modifiers_trait(character, value)
    elif key == m.title:
        _handle_modifiers_trait(character, value)

def _handle_modifiers_stats(character, key, value):
    character.modifiers[m.stats][key] += value
    print(character.modifiers[m.stats])

def _handle_modifiers_numerical(character, key, value):
    character.modifiers[key] += value

def _handle_modifiers_trait(character, value):
    ans = input(f"Did we gain or lose a trait? : Gain->Y, Lose -> N")
    if ans == "Y" or ans =="y":
        if value in character.modifiers[m.traits]:
            print("This trait is already active.")
        else:
            character.modifiers[m.traits].add(value)
            print(character.modifiers[m.traits])
    elif ans == "N" or ans =="n":
        if value in character.modifiers[m.traits]:
            character.modifiers[m.traits].remove(value)
        else:
            print("There is no trait to remove.")

def _handle_modifiers_title(character, key, value):
    character.modifiers[key] = value

def display_stats(character, key):
    tags = {}
    for k, v in character.modifiers[m.stats].items():
        tag = k[:3].upper()
        tags[tag] = k
    print(character.modifiers[m.stats])

def calculate_modifiers(character):
    temp_morale = character.modifiers[m.army_morale]
    character.modifiers[m.army_morale] = 1