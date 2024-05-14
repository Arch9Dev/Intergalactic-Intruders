import pygame
import constants
from constants import Button
import Sprites
import Colours
import main
def test():

   #ViewPort
   pygame.init()
   screen_width = 800
   screen_height = 600
   screen = pygame.display.set_mode((screen_width, screen_height))
   pygame.display.set_caption("Testing")
   screen.fill((127, 192, 255))

   #Code
   clock = pygame.time.Clock()
   pygame.key.set_repeat(10)

  #Button_Palette = Colours.Blue_Buttons
  
   Testing  =  constants.Button(screen,"Testing",100,100, 200,100,Colours.Colour_Palettes["Red_Buttons"])
   buttons = [Testing]

   #Animating Sprites
   Player = Sprites.AnimatedSpriteGroup("Intergalactic-Intruders\Test.gif",screen_width//2,screen_height//2)
   PosX = 0
   PosY = 0
 
  

 
   while True:
      clock.tick(24)
      i= 0
      for event in pygame.event.get():
         if event.type == pygame.MOUSEMOTION:
            MousePos = pygame.mouse.get_pos()
            while  i < len(buttons):
               buttons[i].hovered = buttons[i].rect.collidepoint(MousePos)
               i += 1
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
      pygame.display.

      while  i < len(buttons):
         buttons[i].draw()
         i += 1
      Player.draw(screen)   
      pygame.display.update()
     

      
if __name__ == "__main__":
   main.main_menu()
   
    
    





