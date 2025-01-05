class Screen:
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 650

class Scaling:
    CHARACTER_SCALING = 0.3
    TILE_SCALING = 0.5

class Button:
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 50
    BUTTON_SPACING = 20

class CharacterCreator:
    BUTTON_WIDTH = (Screen.SCREEN_WIDTH / 5) * 2
    BUTTON_HEIGHT = (Screen.SCREEN_HEIGHT / 5) * 4

class DefaultValues:
    def_honorifics_M = ["Father", "Husband", "Son"]
    def_honorifics_F = ["Mother", "Wife", "Daughter"]
    title = "Sovereign"

class Modifiers:
    army_morale = "army_morale"
    tax_income_mod = "tax_income_mod"
    title = "title"
    traits = "traits"
    stats = "stats"
    upkeep_cost = "upkeep_cost"
    gold = "gold"
    stats_administrative = "administrative"
    stats_strength = "strength"
    stats_tactics = "tactics"
    stats_infrastructural = "infrastructural"
    stats_knowledge = "knowledge"

class GameEssentials:
    PLAYER_CHARACTER = None
    TURN=0

class SavedGames:
    from pathlib import Path
    FOLDER_PATH_STR = "E:\PythonProject\Medieval-Lords-1\Resources\Files\SaveFiles\\"
    FOLDER_PATH = Path(FOLDER_PATH_STR)
    SAVED_GAMES = len([f for f in FOLDER_PATH.iterdir() if f.is_file()])

class CityAlgorithm:
    START = 1
    GROWTH_RATE = 0.5

class Text:
    greet ="""
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
    modify_city_how = """
The commands to use are :
build
destroy
"""