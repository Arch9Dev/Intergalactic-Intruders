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
    
    
    Player = Sprites.AnimatedSpriteGroup("Intergalactic-Intruders\Test.gif",screen.get_width() //2 ,screen.get_height() //2)

    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Player.update() 
        screen.fill((127, 192, 255))
        Player.draw(screen)
       
        pygame.display.flip()

     

      
        
       
    
    





