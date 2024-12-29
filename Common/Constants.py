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