import pygame
import constants
import Sprites

def test():
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Main Menu")
   
    screen.fill(constants.PURPLE)
    
    title_text = constants.TITLE_FONT.render("Test", True, constants.BLACK)
    title_rect = title_text.get_rect(center=(screen_width // 2, 50))
    screen.blit(title_text, title_rect)
    
   # Player_Frames = [] 
    #for i in range(9) :
     #   Player_Frames.append(pygame.image.load(f"./Intergalactic-Intruders/images/PlayerShip/sprite_{i}.png").convert_alpha())

    #Current_Frame = 0 
    PlayerSprite = Sprites.PlayerSprites()
    PlayerSpriteGroup = pygame.sprite.Group(PlayerSprite)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        PlayerSpriteGroup.update()
        PlayerSpriteGroup.draw()
        pygame.display.flip()
        
       # screen.blit(Player_Frames[Current_Frame], 200,200)
       # Current_Frame = Current_Frame + 1 if (Current_Frame != 8) else 0
       # print(Current_Frame)
        
        #pygame.display.update()
    
    





