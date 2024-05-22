import pygame
import constants
import difficulty


def show_levels():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("LEVELS")

    # Define Buttons:
    Button_X = (constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2
    Button_Y = 300
    Button_Gap = constants.BUTTON_HEIGHT + constants.BUTTON_GAP
    Button_W = constants.BUTTON_WIDTH
    Button_H = constants.BUTTON_HEIGHT

    Level1_Button = constants.Button(screen, "LEVEL 1", Button_X, Button_Y, Button_W, Button_H, constants.Colour_Palettes["Red_Buttons"])
    Level2_Button = constants.Button(screen, "LEVEL 2", Button_X, Level1_Button.Y + Button_Gap, Button_W, Button_H, constants.Colour_Palettes["Red_Buttons"])

    Level_Buttons = [Level1_Button, Level2_Button]
    
    pygame.key.set_repeat(100)

    levels_running = True
    while levels_running:
        screen.fill(constants.BLUE_LIGHT)
        title_rect = constants.TITLE_IMAGE.get_rect(center=(constants.SCREEN_WIDTH // 2, 150))
        screen.blit(constants.TITLE_IMAGE, title_rect)
        
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for button in Level_Buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
                    
            if event.type == pygame.QUIT:
                levels_running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Level1_Button.rect.collidepoint(event.pos):
                    difficulty.show_difficulty()
                if Level2_Button.rect.collidepoint(event.pos):
                    difficulty.show_difficulty()
                    # Add change for higher levels
                    
                    
            
        for button in Level_Buttons:
            button.draw()
        

        # Render title image
        title_rect = constants.TITLE_IMAGE.get_rect(center=(constants.SCREEN_WIDTH // 2, 150))
        screen.blit(constants.TITLE_IMAGE, title_rect)


        pygame.display.update()

    pygame.quit()
    quit()