# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.room = current_room

    def __str__(self):
        output = f'Player name: {self.name} \n'
        output += f'Location: {self.current_room}'
        return output
