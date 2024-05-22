import pygame
import constants
import difficulty


def show_levels():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("LEVELS")

    # Define Buttons:
    Level1_Button = constants.Button("LEVEL 1", 0, 0, 0, 0, constants.Colour_Palettes["Orange_Buttons"])
    Level2_Button = constants.Button("LEVEL 2", 0, Level1_Button.rect.y + constants.BUTTON_GAP, 0, 0, constants.Colour_Palettes["Orange_Buttons"])
    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"PLAY")

    Level_Buttons = [Level1_Button, Level2_Button,Back_button]
    
    pygame.key.set_repeat(100)

    levels_running = True
    while levels_running:
        screen.fill(constants.BLUE_DARK)
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
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()
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