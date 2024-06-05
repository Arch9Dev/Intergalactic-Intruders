import pygame
import constants
import Sprites
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

  #Button_Palette = Colours.Blue_Buttons
  
   Testing  =  constants.Button("Testing",100,100, 200,100,constants.Colour_Palettes["Red_Buttons"])
   buttons = [Testing]

   #Animating Sprites
   Player = Sprites.AnimatedSpriteGroup("Intergalactic-Intruders/Test.gif",screen_width//2,screen_height//2)
   PosX = 0
   PosY = 0
   start = True
   timedisplaytext = "  "
   while True:
      clock.tick(60)
      i= 0
      if start : 
         j = 0
         t = 0
         start = False
      screen.fill((127, 192, 255))
      for event in pygame.event.get():
         if event.type == pygame.MOUSEMOTION:
            MousePos = pygame.mouse.get_pos()
            while  i < len(buttons):
               buttons[i].hovered = buttons[i].rect.collidepoint(MousePos)
               buttons[i].draw()
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
    
     

      j = j + 1
      

      

      while  i < len(buttons):
         buttons[i].draw()
         i += 1
      Player.update(PosX,PosY)
     
      Player.draw(screen)
      pygame.display.flip()
     

      
if __name__ == "__main__":
   test()
   
    
    





