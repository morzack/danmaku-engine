# player.py

# player class and helper functions

from bullet import WeaponizedObject

import json

class PlayerMoveDirection:
    n = [0, 1]
    ne = [0.5, 0.5]
    e = [1, 0]
    se = [0.5, -0.5]
    s = [0, -1]
    sw = [-0.5, -0.5]
    w = [-1, 0]
    nw = [-0.5, 0.5]

class Player(WeaponizedObject):
    def __init__(self):
        # yeah basically just do the super thing but add in useful tags for the player
        super().__init__(tags=["player", "friendly"])

        self.speed = 1
        self.visible_collider = False

    def load_player_config(self, config_filename):
        # load a player config from a json file
        with open(config_filename, 'r') as f:
            player_data = json.load(f)
            self.speed = player_data["speed"]
            self.collider.radius = player_data["size"]
            self.load_barrels(player_data["player_barrels"])

    def move(self, direction):
        # move the player at its speed using a PlayerMoveDirection
        self.collider.position.move_position(direction[0]*self.speed, direction[1]*self.speed)