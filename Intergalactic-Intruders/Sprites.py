from typing import Any
import pygame

def load_image(name):
    image = pygame.image.load(name)
    return image

class PlayerSprites(pygame.sprite.Sprite):
    def __init__(self):
        super(PlayerSprites, self).__init__()
        self.Player_Frames = []
        for i in range(9) :
            self.Player_Frames.append(load_image(f"Intergalactic-Intruders\images\PlayerShip\sprite_{i}.png"))
        self.index = 0
        self.Player_Frames = self.Player_Frames[self.index]
        self.rect = pygame.Rect(5,5, 32,32)
   
    def  update(self):
        self.index += 1
        self.index = 0 if self.index >= 8  else   self.index
        self.Player_Frames = self.Player_Frames[self.index]