import arcade

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, title='Into the space')
        arcade.set_background_color(arcade.color.WHEAT)

        self.background = None

    def set_up(self):
        self.background = arcade.load_texture("img/background.jpg")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.set_up()
    arcade.run()