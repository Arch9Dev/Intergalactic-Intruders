import pygame
import constants
import Gameplay

def show_controls():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("CONTROLS")
    Next_Button = constants.Button("NEXT",screen.get_width()/7*6,screen.get_height()/7,-90,-100,constants.Colour_Palettes["Green_Buttons"])
    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"Settings")
    Control_Buttons =[Back_button,Next_Button]
    controls_running = True         
    controls_image = constants.CONTROLS_IMAGE

    while controls_running:
        screen.blit(controls_image, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for button in Control_Buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Next_Button.rect.collidepoint(event.pos):
                    Gameplay.show_GAMEPLAY()
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()
        for button in Control_Buttons:
            button.draw()

        # Load and render controls image
       

        # Render back button with border
        
        pygame.display.update()
