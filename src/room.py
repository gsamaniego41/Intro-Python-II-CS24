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

    def __repr__(self):
        # __repr__ is for debuggin and development
        return f'Name: {self.name}, Description: {self.desc}'

    def __str__(self):
        # __str__ is for end user
        return f'You\'re in {self.name} - {self.desc}'
