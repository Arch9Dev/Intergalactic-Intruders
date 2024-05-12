import pygame
import constants
import difficulty


def show_levels():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("LEVELS")

    tutorials_running = True
    while tutorials_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if level1.collidepoint(event.pos):
                    difficulty.show_difficulty()
                elif constants.BACK_BUTTON.collidepoint(event.pos):
                    pygame.display.set_caption("PLAY")
                    return
            
            
        screen.fill(constants.PURPLE)

        # Render display content
        y_offset = 50
        for line in constants.LEVELS_TEXT:
            text_surface = constants.FONT.render(line, True, constants.BLACK)
            text_rect = text_surface.get_rect(center=(constants.SCREEN_WIDTH // 2, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += 30
            
            
        # Render level placeholder
        # Render buttons
        level1 = pygame.Rect((constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2, 300, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)

        constants.draw_button(screen, level1.x, level1.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "LEVEL1")


        # Render back button with border
        pygame.draw.rect(screen, constants.RED, constants.BACK_BUTTON)
        pygame.draw.rect(screen, constants.BLACK, constants.BACK_BUTTON, 2)  # Draw border
        back_text = constants.FONT.render("BACK", True, constants.BLACK)
        screen.blit(back_text, (constants.BACK_BUTTON.x + 20, constants.BACK_BUTTON.y + 10))

        pygame.display.update()
