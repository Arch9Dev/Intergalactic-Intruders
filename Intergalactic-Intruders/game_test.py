import pygame
import constants
import Sprites

def test():
   pygame.init()
   screen_width = 800
   screen_height = 600
   screen = pygame.display.set_mode((screen_width, screen_height))
   pygame.display.set_caption("Main Menu")


   clock = pygame.time.Clock()
   pygame.key.set_repeat(10)
   
   Player = Sprites.AnimatedSpriteGroup("Intergalactic-Intruders\Test.gif",screen_width//2,screen_height//2)
   PosX = 0
   PosY = 0
   while True:
      clock.tick(24)
      for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                  PosX  = (PosX -1)  if  PosX  >= 0 else  800  
               if event.key == pygame.K_RIGHT:
                  PosX  = (PosX +1)  if  PosX  <= 800 else 0  
               if event.key == pygame.K_UP:
                  PosY  =1  if  PosY  >= 0 else  -600 
               if event.key == pygame.K_DOWN:
                  PosY  =1  if  PosY  >= -600 else 0     
         if event.type == pygame.QUIT:
               pygame.quit()
               quit()
      Player.update(PosX,PosY) 
      screen.fill((127, 192, 255))
      Player.draw(screen)
      print(f"Pos x = {PosX} /n y = {PosY} ")
      pygame.display.flip()

     

      
        
       
    
    





