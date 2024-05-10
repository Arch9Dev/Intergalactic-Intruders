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
    
    
    Player = Sprites.AnimatedSpriteGroup("Intergalactic-Intruders\Test.gif",screen_width//2,screen_height//2)
    PosX = 0
    PosY = 0
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   PosX  -=1  if  PosX  > 0 else  PosX  
                if event.key == pygame.K_RIGHT:
                   PosX  +=1  if  PosX  < screen_width else PosX   
                if event.key == pygame.K_UP:
                   PosX  +=1  if  PosX  > screen_height else  PosX  
                if event.key == pygame.K_DOWN:
                   PosX  -=1  if  PosX  < 0 else PosX     
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Player.update(PosX,PosY) 
        screen.fill((127, 192, 255))
        Player.draw(screen)
       
        pygame.display.flip()

     

      
        
       
    
    





