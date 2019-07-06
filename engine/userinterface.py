import pygame

import json

class FontRenderer:
    def __init__(self):
        with open("data/configuration.json", 'r') as f:
            font_config = json.load(f)["fontconfig"]

        self.size = font_config["size"]
        self.name = font_config["name"]
        r, g, b = font_config["color"]
        self.color = pygame.Color(r, g, b)

        self.font = pygame.font.Font(pygame.font.match_font(self.name), self.size)

    def render_text(self, surface : pygame.Surface, x, y, text, color : pygame.Color = None):
        surface.blit(self.font.render(str(text), True, self.color if color == None else color), (x, y))

def get_input():
    keys = pygame.key.get_pressed()
    return {
        "quit" : keys[pygame.K_q],
        "left" : keys[pygame.K_LEFT],
        "right" : keys[pygame.K_RIGHT],
        "up" : keys[pygame.K_UP],
        "down" : keys[pygame.K_DOWN],
        "slowed" : keys[pygame.K_LSHIFT],
        "shoot" : keys[pygame.K_z],
        "bomb" : keys[pygame.K_x],
        "fpsup" : keys[pygame.K_CAPSLOCK]+keys[pygame.K_TAB],
        "debugpause" : keys[pygame.K_1]
    }