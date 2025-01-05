from Common.Constants import GameEssentials as ge
from Services.ModelServices import CharacterService as cs
from Services.ModelServices import EventService as es
from Common.Constants import Text as t
from Services.ModelServices import TerritoryService as ts
turn = ge.TURN
game_state = {
    "turn":turn,
    "PLAYER_CHARACTER":ge.PLAYER_CHARACTER,
              }

def start_game():
    cmd = input(t.greet)
    if cmd == "1":
        result = cs.char_selector()
        if result == 1:
            play()
        pass
    if cmd == "2":
        pass
    if cmd == "3":
        pass
    if cmd == "4":
        return 0
    return 0

def play():
    events = es.get_events_no_cooldown(es.generate_events()) #Seems unsightly *level of abstraction*, maybe fix later
    cmd = "AAA"
    while cmd != "end":
        play_turn(events)
        ge.TURN = ge.TURN + 1
        cmd = input("what now?")

def play_turn(events):
    events_this_turn = es.select_events_for_turn(events)
    print()
    cmd = input(t.text_base1)
    while True:
        if cmd == "1":
            ans = es.handle_events(events_this_turn)
            pass
        if cmd == "2":
            ts.modify_terry()
            pass
        if cmd == "3":
            pass
        if cmd == "4":
            return 0
        if cmd == "stats":
            ge.PLAYER_CHARACTER.present_self()
        cmd = input(t.text_base1)

start_game()


