import pygame
import tutorial
import settings
import play
import constants
import audio

def main_menu():
    # Initialize Pygame
    pygame.init()
    
    # Create the main menu screen
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("MAIN MENU")

    # Main loop for the main menu
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game if the close button is clicked
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if any button is clicked
                if play_button.collidepoint(event.pos):
                    play.show_play()  # OPEN PLAY SCREEN
                elif tutorial_button.collidepoint(event.pos):
                    tutorial.show_tutorial()  # Open tutorial screen
                elif settings_button.collidepoint(event.pos):
                    settings.show_settings()  # Open settings screen
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()

        screen.fill(constants.PURPLE)

        # Render title image
        title_rect = constants.TITLE_IMAGE.get_rect(center=(constants.SCREEN_WIDTH // 2, 150))
        screen.blit(constants.TITLE_IMAGE, title_rect)

        # Render buttons
        play_button = pygame.Rect((constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2, 300, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        tutorial_button = pygame.Rect((constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2, 300 + constants.BUTTON_HEIGHT + constants.BUTTON_GAP, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        settings_button = pygame.Rect((constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2, 300 + 2 * (constants.BUTTON_HEIGHT + constants.BUTTON_GAP), constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        quit_button = pygame.Rect(constants.SCREEN_WIDTH - constants.BUTTON_WIDTH - 20, constants.SCREEN_HEIGHT - constants.BUTTON_HEIGHT - 20, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)

        constants.draw_button(screen, play_button.x, play_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "PLAY")
        constants.draw_button(screen, tutorial_button.x, tutorial_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "TUTORIAL")
        constants.draw_button(screen, settings_button.x, settings_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "SETTINGS")
        constants.draw_button(screen, quit_button.x, quit_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "QUIT")

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
