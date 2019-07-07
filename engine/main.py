import pygame

import json

from engine.userinterface import get_input, FontRenderer, get_keypresses

from engine.level import Level

def main():
    print("starting game")

    pygame.init()
    pygame.mixer.init()

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

    # marked frames for level design purposes
    marked_frames = []

    running = True
    while running:
        actualfps = config_data["framerate"]

        keys = get_input()
        if keys["quit"]:
            running = False
        if not (keys["debugpause"] and debug_mode):
            l0.update(screen, keys, current_frame)
            # print(current_frame) # TODO make this render onscreen if there's a debug mode or something
            debug_font_renderer.render_text(screen, 0, 0, current_frame)
            current_frame += 1
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys_pressed = get_keypresses(event.key)
                if debug_mode and keys_pressed["mark"]:
                    marked_frames.append(current_frame)

        clock.tick(default_fps*(2 if debug_mode and keys["fpsup"] else 1))
        pygame.event.pump() # TODO potentially have some kind of event hanlding for going through menus
        pygame.display.flip()
    
    # print out the marked frames for debug reasons
    print(marked_frames)