# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    '''
    Room class with attributes of name and description
    '''

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        '''
        Removes item from room after being picked up by player.
        '''
        self.items = []

    def __repr__(self):
        # __repr__ is for debugging and development
        return f'<Name: {self.name}, Description: {self.desc}>'

    def __str__(self):
        # __str__ is for end user
        return f'{self.name} - {self.desc}'
