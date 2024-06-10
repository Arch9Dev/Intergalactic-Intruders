import pygame
import constants

def show_intro():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("INTRODUCTION")

    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"main")
    Tutorial_Buttons =[Back_button]
    

    intro_running = True
    while intro_running:
        screen.blit(constants.INTRO_IMAGE, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for button in Tutorial_Buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()

                
        for button in Tutorial_Buttons:
            button.draw()
        
        pygame.display.update()

