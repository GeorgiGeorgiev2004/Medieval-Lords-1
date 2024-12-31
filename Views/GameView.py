from Common.Constants import GameEssentials as ge
from Services.ModelServices import CharacterService as cs
from Services.ModelServices import EventService as es
greet = """
Fancy seeing you here future lord!
What would you like to do now?
1) New Game
2) Settings
3) Saved Games
4) Exit
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
def play_turn():

    pass

def play():
    events = es.generate_events()

    play_turn()
    ge.TURN = ge.TURN + 1
    pass

start_game()


