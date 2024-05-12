import pygame
import constants


def show_difficulty():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("DIFFICULTY")
    
    difficulty_running = True
    while difficulty_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if constants.BACK_BUTTON.collidepoint(event.pos):
                    pygame.display.set_caption("LEVELS")
                    return

        screen.fill(constants.PURPLE)
        
        # Render buttons
        easy_button = pygame.Rect((constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2, 300, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        medium_button = pygame.Rect((constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2, 300 + 1 * (constants.BUTTON_HEIGHT + constants.BUTTON_GAP), constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        hard_button = pygame.Rect((constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2, 300 + 2 * (constants.BUTTON_HEIGHT + constants.BUTTON_GAP), constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        
        
        
        constants.draw_button(screen, easy_button.x, easy_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "EASY")
        constants.draw_button(screen, medium_button.x, medium_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "MEDIUM")
        constants.draw_button(screen, hard_button.x, hard_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "HARD")
        
        
        # Render back button with border
        pygame.draw.rect(screen, constants.RED, constants.BACK_BUTTON)
        pygame.draw.rect(screen, constants.BLACK, constants.BACK_BUTTON, 2)  # Draw border
        back_text = constants.FONT.render("BACK", True, constants.BLACK)
        screen.blit(back_text, (constants.BACK_BUTTON.x + 20, constants.BACK_BUTTON.y + 10))
        
        pygame.display.update()