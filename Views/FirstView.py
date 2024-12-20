import arcade
import Common.Constants

SCREEN_TITLE = "TITLETESTAAAAAAAAAAAAAA"
class MyGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = 0
        self.player_sprite = None
        arcade.set_background_color(arcade.csscolor.CHOCOLATE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        self.scene = arcade.Scene()

        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        image_source = "E:\PythonProject\Medieval-Lords-1\Resources\\Throne.png"
        self.player_sprite = arcade.Sprite(image_source, Common.Constants.Scaling.CHARACTER_SCALING)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 325
        self.scene.add_sprite("Player", self.player_sprite)

        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png",  Common.Constants.Scaling.TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png",  Common.Constants.Scaling.TILE_SCALING
            )
            wall.position = coordinate
            self.scene.add_sprite("Walls", wall)

    def on_draw(self):
        self.clear()

        self.scene.draw()

def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()