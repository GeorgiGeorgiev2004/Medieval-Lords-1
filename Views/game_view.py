from common.constants import GameEssentials as ge
from services.model_services import character_service as cs
from services.model_services import event_service as es
from common.constants import Text as t
from common.constants import SavedGames as sg
from services.model_services import territory_service as ts
from services.file_services import file_service as fs
import sys

turn = ge.TURN
game_state = {
    "turn": turn,
    "PLAYER_CHARACTER": ge.PLAYER_CHARACTER,
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
        files = list(sg.FOLDER_PATH.iterdir())

        file_list = [f.name for f in files if f.is_file()]
        for f in file_list:
            print(f)
        cmd = input("Which savefile would you like to load up?")
        game_state = fs.load_game(sg.FOLDER_PATH_STR + "\\" + cmd)
    if cmd == "4":
        return 0
    return 0


def play():
    cmd = "AAA"
    while cmd != "end":
        events = es.get_events_no_cooldown(es.generate_events())
        play_turn(events)
        es.fix_events(events, turn)
        game_state["events"] = events
        ge.TURN = ge.TURN + 1

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
            return 0
        if cmd == "4":
            fs.save_game(game_state, sg.FOLDER_PATH + fs.generate_file_name())
            sys.exit()
        if cmd == "stats":
            ge.PLAYER_CHARACTER.present_self()
        cmd = input(t.text_base1)


start_game()
