from Common.Constants import GameEssentials as ge

greet = """
Fancy seeing you here future lord!
What would you like to do now?
1) New Game
2) Settings
3) Saved Games
4) Exit
"""

def play():
    cmd = input(greet)
    while cmd != "end":
        if cmd == "1":
            pass
        if cmd == "2":
            pass
        if cmd == "3":
            pass
        if cmd == "4":
            return 0
        cmd = input(greet)

play()