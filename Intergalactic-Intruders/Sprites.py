import pygame
from PIL import Image, ImageSequence

def loadGIF(filename):
    pilImage = Image.open(filename)
    AnimationFrames = []
    for Frames in ImageSequence.Iterator(pilImage):
        Frames = Frames.convert('RGBA')
        pygameImage = pygame.image.fromstring(
            Frames.tobytes(), Frames.size, Frames.mode).convert_alpha()
        AnimationFrames.append(pygameImage)
    return AnimationFrames

class AnimatedSpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, bottom, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom = (x, bottom))
        self.image_index = 0
    def update(self):
        self.image_index += 1
        self.image = self.images[self.image_index % len(self.images)]
        


def AnimatedSpriteGroup(SpriteFileName,PosX,PosY):
 SpriteGIFFrameList = loadGIF(SpriteFileName)
 animated_sprite = AnimatedSpriteObject(PosX,PosY,SpriteGIFFrameList)
 return (pygame.sprite.Group(animated_sprite))

