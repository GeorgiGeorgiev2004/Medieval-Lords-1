import arcade

class Button:
    def __init__(self, x, y, width, height, text, action_function):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.action_function = action_function

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.BLUE)

        arcade.draw_text(self.text, self.x, self.y, arcade.color.WHITE, font_size=18, anchor_x="center", anchor_y="center")

    def draw_with_offset_x_axis(self, scroll_x):
        x = self.x - scroll_x

        arcade.draw_rectangle_filled(x, self.y, self.width, self.height, arcade.color.BLUE)
        arcade.draw_text(self.text, x, self.y, arcade.color.WHITE, font_size=18, anchor_x="center", anchor_y="center")

    def is_clicked(self, x, y, scroll_x=None):
        if scroll_x is not None:
            coord_x = self.x - scroll_x
        return (coord_x - self.width / 2 < x < coord_x + self.width / 2 and
                self.y - self.height / 2 < y < self.y + self.height / 2)