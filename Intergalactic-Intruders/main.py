import pygame
import tutorial
import settings
import game
import constants
import game_test

def main_menu():
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Main Menu")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    #game.show_game()  # Open game screen
                    game_test.test()
                elif tutorial_button.collidepoint(event.pos):
                    tutorial.show_tutorial()  # Open tutorial screen
                elif settings_button.collidepoint(event.pos):
                    settings.show_settings()  # Open settings screen


        screen.fill(constants.PURPLE)


        # Render title image
        title_rect = constants.TITLE_IMAGE.get_rect(center=(screen_width // 2, 150))
        screen.blit(constants.TITLE_IMAGE, title_rect)


        # Render buttons
        play_button = pygame.Rect((screen_width - constants.BUTTON_WIDTH) // 2, 300, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        tutorial_button = pygame.Rect((screen_width - constants.BUTTON_WIDTH) // 2, 300 + constants.BUTTON_HEIGHT + constants.BUTTON_GAP, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        settings_button = pygame.Rect((screen_width - constants.BUTTON_WIDTH) // 2, 300 + 2 * (constants.BUTTON_HEIGHT + constants.BUTTON_GAP), constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)


        constants.draw_button(screen, play_button.x, play_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "PLAY")
        constants.draw_button(screen, tutorial_button.x, tutorial_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "TUTORIAL")
        constants.draw_button(screen, settings_button.x, settings_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "SETTINGS")


        pygame.display.update()


if __name__ == "__main__":
    main_menu()