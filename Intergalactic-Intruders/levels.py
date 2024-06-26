import pygame
import constants
import difficulty


def show_levels(Time_trial):
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("LEVELS")

    # Define Buttons:
    Level1_Button = constants.Button("LEVEL 1", 0, 0, 0, 0, constants.Colour_Palettes["Green_Buttons"])
    Level2_Button = constants.Button("LEVEL 2", 0, Level1_Button.rect.y + 1, 0, 0, constants.Colour_Palettes["Green_Buttons"])
    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"PLAY")

    Level_Buttons = [Level1_Button, Level2_Button,Back_button]
    
    pygame.key.set_repeat(100)

    levels_running = True
    
    #main loop 
    while levels_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0,0))
        screen.blit(constants.TITLE_IMAGE, constants.Logo_POS)
        
        
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
                    difficulty.show_difficulty(Time_trial, 1)
                if Level2_Button.rect.collidepoint(event.pos):
                    difficulty.show_difficulty(Time_trial, 2)
                    # Add change for higher levels

                    
                    
            
        for button in Level_Buttons:
            button.draw()
        

        # Render title image



        pygame.display.update()

    pygame.quit()
    quit()