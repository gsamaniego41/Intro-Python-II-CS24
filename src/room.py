# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    '''
    Room class with an attribute of description
    '''

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __repr__(self):
        # __repr__ is for debuggin and development
        print(f'Name: {self.name}, Description: {self.desc}')

    def __str__(self):
        # __str__ is for end user
        print(f'Room: {self.name} - {self.desc}')
