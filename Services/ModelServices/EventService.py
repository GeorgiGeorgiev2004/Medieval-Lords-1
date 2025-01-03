import random
from Models.Choice import Choice
from Models.Event import Event
from Models.Trait import Trait
import Services.ModelServices.CharacterService as smscs
import Configuration.EventsConfiguration as es
from Common.Constants import Modifiers as ccm
import Models.CustomError as mc

def display_event(event):
    print(event.name)
    print(event.description)
    for i in range(len(event.choices)):
        print(str(event.choices[i]))

def pick_a_choice(character,event):
    decision = input("Which option would your Majesty prefer?")
    for i, x in enumerate(event.choices):
        if decision == x.text:
            print(f"{x.text} selected!")
            handle_choice(character, event,i)
            break
    else:
        raise mc.BadAnswerError


def handle_choice(character, event, choice_ind):
    if event.choices[choice_ind].other_char is not None:
        character = event.choices[choice_ind].other_char
    for key,value in event.choices[choice_ind].consequences.items():
        if key in character.modifiers.keys():
            smscs.handle_modifiers(character, key, value)
        else:
            print(f"Lord we lack knowledge of: {key}")

def generate_events():
    return es.get_events()

def get_events_no_cooldown(events):
    return [e for e in events if e.available is not False]

def select_events_for_turn(events):
    all_available_events = get_events_no_cooldown(events)
    count =  random.randint(1, 3)
    numbers = random.sample(range(len(all_available_events)), count)
    result = list()
    for i in range(count):
        result.append(all_available_events[numbers[i]])
        events[numbers[i]].available = False
    return result

ev = Event(name="The king's new clothes",
           description="The king's description",
           choices=[Choice(text='a',consequences= {"traits": Trait("Small Heroism",("army_morale",0.1), modif_flag=ccm.stats_strength)}, flag=ccm.traits), Choice(text="b", consequences={'army_morale':+0.3,"gold":-15}, flag=ccm.stats_strength)],
           meantime=3,
           chain=None
           )


