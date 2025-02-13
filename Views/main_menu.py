import arcade
import Common.Constants
import ModelsForViews.Button as b
import Views.SavePicker
import Views.FirstView
SCREEN_TITLE = "Start menu"

class MainManuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.buttons = []

    def setup(self):
        start_x = Common.Constants.Screen.SCREEN_WIDTH // 2
        start_y = Common.Constants.Screen.SCREEN_HEIGHT // 2 + Common.Constants.Button.BUTTON_HEIGHT + Common.Constants.Button.BUTTON_SPACING

        self.buttons.append(
            b.Button(start_x, start_y, Common.Constants.Button.BUTTON_WIDTH, Common.Constants.Button.BUTTON_HEIGHT,
                     "Start new game", self.play))
        self.buttons.append(b.Button(start_x, start_y - (
                    Common.Constants.Button.BUTTON_HEIGHT + Common.Constants.Button.BUTTON_SPACING),
                                     Common.Constants.Button.BUTTON_WIDTH, Common.Constants.Button.BUTTON_HEIGHT,
                                     "Saves", self.saves))
        self.buttons.append(b.Button(start_x, start_y - 2 * (
                    Common.Constants.Button.BUTTON_HEIGHT + Common.Constants.Button.BUTTON_SPACING),
                                     Common.Constants.Button.BUTTON_WIDTH, Common.Constants.Button.BUTTON_HEIGHT,
                                     "Settings", self.options))

    def on_draw(self):
        self.clear()

        for button in self.buttons:
            button.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            for button in self.buttons:
                if button.is_clicked(x, y):
                    button.action_function()

    # Action Functions
    def play(self):
        view = Views.FirstView.MyGame()
        view.setup()
        self.window.show_view(view)

    def saves(self):
        view = Views.SavePicker.PickTheSave()
        view.setup()
        self.window.show_view(view)

    def options(self):
        view = Views.Options.SetTheThing()
        view.setup()
        self.window.show_view(view)

# End of Action Functions

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(Common.Constants.Screen.SCREEN_WIDTH, Common.Constants.Screen.SCREEN_HEIGHT, SCREEN_TITLE)

    def setup(self):
        view = MainManuView()
        view.setup()
        self.show_view(view)

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
