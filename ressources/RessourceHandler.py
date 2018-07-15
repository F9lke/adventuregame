from ressources.items.ItemTemplates import ItemTemplates
from ressources.weapons.WeaponTemplates import WeaponTemplates


class RessourceHandler:

    def __init__(self):
        self.item_templates = ItemTemplates()
        self.weapon_templates = WeaponTemplates()

    def increment_durability(self, ressource):
        return True

    def decrement_durability(self, ressource):
        return True

    def load_items(self):
        return True

    def load_weapons(self):
        return True
