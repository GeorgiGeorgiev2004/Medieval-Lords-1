import arcade
import arcade.gui

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade Popup Menu Example"


class PopupMenu(arcade.gui.UIBoxLayout):
    def __init__(self, on_close_callback):
        super().__init__()

        self.on_close_callback = on_close_callback

        # Create buttons for the popup menu
        close_button = arcade.gui.UIFlatButton(text="Close Menu", width=200)
        option_button = arcade.gui.UIFlatButton(text="Option 1", width=200)

        # Add the buttons to the popup layout
        self.add(option_button.with_space_around(bottom=10))
        self.add(close_button.with_space_around(bottom=10))

        # Attach event to the close button
        @close_button.event("on_click")
        def on_close_click(event):
            self.on_close_callback()


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # GUI Manager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a button to open the popup
        open_button = arcade.gui.UIFlatButton(text="Open Menu", width=200)
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=open_button
            )
        )

        # Attach event to the button
        open_button.on_click = self.show_popup

        # Placeholder for popup menu
        self.popup = None

    def show_popup(self, event):
        if not self.popup:
            # Create and add popup to UIManager
            self.popup = PopupMenu(on_close_callback=self.close_popup)
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                    anchor_x="center_x",
                    anchor_y="center_y",
                    child=self.popup
                )
            )

    def close_popup(self):
        # Clear all UI elements and re-add the main button
        self.manager.children.clear()
        self.popup = None

        # Re-add the main button after closing the popup
        open_button = arcade.gui.UIFlatButton(text="Open Menu", width=200)
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=open_button
            )
        )
        open_button.on_click = self.show_popup

    def on_draw(self):
        self.clear()
        self.manager.draw()


if __name__ == "__main__":
    app = MyGame()
    arcade.run()
