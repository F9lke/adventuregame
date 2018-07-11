from core.game_env import Inventory
from core.game_env.Game import Game
from core.story import World as StoryWorld
from core.tutorial import World as TutorialWorld


class Player(Game):

    def __init__(self, tutorial=False):
        self.tutorial_instance = tutorial
        self.inventory = Inventory.inventory
        self.hp = 100
        if tutorial:
            self.world = StoryWorld
            self.location_x, self.location_y = self.world.starting_position
        else:
            self.world = TutorialWorld
            self.locaiton_x, self.location_y = self.world.starting_position
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        if self.world.tile_exists(self.location_x, self.location_y):
            self.world.init_tile_action(self.location_x, self.location_y)
        else:
            super().add_game_error("There is no tile at your position.")

    def move_north(self):
        self.move(dx=0, dy=-0)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
