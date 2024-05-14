import pygame
import constants
import Sprites
import Colours

def test():
   #ViewPort
   pygame.init()
   screen_width = 800
   screen_height = 600
   screen = pygame.display.set_mode((screen_width, screen_height))
   pygame.display.set_caption("Main Menu")
   screen.fill((127, 192, 255))

   #Code
   clock = pygame.time.Clock()
   pygame.key.set_repeat(10)

  #Button_Palette = Colours.Blue_Buttons
  
   test_Button = constants.Button(screen,"Testing",100,100, 200,100,Colours.Colour_Palettes["Red_Buttons"])
   buttons = [test_Button]
   print(test_Button.Colour_Palette["Text_Colour"])
   Mouse_pos = (0,0)
   #Animating Sprites
   Player = Sprites.AnimatedSpriteGroup("Intergalactic-Intruders\Test.gif",screen_width//2,screen_height//2)
   PosX = 0
   PosY = 0

  

 
   while True:
      clock.tick(24)
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
      if PosX >800:
         PosX = 0
      if PosY <-600:
         PosY = 0
      if PosY >0:
         PosY = -600
      Player.update(PosX,PosY) 
      Player.draw(screen)
      Mouse_pos = pygame.mouse.get_pos()

      for constants.Button in buttons :
         constants.Button.hovered = constants.Button.rect.collidepoint(Mouse_pos)
      
      for constants.Button in buttons :
         constants.Button.draw()
     # print(f"Pos x = {PosX} /n y = {PosY} ")
      pygame.display.flip()

     

      
        
       
    
    





