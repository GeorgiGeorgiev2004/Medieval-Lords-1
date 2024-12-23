from Models.Choice import Choice
from Models.Event import Event
from Models.Trait import Trait
import Services.ModelServices.CharacterService as smscs
import Configuration.CharacterArchetypes

def display_event(event):
    print(event.description)
    for i in range(len(event.choices)):
        print(event.choices[i])

def pick_a_choice(character,event):
    display_event(event)
    decision = input("Which option would your Majesty prefer?")
    for i, x in enumerate(event.choices):
        if decision is x.text:
            print(f"{decision} selected!")
            handle_choice(character, event,i)
            break
    else:
        print("No such option")

def handle_choice(character, event, choice_ind):
    for key,value in event.choices[choice_ind].consequences.items():
        if key in character.modifiers.keys():
            smscs.handle_modifiers(character, key, value)
        else:
            print(f"Lord we lack knowledge of: {key}")


ev = Event(name="The king's new clothes",
           description="The king's description",
           choices=[Choice(text='a',consequences= {"traits": Trait("Tr",("army_morale",0.1))}), Choice(text="b",consequences={'army_morale':+0.3,"gold":-15})],
           meantime=3,
           chain=None
           )

chr = Configuration.CharacterArchetypes.generateFighter()
(pick_a_choice(chr, ev))
