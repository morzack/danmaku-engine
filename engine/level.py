from .state import State
from .player import Player
from .enemy import Enemy
from .utils import raduis_collision

import pygame

import json

class Level(State):
    """
    a playable level state, contains level updating logic and stuff like that
    """

    def __init__(self, level_number):
        """
        initialize the level given a number to pull from
        """
        super().__init__()
        self.level = level_number
        
        # load config stuff
        resource_directory = f"data"
        level_directory = f"{resource_directory}/levels/{self.level}"
        config_file = f"{resource_directory}/configuration.json"

        with open(config_file, 'r') as f:
            config_data = json.load(f)

        # load assets
        self.background = pygame.image.load(f"{level_directory}/background.png")
        self.background = pygame.transform.scale(self.background, (config_data["width"], config_data["height"]))

        # load objects
        self.player = Player()

        self.enemies = []
        with open(f"{level_directory}/enemies.json", 'r') as f:
            enemy_level_data = json.load(f)
        for enemy in enemy_level_data["enemies"]:
            self.enemies.append(Enemy(enemy["id"], self.level))

    def process_event(self, event : pygame.event.EventType):
        """
        process an event as needed. tl;dr keypresses and stuff
        """
        pass

    def update(self, surface : pygame.Surface, keys_pressed, current_time):
        """
        update the level and components or whatever
        """
        surface.blit(self.background, (0, 0))
        self.player.update(surface, keys_pressed, current_time)
        for enemy in self.enemies:
            enemy.update(surface, current_time, self.player)
        
        for bullet in self.player.bullets:
            for enemy in self.enemies:
                if enemy.active and enemy.alive and raduis_collision([bullet.x, bullet.y], bullet.radius, enemy.get_center(), enemy.hitbox):
                    enemy.kill()
                    try:
                        self.player.bullets.remove(bullet)
                    except:
                        # ¯\_(ツ)_/¯
                        pass