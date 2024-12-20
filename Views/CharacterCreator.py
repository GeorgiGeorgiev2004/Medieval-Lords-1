import arcade
import Common.Constants
import ModelsForViews.Button as b

class HorizontalScrollView(arcade.View):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.scroll_x = 0
        self.button_height = Common.Constants.CharacterCreator.BUTTON_HEIGHT
        self.button_width = Common.Constants.CharacterCreator.BUTTON_WIDTH
        self.spacing = 30
        self.max_scroll_x = 0

    def setup(self):
        start_y = self.window.height // 2
        x_position = self.button_width // 2 + self.spacing

        for i in range(6):
            self.buttons.append(b.Button(x_position, start_y, self.button_width, self.button_height,f"{i+1}" , self.on_button_click(i)))
            x_position += self.button_width + self.spacing

        total_width = len(self.buttons) * (self.button_width + self.spacing) - self.spacing
        self.max_scroll_x = max(0, total_width - self.window.width)

    def on_draw(self):
        self.clear()

        arcade.draw_rectangle_filled(self.window.width // 2, self.window.height // 2, self.window.width, self.window.height, arcade.color.LIGHT_GRAY)

        for button in self.buttons:
            button.draw_with_offset(self.scroll_x)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        if scroll_y != 0:
            self.scroll_x -= scroll_y * 30
            self.scroll_x = max(0, min(self.scroll_x, self.max_scroll_x))

    def on_mouse_press(self, x, y, button, modifiers):
        for btn in self.buttons:
            if btn.is_clicked(x, y, self.scroll_x):
                btn.action_function()

    def on_button_click(self, button_index):
        print(f"Button {button_index + 1} clicked!")

def main():
    window = arcade.Window(800, 600, "Horizontal Scroll with Mouse Wheel Example")
    scroll_view = HorizontalScrollView()
    scroll_view.setup()
    window.show_view(scroll_view)
    arcade.run()

if __name__ == "__main__":
    main()
