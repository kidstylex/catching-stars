import arcade
from models import World, Ship

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, title='Into the space')

        self.background = None
        self.ship_sprite = arcade.Sprite('img/ship.png')
        self.world = World(width, height)

    def set_up(self):
        self.background = arcade.load_texture("img/background.jpg")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.ship_sprite.draw()

    def update(self, delta):
        self.world.update(delta)
        self.ship_sprite.set_position(self.world.ship.x, self.world.ship.y)
if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.set_up()
    arcade.run()