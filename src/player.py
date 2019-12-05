# Write a class to hold player information, e.g. what room they are in
# currently.

stars = '******************************'


class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(
            f'\n{stars}\nYou picked up the {item.name}\nYour inventory: {[i.name for i in self.inventory]}\n{stars}\n')
