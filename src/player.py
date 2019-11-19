# Write a class to hold player information, e.g. what room they are in
# currently.
class Player(self, name, current_room):
    """docstring for Player."""

    def __init__(self):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        output = f'Player name: {self.name} \n'
        output += f'Location: {self.current_room}'
        return output
