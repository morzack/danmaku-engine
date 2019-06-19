import pygame
import json

from .utils import clamp
from .bullet import Bullet

class Player:
    """
    the player. pretty self explanatory i hope
    """

    def __init__(self):
        data_dir = f"data"
        player_data_dir = f"{data_dir}/playerdata"

        with open(f"{data_dir}/configuration.json", 'r') as f:
            self.config_data = json.load(f)

        with open(f"{player_data_dir}/playerconfig.json") as f:
            self.player_config = json.load(f)

        self.player_image = pygame.image.load(f"{player_data_dir}/player.png")
        self.player_image = pygame.transform.scale(self.player_image, (self.player_config["width"], self.player_config["height"]))

        self.hitbox_image = pygame.image.load(f"{player_data_dir}/playerhitbox.png")
        self.hitbox_image = pygame.transform.scale(self.hitbox_image, (self.player_config["hitbox"]*2, self.player_config["hitbox"]*2))

        # start the player 80% down in the center of the screen
        self.x = self.config_data["width"]/2 - self.player_config["width"]/2
        self.y = self.config_data["height"]*.7

        self.hitbox_size = self.player_config["hitbox"]

        self.bullets = []

        self.last_shot = -self.player_config["shootrate"]
        self.frames_between_shots = self.player_config["shootrate"]

        self.hit_last_frame = False

    def shoot(self, current_time):
        """
        return all the bullets that the player can shoot at a given time
        """
        b = []

        if self.last_shot+self.frames_between_shots < current_time:
            b.append(Bullet("playerbullet", [self.x+self.player_config["width"]/2-self.player_config["barreloffset"], self.y], 180))
            b.append(Bullet("playerbullet", [self.x+self.player_config["width"]/2+self.player_config["barreloffset"], self.y], 180))
            self.last_shot = current_time

        return b

    def get_center(self):
        center_x = self.x+self.player_config["width"]/2
        center_y = self.y+self.player_config["height"]/2
            
        return [center_x, center_y]

    def kill(self):
        """
        this should be called if the player is ever hit by a bullet
        """
        self.hit_last_frame = True

    def update(self, surface : pygame.Surface, keys, current_time):
        # handle killing the player
        if self.hit_last_frame:
            print("oof, you got hit")
            self.hit_last_frame = False

        # handle slowing if the player makes it slower
        speed_modifier = self.player_config["slowedmodifier"] if keys["slowed"] else 1
        if keys["left"]:
            self.x -= self.player_config["speed"]*speed_modifier
        if keys["right"]:
            self.x += self.player_config["speed"]*speed_modifier
        if keys["up"]:
            self.y -= self.player_config["speed"]*speed_modifier
        if keys["down"]:
            self.y += self.player_config["speed"]*speed_modifier
        if keys["shoot"]:
            self.bullets.extend(self.shoot(current_time))

        # clamp the player's position
        self.x = clamp(self.x, 0, self.config_data["width"]-self.player_config["width"])
        self.y = clamp(self.y, 0, self.config_data["height"]-self.player_config["height"])

        # update player bullets
        for bullet in self.bullets:
            if not bullet.check_bounds():
                self.bullets.remove(bullet)
            else:
                bullet.update(surface)

        # draw the player to the screen
        surface.blit(self.player_image, (int(self.x), int(self.y)))

        # show the player hitbox if slowed
        if keys["slowed"]:
            center = self.get_center()
            surface.blit(self.hitbox_image, (int(center[0]-self.hitbox_size), int(center[1]-self.hitbox_size)))