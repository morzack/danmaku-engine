import pygame

import json
import math

from .utils import check_bounds, calculate_angle

class Bullet:
    def __init__(self, name, position, rotation, target=[0,0]):
        with open(f"data/configuration.json", 'r') as f:
            self.game_config = json.load(f)

        with open(f"data/bullets/{name}.json", 'r') as f:
            config = json.load(f)

        self.radius = config["radius"]
        self.speed = config["speed"]
        
        self.x = position[0]
        self.y = position[1]
        self.rotation = rotation

        if config["locking"]:
            # set rotation to position
            self.rotation = -math.degrees(calculate_angle(target, [self.x, self.y]))-90

        self.image = pygame.image.load(config["image_location"])
        self.image = pygame.transform.rotate(self.image, rotation-180)
        self.image = pygame.transform.scale(self.image, (self.radius*2, self.radius*2))

    def check_bounds(self):
        """
        returns True if the bullet is in bounds, otherwise false
        """
        return (check_bounds(self.x, 0, self.game_config["width"]) and check_bounds(self.y, 0, self.game_config["height"]))

    def update(self, surface : pygame.Surface):
        r = math.radians(self.rotation)
        d_x = self.speed*math.sin(r)
        d_y = self.speed*math.cos(r)

        self.x += d_x
        self.y += d_y

        surface.blit(self.image, (int(self.x)-self.image.get_width()/2, int(self.y)))