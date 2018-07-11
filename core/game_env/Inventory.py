class Inventory:
    inventory: list = None

    def __init__(self):
        self.starterTemplate = "[stones]"
        # TODO: load inventory templates from store.txt
        # TODO: load inventory from store.txt and write to self.inventory

    def print_inventory(self):
        for item in self.inventory:
            print(item, "\n")

    def set_inventory(self, template: str, items: list=False):
        if template:
            if template == 'starterTemplate':
                self.inventory = self.starterTemplate
            # TODO: Add Templates
        elif items and not template:
            self.inventory = items

    def add_to_inventory(self, items: list, template: str=False):
        if items:
            for item in items:
                self.inventory.append(item)
        elif template and not items:
            if template == 'starterTemplate':
                for item in self.starterTemplate:
                    self.inventory.append(item)
            # TODO: Add Templates
