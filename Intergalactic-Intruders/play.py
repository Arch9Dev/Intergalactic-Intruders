import pygame
import constants
import levels
import timetrial
import difficulty

def show_play():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("PLAY")
    

    
    levels_button = constants.Button("LEVELS", 0, 0, 0, 0, constants.Colour_Palettes["Green_Buttons"])
    timetrial_button = constants.Button( "TIME TRIAL", 0, levels_button.rect.y + levels_button.height, 0, 0, constants.Colour_Palettes["Green_Buttons"])
    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"MAIN")

    Play_Buttons = [levels_button, timetrial_button,Back_button]
    
    pygame.key.set_repeat(100)
    play_running = True

    while play_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0, 0))
        screen.blit(constants.TITLE_IMAGE, constants.Logo_POS)
        
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for Buttons in Play_Buttons:
                    Buttons.hovered = Buttons.rect.collidepoint(MousePos)
                    
            if event.type == pygame.QUIT:
                play_running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if levels_button.rect.collidepoint(event.pos):
                    levels.show_levels(False)
                elif timetrial_button.rect.collidepoint(event.pos):
                    difficulty.show_difficulty(True, 2)
                elif Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()

                
        
        for Buttons in Play_Buttons:
            Buttons.draw()
        

        # Render title image



        pygame.display.update()
        
    pygame.quit()
    quit()
