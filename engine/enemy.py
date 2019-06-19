import pygame
import json
import math

from .utils import clamp, calculate_angle, raduis_collision
from .bullet import Bullet

class Enemy:
    MOVEMENTERRORTOLERANCE = 2
    ROTATIONSPEED = 20

    def __init__(self, enemyID, level):
        # load the enemy data for this enemy from the level file
        with open(f"data/levels/{level}/enemies.json", 'r') as f:
            leveldata = json.load(f)

        for enemy in leveldata["enemies"]:
            if enemy["id"] == enemyID:
                self.enemy_level_data = enemy
                break
        
        for path in leveldata["paths"]:
            if path["id"] == self.enemy_level_data["path"]:
                self.max_speed = path["maxspeed"]
                self.path = path["points"]
                self.rotate_path = path["rotatewith"]
                break

        self.type = self.enemy_level_data["type"]

        # load the enemy config for _this_ enemy
        with open(f"data/enemies/{self.type}/config.json", 'r') as f:
            self.enemy_data = json.load(f)

        self.active = False
        self.alive = True

        self.image = pygame.image.load(f"data/enemies/{self.type}/image.png")
        self.image = pygame.transform.scale(self.image, [self.enemy_data["width"], self.enemy_data["height"]])

        self.x = float(self.path[0][0])
        self.y = float(self.path[0][1])

        self.current_waypoint = 0

        self.rotation = 0
        
        self.bullets = []

        self.hitbox = self.enemy_data["hitbox"]
        self.frames_between_shots = self.enemy_data["shootrate"]
        self.last_shot = 0

        self.health = self.enemy_data["health"]
    
    def get_center(self):
        center_x = self.x+self.image.get_width()/2
        center_y = self.y+self.image.get_height()/2
            
        return [center_x, center_y]

    def kill(self):
        self.health -= 1

    def shoot(self, current_time, player):
        """
        shoot the bullet, return array of new bullets
        """
        b = []

        player_center = player.get_center()

        if self.last_shot+self.frames_between_shots < current_time:
            b.append(Bullet("testenemybullet", [self.x+self.enemy_data["width"]/2, self.y+self.enemy_data["height"]], 0, player_center))
            self.last_shot = current_time

        return b

    def update(self, surface : pygame.Surface, current_time, player):
        if self.health <= 0:
            self.alive = False
        if current_time > self.enemy_level_data["entrytime"]:
            self.active = True
        if current_time > self.enemy_level_data["exittime"]:
            self.active = False
            self.alive = False
        if not (self.active and self.alive):
            return

        # move in a line to the next point at max speed, if not done moving
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        if self.current_waypoint < len(self.path)-1:
            next_point = self.path[self.current_waypoint+1]
            error = math.sqrt((next_point[0]-self.x)**2+(next_point[1]-self.y)**2)
            angle_to_next_point = calculate_angle([self.x, self.y], next_point)
            dx = math.cos(angle_to_next_point)
            dy = math.sin(angle_to_next_point)
            self.x += dx*self.max_speed
            self.y += dy*self.max_speed
            if error < Enemy.MOVEMENTERRORTOLERANCE*self.max_speed:
                self.current_waypoint += 1
            if self.rotate_path:
                image_rot = 90-math.degrees(angle_to_next_point)
                image_rot -= self.rotation
                self.rotation += image_rot/Enemy.ROTATIONSPEED

        self.bullets.extend(self.shoot(current_time, player))
        for bullet in self.bullets:
            if not bullet.check_bounds():
                self.bullets.remove(bullet)
            else:
                bullet.update(surface)
                if raduis_collision([bullet.x, bullet.y], bullet.radius, player.get_center(), player.hitbox_size):
                    player.kill()
                    self.bullets.remove(bullet)

        surface.blit(rotated_image, [int(self.x), int(self.y)])