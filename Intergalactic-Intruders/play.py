import pygame
import constants
import levels
import timetrial
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
def drawGrid():
   WINDOW_WIDTH= constants.SCREEN_WIDTH
   WINDOWHEIGHT = constants.SCREEN_HEIGHT
   blocksize = 20  
   for x in range(0,blocksize,WINDOW_WIDTH):
        for y in range(0,blocksize, WINDOWHEIGHT):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            pygame.draw.rect(constants.screen, WHITE, rect, 1)  
def show_play():
    pygame.init()
   # screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    screen = constants.screen
    pygame.display.set_caption("PLAY")
    
    pygame.draw.line(screen,constants.BLACK,(0,0),(200,100),1)
    
    # Define Buttons
    
    
    levels_button = constants.Button(screen, "LEVELS",0,0,0,0, constants.Colour_Palettes["Red_Buttons"])
    timetrial_button = constants.Button(screen, "TIME TRIAL",0,levels_button.Y,0,0, constants.Colour_Palettes["Red_Buttons"])
    BackButton = constants.BackButton(screen,constants.Colour_Palettes["Red_Buttons"],"P")

    Play_Buttons = [levels_button, timetrial_button,BackButton]
    
    pygame.key.set_repeat(100)
    play_running = True

    while play_running:
        # Render screen
        screen.fill(constants.BLUE_LIGHT)
        title_rect = constants.TITLE_IMAGE.get_rect(center=(constants.SCREEN_WIDTH // 2, 150))
        screen.blit(constants.TITLE_IMAGE, title_rect)
        drawGrid()
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for button in Play_Buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
                    
            if event.type == pygame.QUIT:
                play_running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if levels_button.rect.collidepoint(event.pos):
                    levels.show_levels()
                elif timetrial_button.rect.collidepoint(event.pos):
                    timetrial.show_timetrial()
                elif BackButton.rect.collidepoint(event.pos):
                    BackButton.Returnpage()

                
        
        for button in Play_Buttons:
            button.draw()
        

        # Render title image
        title_rect = constants.TITLE_IMAGE.get_rect(center=(constants.SCREEN_WIDTH // 2, 150))
        screen.blit(constants.TITLE_IMAGE, title_rect)


        pygame.display.update()

pygame.quit()
quit()
