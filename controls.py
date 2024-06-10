import pygame
import constants

def show_controls():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("CONTROLS")
    Page_label = constants.TitleLable((screen.get_width()/2,100),72,"CONTROL SETTINGS",constants.BLUE_DARKER,True,True)

    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"Settings")
    Control_Buttons =[Back_button]
    controls_running = True
    while controls_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for button in Control_Buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()
        for button in Control_Buttons:
            button.draw()
        Page_label.draw()
        # Load and render controls image
        controls_image = constants.CONTROLS_IMAGE
        controls_image_rect = controls_image.get_rect(center=(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2))
        screen.blit(controls_image, controls_image_rect)

        # Render back button with border
        
        pygame.display.update()
