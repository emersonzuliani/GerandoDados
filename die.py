#class die

from random import randint

class Die():
    """Uma classe que representa um único dado"""

    def __init__(self, num_sides=6):
        """dados de 6 lados"""
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

