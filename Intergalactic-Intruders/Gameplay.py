import pygame
import constants

def show_GAMEPLAY():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("GAMEPLAY")
    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"Controls")
    GAMEPLAY_Buttons =[Back_button]
    GAMEPLAY_running = True
    Gameplay_image = constants.GAMEPLAY_IMAGE

    while GAMEPLAY_running:
        screen.blit(Gameplay_image, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for button in GAMEPLAY_Buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()
        for button in GAMEPLAY_Buttons:
            button.draw()

        # Load and render GAMEPLAY image
            #  GAMEPLAY_image = constants.GAMEPLAY_IMAGE
            # GAMEPLAY_image_rect = GAMEPLAY_image.get_rect(center=(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2))
            #   screen.blit(GAMEPLAY_image, GAMEPLAY_image_rect)

        # Render back button with border
        
        pygame.display.update()
