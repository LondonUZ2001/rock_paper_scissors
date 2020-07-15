import random

class Computer:
    def __init__(self,choices):
        self.choices = choices

    def get_choice(self):
        return random.choice(self.choices)


