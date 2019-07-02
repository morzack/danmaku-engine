from .state import State
from .player import Player
from .enemy import Enemy
from .utils import raduis_collision
from .spritecache import SpriteCache

import pygame

import json

class Level(State):
    """
    a playable level state, contains level updating logic and stuff like that
    """

    def __init__(self, level_number, config_data):
        """
        initialize the level given a number to pull from
        """
        super().__init__()
        self.level_number = level_number

        self.cached_level_data = SpriteCache(self.level_number)
        
        # load config stuff
        level_directory = f"data/levels/{self.level_number}"

        # load assets
        self.background = pygame.image.load(f"{level_directory}/background.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (config_data["width"], config_data["height"]))

        # load objects
        self.player = Player(config_data)

        self.enemies = []
        with open(f"{level_directory}/enemies.json", 'r') as f:
            enemy_level_data = json.load(f)
        for enemy in enemy_level_data["enemies"]:
            self.enemies.append(Enemy(enemy["id"], self.level_number, self.cached_level_data))

    def process_event(self, event : pygame.event.EventType):
        """
        process an event as needed. tl;dr keypresses and stuff
        """
        pass

    def update(self, surface : pygame.Surface, keys_pressed, current_time):
        """
        update the level and components or whatever
        """
        surface.blit(self.background, (0, 0)) # TODO is there a way to not blit over the _whole_ surface? this is time consuming
        self.player.update(surface, keys_pressed, current_time)
        for enemy in self.enemies:
            enemy.update(surface, current_time, self.player)
        
        # can we make this not something like O(n^2)? that's complete garbage.
        for bullet in self.player.bullets:
            for enemy in self.enemies:
                if enemy.active and enemy.alive and raduis_collision([bullet.x, bullet.y], bullet.radius, enemy.get_center(), enemy.hitbox):
                    enemy.kill()
                    self.player.bullets.remove(bullet) # NOTE this might throw an error, there was a try catch earlier...
                    break