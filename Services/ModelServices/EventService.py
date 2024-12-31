from Models.Choice import Choice
from Models.Event import Event
from Models.Trait import Trait
import Services.ModelServices.CharacterService as smscs
import Configuration.EventsConfiguration as es
from Common.Constants import Modifiers as ccm

def display_event(event):
    print(event.name)
    print(event.description)
    for i in range(len(event.choices)):
        print(str(event.choices[i]))

def pick_a_choice(character,event):
    display_event(event)
    decision = input("Which option would your Majesty prefer?")
    for i, x in enumerate(event.choices):
        if decision == x.text:
            print(f"{x.text} selected!")
            handle_choice(character, event,i)
            break
    else:
        print("No such option")

def handle_choice(character, event, choice_ind):
    if event.choices[choice_ind].other_char is not None:
        character = event.choices[choice_ind].other_char
    for key,value in event.choices[choice_ind].consequences.items():
        if key in character.modifiers.keys():
            smscs.handle_modifiers(character, key, value)
        else:
            print(f"Lord we lack knowledge of: {key}")

def generate_events():
    """returns {event1:false},{event2:false},{event3:false}"""
    events = es.get_events()
    tukati_dukati = dict()
    for event in events:
        tukati_dukati[event] = False
    return tukati_dukati


ev = Event(name="The king's new clothes",
           description="The king's description",
           choices=[Choice(text='a',consequences= {"traits": Trait("Small Heroism",("army_morale",0.1), modif_flag=ccm.stats_strength)}, flag=ccm.traits), Choice(text="b", consequences={'army_morale':+0.3,"gold":-15}, flag=ccm.stats_strength)],
           meantime=3,
           chain=None
           )
