import Configuration.CharacterArchetypes


def handle_modifiers(character, key, value):
    modif_type = type(character.modifiers[key])
    if key == "stats":
        _handle_modifiers_stats(character, key, value)
    if modif_type in [int, float]:
        _handle_modifiers_numerical(character, key, value)
    elif key == "traits":
        _handle_modifiers_trait(character, value)


def _handle_modifiers_stats(character, key, value):
    character.modifiers["stats"][key] += value
    print(character.modifiers["stats"])

def _handle_modifiers_numerical(character, key, value):
    character.modifiers[key] += value

def _handle_modifiers_trait(character, value):
    ans = input(f"Did we gain or lose a trait? : Gain->Y, Lose -> N")
    if ans == "Y" or ans =="y":
        if value in character.modifiers["traits"]:
            print("This trait is already active.")
        else:
            character.modifiers["traits"].add(value)
            print(character.modifiers["traits"])
    elif ans == "N" or ans =="n":
        if value in character.modifiers["traits"]:
            character.modifiers["traits"].remove(value)
        else:
            print("There is no trait to remove.")

def display_stats(character, key):
    tags = {}
    for k, v in character.modifiers["stats"].items():
        tag = k[:3].upper()
        tags[tag] = k
    print(character.modifiers["stats"])


chr = Configuration.CharacterArchetypes.generateFighter()

display_stats(chr,'strength')