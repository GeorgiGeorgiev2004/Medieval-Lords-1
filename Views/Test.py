import arcade

# Set up screen size and other constants
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Turn-Based System with Button Press"

# Initialize game variables
player_turn = True  # Starts with Player 1

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player_1 = arcade.Sprite("E:\PythonProject\Medieval-Lords-1\Resources\Throne.png", scale=0.5)
        self.player_2 = arcade.Sprite("E:\PythonProject\Medieval-Lords-1\Resources\Views\CharacterSelecter.png", scale=0.5)

    def on_draw(self):
        arcade.start_render()
        # Draw the players
        self.player_1.draw()
        self.player_2.draw()

        # Display whose turn it is
        if player_turn:
            arcade.draw_text("Player 1's Turn", 350, 550, arcade.color.WHITE, 24)
        else:
            arcade.draw_text("Player 2's Turn", 350, 550, arcade.color.WHITE, 24)

    def on_update(self, delta_time):
        pass  # No need to do anything here since turn switching is done via key press

    def on_key_press(self, symbol, modifiers):
        global player_turn

        if symbol == arcade.key.W and player_turn:
            # Player 1 moves up
            self.player_1.center_y += 5
        elif symbol == arcade.key.S and player_turn:
            # Player 1 moves down
            self.player_1.center_y -= 5
        elif symbol == arcade.key.UP and not player_turn:
            # Player 2 moves up
            self.player_2.center_y += 5
        elif symbol == arcade.key.DOWN and not player_turn:
            # Player 2 moves down
            self.player_2.center_y -= 5

        # Switch turn on pressing Enter (for both players)
        if symbol == arcade.key.ENTER:
            self.switch_turn()

    def switch_turn(self):
        global player_turn
        player_turn = not player_turn  # Switch the turn

        # You can add additional actions when the turn switches, like sound effects or animations.

if __name__ == "__main__":
    game = MyGame()
    arcade.run()
