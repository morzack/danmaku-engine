import pygame

import json

class CachedPath:
    def __init__(self, max_speed, path, rotate_path):
        self.max_speed = max_speed
        self.path = path
        self.rotate_path = rotate_path

class CachedEnemy:
    def __init__(self, enemy_data):
        self.data = enemy_data
        self.image = pygame.image.load(f"data/enemies/images/{self.data['image']}.png").convert_alpha()

class CachedBullet:
    def __init__(self, bullet_data):
        self.data = bullet_data
        self.image = pygame.image.load(f"data/bullets/images/{self.data['image_location']}.png").convert_alpha()

class SpriteCache:
    def __init__(self, level_id):
        """
        this is used to preload all of the sprites referenced in various json files
        it also preloads things that are level specific like paths
        """
        self.enemy_sprites = {}
        self.bullet_sprites = {}

        level_dir = f"data/levels/{level_id}"

        with open(f"{level_dir}/enemies.json", 'r') as f:
            self.level_enemy_data = json.load(f)["enemies"]
        with open(f"data/paths.json", 'r') as f:
            path_data = json.load(f)["paths"]
        with open("data/enemies/enemies.json", 'r') as f:
            all_enemy_data = json.load(f)
        with open("data/bullets/bullets.json", 'r') as f:
            all_bullet_data = json.load(f)

        # build a list of all enemies referenced in this level
        self.referenced_enemies = []
        for enemy_id in [x["type"] for x in self.level_enemy_data]:
            if enemy_id not in self.referenced_enemies:
                self.referenced_enemies.append(enemy_id)
        
        # load in paths
        self.paths = {}
        for path in path_data:
            self.paths[path["id"]] = CachedPath(path["maxspeed"], path["points"], path["rotatewith"])
        
        # load enemy ids based on sprites
        for enemy in self.referenced_enemies:
            self.enemy_sprites[enemy] = CachedEnemy(all_enemy_data[enemy])

        # load bullet data
        for bullet in all_bullet_data:
            self.bullet_sprites[bullet] = CachedBullet(all_bullet_data[bullet])

    def get_cached_bullet(self, i):
        return self.bullet_sprites[i]

    def get_cached_path(self, i):
        return self.paths[i]
    
    def get_cached_enemy(self, i):
        return self.enemy_sprites[i]