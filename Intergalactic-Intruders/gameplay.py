import pygame
import constants
import pygame
import constants

def show_gameplay():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("GAMEPLAY")

    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"levels")
    Gameplay_buttons = [Back_button]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for button in Gameplay_buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()

        screen.blit(constants.BACKGROUND_IMAGE, (0,0))
        # Placeholder content
        placeholder_text = constants.FONT.render("Gameplay Placeholder", True, constants.BLACK)
        screen.blit(placeholder_text, (constants.SCREEN_WIDTH // 2 - 100, constants.SCREEN_HEIGHT // 2))
        Back_button.draw()

        for button in Gameplay_buttons:
            button.draw()
        
        pygame.display.update()
