from engine.state import State

import pygame

import json

class LevelEditor(State):
    """
    A state to edit a given level
    """

    def __init__(self, level_number):
        """
        initialize the level given a number to pull from
        """
        super().__init__()
        self.level = level_number
        
        # load config stuff
        level_directory = "data/levels/{self.level}"
        game_config_file = f"data/configuration.json"

        with open(game_config_file, 'r') as f:
            config_data = json.load(f)

        # load assets
        self.background = pygame.Surface((config_data["width"], config_data["height"]))
        self.background.fill(pygame.Color(0, 0, 100))

        self.point_x = 100
        self.point_y = 100

        self.point_move_speed = 2

        self.point_radius = 5
        self.point_image = pygame.image.load(f"data/playerdata/playerhitbox.png")
        self.point_image = pygame.transform.scale(self.point_image, (self.point_radius*2, self.point_radius*2))

        self.marked_point_radius = 2
        self.marked_point_image = pygame.transform.scale(self.point_image, (self.marked_point_radius*2, self.marked_point_radius*2))

        self.marked_points = []

    def process_event(self, event : pygame.event.EventType):
        """
        process an event as needed. tl;dr keypresses and stuff
        """
        pass

    def update(self, surface : pygame.Surface, keys_pressed):
        """
        update the level and components or whatever
        """
        surface.blit(self.background, (0, 0))

        if keys_pressed["left"]:
            self.point_x -= self.point_move_speed
        if keys_pressed["right"]:
            self.point_x += self.point_move_speed
        if keys_pressed["up"]:
            self.point_y -= self.point_move_speed
        if keys_pressed["down"]:
            self.point_y += self.point_move_speed

        if keys_pressed["shoot"]:
            point = [self.point_x, self.point_y]
            if len(self.marked_points) == 0 or self.marked_points[-1] != point:
                self.marked_points.append(point)

        for point in self.marked_points:
            surface.blit(self.marked_point_image, (int(point[0]), int(point[1])))
        
        if keys_pressed["slowed"]:
            print(self.marked_points)

        if keys_pressed["bomb"]:
            self.marked_points = []

        surface.blit(self.point_image, (int(self.point_x-self.point_radius), int(self.point_y-self.point_radius)))