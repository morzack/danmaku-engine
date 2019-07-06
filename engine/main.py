import pygame

import json

from engine.userinterface import get_input, FontRenderer

from engine.level import Level

def main():
    print("starting game")

    pygame.init()

    config_file = "data/configuration.json"

    with open(config_file, 'r') as f:
        config_data = json.load(f)
        screen_width, screen_height = config_data["width"], config_data["height"]
        screen_caption = config_data["title"]
        default_fps = config_data["framerate"]
        debug_mode = config_data["debug"]

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(screen_caption)

    l0 = Level(0, config_data) # TODO proper level loading and menus

    clock = pygame.time.Clock()

    current_frame = 0

    debug_font_renderer = FontRenderer()

    running = True
    while running:
        actualfps = config_data["framerate"]

        keys = get_input()
        if keys["quit"]:
            running = False
        if not keys["debugpause"]:
            l0.update(screen, keys, current_frame)
            # print(current_frame) # TODO make this render onscreen if there's a debug mode or something
            debug_font_renderer.render_text(screen, 0, 0, current_frame)
            current_frame += 1

        clock.tick(default_fps*(2 if debug_mode and keys["fpsup"] else 1))
        pygame.event.pump() # TODO potentially have some kind of event hanlding for going through menus
        pygame.display.flip()