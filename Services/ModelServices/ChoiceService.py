import Services.ModelServices.CharacterService as smscs
import Models.CustomError as mc

def handle_choice(character, event, choice_ind):
    if event.choices[choice_ind].other_char is not None:
        character = event.choices[choice_ind].other_char
    for key,value in event.choices[choice_ind].consequences.items():
        if key in character.modifiers.keys():
            smscs.handle_modifiers(character, key, value)
        else:
            print(f"Lord we lack knowledge of: {key}")


def pick_a_choice(character,event):
    decision = input("Which option would your Majesty prefer?")
    for i, x in enumerate(event.choices):
        if decision == x.text:
            print(f"{x.text} selected!")
            handle_choice(character, event,i)
            break
    else:
        raise mc.BadAnswerError
