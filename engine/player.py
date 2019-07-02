import pygame
import json

from .utils import clamp
from .bullet import Bullet

class Player:
    """
    the player. pretty self explanatory i hope
    """

    def __init__(self, config_data):
        """
        config_data should be the json data config for the _game_ preloaded into a dict
        """
        player_data_dir = "data/playerdata"
        
        self.screen_w, self.screen_h = config_data["width"], config_data["height"]

        with open(f"{player_data_dir}/playerconfig.json") as f:
            # NOTE all of the important things here are loaded into variables because that's faster than a dict
            player_config = json.load(f)
            self.height, self.width = player_config["height"], player_config["width"]
            self.barreloffset = player_config["barreloffset"]
            self.hitbox_size = player_config["hitbox"]
            self.frames_between_shots = player_config["shootrate"]
            self.slowed_modifier = player_config["slowedmodifier"]
            self.speed = player_config["speed"]

        # configure images to render
        # TODO player animations
        self.player_image = pygame.image.load(f"{player_data_dir}/player.png").convert_alpha()
        self.player_image = pygame.transform.scale(self.player_image, (self.width, self.height))

        self.hitbox_image = pygame.image.load(f"{player_data_dir}/playerhitbox.png").convert_alpha()
        self.hitbox_image = pygame.transform.scale(self.hitbox_image, (self.hitbox_size*2, self.hitbox_size*2))

        # start the player down in the center of the screen
        self.x = self.screen_w/2 - self.width/2
        self.y = self.screen_h*.7

        # bullets that the player will keep track of
        self.bullets = []

        # used to regulate fire
        self.last_shot = -self.frames_between_shots

        # updated by outside forces if the player is hit
        self.hit_last_frame = False

    def shoot(self, current_time):
        """
        return all the bullets (in a list) that the player _can_ shoot at a given time
        """
        b = []
        if self.last_shot+self.frames_between_shots < current_time:
            # TODO change this based on player shot type configuration and power
            b.append(Bullet("playerbullet", [self.x+self.width/2-self.barreloffset, self.y], 180))
            b.append(Bullet("playerbullet", [self.x+self.width/2+self.barreloffset, self.y], 180))
            self.last_shot = current_time
        return b

    def get_center(self):
        """
        get the center of the player's sprite, which is also the center of the hitbox
        """
        center_x = self.x+self.width/2
        center_y = self.y+self.height/2
        return [center_x, center_y]

    def kill(self):
        """
        this should be called if the player is ever hit by a bullet
        """
        self.hit_last_frame = True

    def update(self, surface : pygame.Surface, keys, current_time):
        """
        update the player object
        surface is the surface to render onto
        keys are the keys currently pressed, as declared in userinterface
        current_time is the current frame
        """
        # handle killing the player
        # TODO actually kill the player
        if self.hit_last_frame:
            print("oof, you got hit") # this shouldn't exist for too long...
            self.hit_last_frame = False

        # handle slowing if the player makes it slower
        speed_modifier = self.slowed_modifier if keys["slowed"] else 1
        if keys["left"]:
            self.x -= self.speed*speed_modifier
        if keys["right"]:
            self.x += self.speed*speed_modifier
        if keys["up"]:
            self.y -= self.speed*speed_modifier
        if keys["down"]:
            self.y += self.speed*speed_modifier
        if keys["shoot"]:
            self.bullets.extend(self.shoot(current_time))

        # clamp the player's position
        self.x = clamp(self.x, 0, self.screen_w-self.width)
        self.y = clamp(self.y, 0, self.screen_h-self.height)

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