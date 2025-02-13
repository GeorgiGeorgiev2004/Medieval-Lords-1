import random
import configuration.events_configuration as es
import models.custom_error as mc
from services.model_services import choice_service as cs
from common.constants import GameEssentials as ge
from common.constants import Text as t


def display_event(event):
    print(event.name)
    print(event.description)
    for i in range(len(event.choices)):
        print(str(event.choices[i]))


def generate_events():
    return es.get_events()


def get_events_no_cooldown(events):
    return [e for e in events if e.available is not False]


def select_events_for_turn(events):
    all_available_events = get_events_no_cooldown(events)
    count = random.randint(1, 3)
    numbers = random.sample(range(len(all_available_events)), count)
    result = list()
    for i in range(count):
        result.append(all_available_events[numbers[i]])
        events[numbers[i]].available = False
    return result


def handle_events(events_this_turn):
    print(f"You still have to answer to {len(events_this_turn)} more requests.")
    cmd = input(t.text_base2)
    while cmd != "2":
        if len(events_this_turn) == 0:
            return 0
        if cmd == "1":
            event = events_this_turn[0]
            display_event(event)
            try:
                cs.pick_a_choice(ge.PLAYER_CHARACTER, event)
                events_this_turn.remove(events_this_turn[0])
            except mc.BadAnswerError as bae:
                print(bae._message)
        if cmd == "2":
            return 0
        if cmd == "stats":
            ge.PLAYER_CHARACTER.present_self()
        cmd = input(t.text_base2)
    return 1


def fix_events(events, turn):
    for event in events:
        if event.available_on_turn == turn:
            event.available = True
