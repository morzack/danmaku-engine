import pygame

import json

from engine.userinterface import get_input

from editor.patheditor import LevelEditor

def main():
    print("entering main")
    
    pygame.init()

    game_config_file = f"data/configuration.json"

    with open(game_config_file, 'r') as f:
        game_config_data = json.load(f)
    
    path_editor_config_file = f"editor/config.json"

    with open(path_editor_config_file, 'r') as f:
        path_editor_config_data = json.load(f)

    screen = pygame.display.set_mode((path_editor_config_data["width"], path_editor_config_data["height"]))
    pygame.display.set_caption(path_editor_config_data["title"])

    clock = pygame.time.Clock()

    editor = LevelEditor(0)

    running = True
    while running:
        keys = get_input()
        if keys["quit"]:
            running = False

        pygame.event.pump()
        pygame.display.flip()

        editor.update(screen, keys)

        clock.tick(game_config_data["framerate"])