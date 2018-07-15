import os
from os.path import join, isfile

from utils.FileReader import FileReader
from utils.Functions import Functions


class WeaponTemplates:

    @staticmethod
    def get_starter_template():
        # Init
        filereader = FileReader()
        weaponsdict = []
        weapons_read = []
        weapons = []
        information_number = 4 * 2

        # Scan Dir for Weapon Files
        files = [f for f in os.listdir("./") if isfile(join("./", f))]
        files.remove("WeaponTemplates.py")

        # Append File Content
        for i in range(len(files)):
            weapons_read.append(filereader.line(os.path.dirname(__file__) + "/" + files[i]))

        # Write Data to List
        for i in weapons_read:
            for _i in i:
                item = _i.split("=")

                for _item in item:
                    _item = _item.strip(' ')
                    if "??" in item:
                        _item.replace("??", "100")
                    weapons.append(_item)

        # Convert List to Dict
        weapon = []
        for item in weapons:
            weapon.append(item)
            if len(weapon) % information_number == 0:
                weaponsdict.append(Functions.list_to_dict(weapon))
                del weapon

        # Return Result
        return weaponsdict
