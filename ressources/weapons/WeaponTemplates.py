import os

from utils.FileReader import FileReader


class WeaponTemplates:

    @staticmethod
    def get_starter_template():
        filereader = FileReader()
        weapon_read = filereader.line(os.path.dirname(__file__) + "/fist.txt")
        weapon = []
        for i in weapon_read:
            item = i.replace(" ", "")
            item = item.split("=")
            if "??" in item:
                item.replace("??", "100")
            weapon.append(item)
        print(weapon)
        return {
            "weapon": weapon
        }


templates = WeaponTemplates()
templates.get_starter_template()