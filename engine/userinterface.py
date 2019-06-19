import pygame

import json

def get_input():
    keys = pygame.key.get_pressed()
    return {
        "quit" : keys[pygame.K_q],
        "left" : keys[pygame.K_LEFT],
        "right" : keys[pygame.K_RIGHT],
        "up" : keys[pygame.K_UP],
        "down" : keys[pygame.K_DOWN],
        "slowed" : keys[pygame.K_LSHIFT],
        "shoot" : keys[pygame.K_z]
    }