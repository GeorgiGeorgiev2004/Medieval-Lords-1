from Common.Constants import GameEssentials as ge
from Services.ModelServices import CharacterService as cs
from Services.ModelServices import EventService as es
import Models.CustomError as mc
greet = """
Fancy seeing you here future lord!
What would you like to do now?
1) New Game
2) Settings
3) Saved Games
4) Exit
"""
text_base1 = """
As it stands lord, you can choose your next activity:
1) See to the visitor's demands
2) View your territory
3) Next turn!
4) Save and Exit
"""
text_base2 = """
Would you like to answer the next person or switch your focus for now?
1) See to the visitor's demands
2) Go back!
"""
turn = ge.TURN
game_state = {
    "turn":turn,
    "PLAYER_CHARACTER":ge.PLAYER_CHARACTER,
              }
def start_game():
    cmd = input(greet)
    if cmd == "1":
        char_selector()
        pass
    if cmd == "2":
        pass
    if cmd == "3":
        pass
    if cmd == "4":
        return 0
    return 0

def char_selector():
    chars = cs.generate_heroes()
    for i in range(len(chars)):
        print(chars[i].present_self())
    decision = input("Which character would you like?")
    for i, x in enumerate(chars):
        if decision == x.first_name:
            ge.PLAYER_CHARACTER = x
            print(f"{x.first_name} selected!")
            play()
            return 0
    else:
        print("Opsa broski try again maybe?")


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
    cmd = input(text_base1)
    while True:
        if cmd == "1":
            ans = handle_events(events_this_turn)
            pass
        if cmd == "2":
            pass
        if cmd == "3":
            pass
        if cmd == "4":
            return 0
        cmd=input(text_base1)

def handle_events(events_this_turn):
    print(f"You still have to answer to {len(events_this_turn)} more requests.")
    cmd = input(text_base2)
    while cmd!= "2":
        if len(events_this_turn) ==0:
            return 0
        if cmd == "1":
            event = events_this_turn[0]
            es.display_event(event)
            try:
                es.pick_a_choice(ge.PLAYER_CHARACTER, event)
                events_this_turn.remove(events_this_turn[0])
            except mc.BadAnswerError as bae:
                print(bae._message)
        if cmd == "2":
            return 0
        cmd = input(text_base2)
    return 1

start_game()


