import pygame
import constants
import levels
import timetrial

def show_play():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("PLAY")
    
    
    # Define Buttons
    Button_X = (constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2
    Button_Y = 300
    Button_Gap = constants.BUTTON_HEIGHT + constants.BUTTON_GAP
    Button_W = constants.BUTTON_WIDTH
    Button_H = constants.BUTTON_HEIGHT
    
    
    levels_button = constants.Button(screen, "LEVELS", Button_X, Button_Y, Button_W, Button_H, constants.Colour_Palettes["Red_Buttons"])
    timetrial_button = constants.Button(screen, "TUTORIAL", Button_X, levels_button.y + Button_Gap, Button_W, Button_H, constants.Colour_Palettes["Red_Buttons"])


    Play_Buttons = [levels_button, timetrial_button]
    
    pygame.key.set_repeat(100)
    play_running = True

    while play_running:
        # Render screen
        screen.fill(constants.BLUE_LIGHT)
        title_rect = constants.TITLE_IMAGE.get_rect(center=(constants.SCREEN_WIDTH // 2, 150))
        screen.blit(constants.TITLE_IMAGE, title_rect)
        
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

                
        
        for button in Play_Buttons:
            button.draw()
        

        # Render title image
        title_rect = constants.TITLE_IMAGE.get_rect(center=(constants.SCREEN_WIDTH // 2, 150))
        screen.blit(constants.TITLE_IMAGE, title_rect)


        

        pygame.display.update()
