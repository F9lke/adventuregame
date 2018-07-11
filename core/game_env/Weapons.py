from core.game_env.Inventory import Inventory


class Weapons(Inventory):
    def __init__(self):
        super().__init__()
        self.weapons = []