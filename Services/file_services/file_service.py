import pickle
from common.constants import SavedGames


def save_game(game_state, filename):
    with open(filename, 'wb') as file:
        pickle.dump(game_state, file)
    print("Game saved!")


def load_game(filename):
    try:
        with open(filename, 'rb') as file:
            game_state = pickle.load(file)
            print("Game loaded!")
            return game_state
    except FileNotFoundError:
        print("No save file found.")
        return []


def generate_file_name():
    return "save_file-" + str(SavedGames.SAVED_GAMES)
