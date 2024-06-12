import pygame
from PIL import Image, ImageSequence
def test():

   #ViewPort
   pygame.init()
   screen_width = 800
   screen_height = 600
   screen = pygame.display.set_mode((screen_width, screen_height))
   pygame.display.set_caption("Testing")

   #Code
   clock = pygame.time.Clock()
   pygame.key.set_repeat(10)

   def AnimatedSpriteGroup(SpriteFileName,PosX,PosY):
      SpriteGIFFrameList = loadGIF(SpriteFileName)
      animated_sprite = AnimatedSpriteObject(PosX,PosY,SpriteGIFFrameList)
      return (pygame.sprite.Group(animated_sprite)) # type: ignore

   def loadGIF(filename):
    pilImage = Image.open(filename)
    AnimationFrames = []
    for Frames in ImageSequence.Iterator(pilImage):
        Frames = Frames.convert('RGBA')
        pygameImage = pygame.image.fromstring(
            Frames.tobytes(), Frames.size, 'RGBA').convert_alpha()
        AnimationFrames.append(pygameImage)
    return AnimationFrames

   class AnimatedSpriteObject(pygame.sprite.Sprite):
    def __init__(self, X, Y, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom = (X, -Y))
        self.image_index = 0
    def update(self, PosX, PosY):
        self.rect.x = PosX
        self.rect.y = -PosY
        self.image_index += 1
        self.image = self.images[self.image_index % len(self.images)]


   Sprite_GIF_Path = {
      "Player_Ship" : r"Intergalactic-Intruders\images\Player.gif",
      "Alion_ONE": r"Intergalactic-Intruders/images/Alien1.gif",
      "Alion_TWO": r"Intergalactic-Intruders/images/Alien2.gif",
      "Alion_THREE": r"Intergalactic-Intruders/images/Alien3.gif",
      "Mother_Ship": r"Intergalactic-Intruders\images\Alien4.gif"
   }

   #Animating Sprites
   Player = AnimatedSpriteGroup(Sprite_GIF_Path["Player_Ship"],screen_width//2,screen_height//2)
   Ailon_1 = AnimatedSpriteGroup(Sprite_GIF_Path["Alion_ONE"],screen_width//2,screen_height//2)  
   Ailon_2 = AnimatedSpriteGroup(Sprite_GIF_Path["Alion_TWO"],screen_width//2,screen_height//2)
   Ailon_3 = AnimatedSpriteGroup(Sprite_GIF_Path["Alion_THREE"],screen_width//2,screen_height//2)
   Mothership = AnimatedSpriteGroup(Sprite_GIF_Path["Mother_Ship"],screen_width//2,screen_height//2)
   PosX = 0
   PosY = 0
   while True:
      clock.tick(24)
      screen.fill((127, 192, 255))
      for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               PosX  = (PosX -1)  
            if event.key == pygame.K_RIGHT:
               PosX  = (PosX +1) 
            if event.key == pygame.K_UP:
               PosY  = (PosY +1)  
            if event.key == pygame.K_DOWN:
               PosY  = (PosY -1)  
         if event.type == pygame.QUIT:
            pygame.quit()
            quit()
      if PosX <0:
         PosX = 800
      elif PosX >800:
         PosX = 0
      
      if PosY <-600:
         PosY = 0 
      elif PosY >0:
         PosY = -600
    
     

      Player.update(PosX,PosY)
      Mothership.update(100,-100)
      Ailon_1.update(600,-300)
      Ailon_2.update(500,-400)
      Ailon_3.update(300,-300)
      Mothership.draw(screen)
      Ailon_3.draw(screen)
      Ailon_2.draw(screen)
      Ailon_1.draw(screen)
      
      Player.draw(screen)
      Mothership.draw(screen)

      pygame.display.flip()
     

      
if __name__ == "__main__":
   test()