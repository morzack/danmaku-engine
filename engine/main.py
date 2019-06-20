import pygame

import json

from engine.userinterface import get_input

from engine.level import Level

def main():
    print("entering main")
    
    pygame.init()

    config_file = f"data/configuration.json"

    with open(config_file, 'r') as f:
        config_data = json.load(f)

    screen = pygame.display.set_mode((config_data["width"], config_data["height"]))
    pygame.display.set_caption(config_data["title"])

    l0 = Level(0)

    clock = pygame.time.Clock()

    frameCounter = 0

    running = True
    while running:
        actualfps = config_data["framerate"]

        keys = get_input()
        if keys["quit"]:
            running = False
        if keys["fpsup"]:
            actualfps *= 2

        l0.update(screen, get_input(), frameCounter)

        # print(frameCounter)

        pygame.event.pump()
        pygame.display.flip()

        clock.tick(actualfps)
        frameCounter += 1