import pygame
import constants
import levels
import timetrial

def show_game():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Game")

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if levels_button.collidepoint(event.pos):
                    levels.show_levels()
                elif timetrial_button.collidepoint(event.pos):
                    timetrial.show_timetrial()
                elif constants.BACK_BUTTON.collidepoint(event.pos):
                    return  # Return to main menu when the "Back" button is clicked

        screen.fill(constants.PURPLE)

        # Render game content
        # Render buttons
        levels_button = pygame.Rect((constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2, 300, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        timetrial_button = pygame.Rect((constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2, 300 + 2 * (constants.BUTTON_HEIGHT + constants.BUTTON_GAP), constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)

        constants.draw_button(screen, levels_button.x, levels_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "LEVELS")
        constants.draw_button(screen, timetrial_button.x, timetrial_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "TIME TRIAL")


        # Render back button with border
        pygame.draw.rect(screen, constants.RED, constants.BACK_BUTTON)
        pygame.draw.rect(screen, constants.BLACK, constants.BACK_BUTTON, 2)  # Draw border
        back_text = constants.FONT.render("BACK", True, constants.BLACK)
        screen.blit(back_text, (constants.BACK_BUTTON.x + 20, constants.BACK_BUTTON.y + 10))

        pygame.display.update()
