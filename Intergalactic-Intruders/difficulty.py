import pygame
import constants


def show_difficulty():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Difficulty")
    
    difficulty_running = True
    while difficulty_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if constants.BACK_BUTTON.collidepoint(event.pos):
                    return  # Return to settings page when the "Back" button is clicked

        screen.fill(constants.PURPLE)
        
        # Render buttons
        easy_button = pygame.Rect((constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2, 300, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        medium_button = pygame.Rect((constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2, 300 + 1 * (constants.BUTTON_HEIGHT + constants.BUTTON_GAP), constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        hard_button = pygame.Rect((constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2, 300 + 2 * (constants.BUTTON_HEIGHT + constants.BUTTON_GAP), constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        
        
        
        constants.draw_button(screen, easy_button.x, easy_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "EASY")
        constants.draw_button(screen, medium_button.x, medium_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "MEDIUM")
        constants.draw_button(screen, hard_button.x, hard_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "HARD")
        
        pygame.display.update()