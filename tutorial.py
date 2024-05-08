import pygame
import constants

def show_display():
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Display Settings")

    display_running = True
    while display_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if constants.BACK_BUTTON.collidepoint(event.pos):
                    return  # Return to settings page when the "Back" button is clicked

        screen.fill(constants.PURPLE)

        # Render display content
        y_offset = 50
        for line in constants.DISPLAY_TEXT:
            text_surface = constants.FONT.render(line, True, constants.BLACK)
            text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += 30

        # Render back button with border
        pygame.draw.rect(screen, constants.RED, constants.BACK_BUTTON)
        pygame.draw.rect(screen, constants.BLACK, constants.BACK_BUTTON, 2)  # Draw border
        back_text = constants.FONT.render("Back", True, constants.BLACK)
        screen.blit(back_text, (constants.BACK_BUTTON.x + 20, constants.BACK_BUTTON.y + 10))

        pygame.display.update()
