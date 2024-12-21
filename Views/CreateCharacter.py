import arcade
from arcade.gui import UIManager, UIInputText, UIFlatButton


class MyForm(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Initialize UI Manager
        self.ui_manager = UIManager(self)

        # Text input field
        self.input_text = UIInputText(x=300, y=300, width=200, height=40)

        # Submit button
        self.submit_button = UIFlatButton(text="Submit", x=300, y=200, width=200, height=40)

        # Add widgets to the UI manager
        self.ui_manager.add(self.input_text)
        self.ui_manager.add(self.submit_button)

    def on_draw(self):
        arcade.start_render()
        self.ui_manager.draw()  # This will draw all the UI elements

    def on_update(self, delta_time):
        self.ui_manager.on_update(delta_time)  # Update UI manager

    def on_mouse_press(self, x, y, button, modifiers):
        self.ui_manager.on_mouse_press(x, y, button, modifiers)  # Handle mouse press

        # Handle button click
        if self.submit_button.collides_with_point((x, y)):
            print("Input Text:", self.input_text.text)


# Create and run the form window
window = MyForm(800, 600, "Arcade Form with Text Input")
arcade.run()
