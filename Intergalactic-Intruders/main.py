import pygame
import constants
import tutorial
import settings
import play

import test



def main_menu():
    # Initialize Pygame
    pygame.init()

    # Create the main menu screen
    screen = constants.screen
    pygame.display.set_caption("MAIN MENU")

    # Buttons
    play_button = constants.Button( "PLAY", 0, 0,0,0, constants.Colour_Palettes["Green_Buttons"])
    tutorial_button = constants.Button( "TUTORIAL", 0,  play_button.rect.y,0,0, constants.Colour_Palettes["Green_Buttons"])
    settings_button = constants.Button( "SETTINGS", 0, tutorial_button.rect.y,0,0, constants.Colour_Palettes["Green_Buttons"])
    quit_button = constants.QuitButton( constants.Colour_Palettes["Red_Buttons"])
    
    Main_Buttons = [play_button, tutorial_button, settings_button, quit_button]

    pygame.key.set_repeat(100)
    MainRunning = True

    # Main loop for the main menu
    while MainRunning:
        # Blit the background image onto the screen
        screen.blit(constants.BACKGROUND_IMAGE, (0, 0))
        title_rect = constants.TITLE_IMAGE.get_rect(center=(constants.SCREEN_WIDTH // 2, 150))
        screen.blit(constants.TITLE_IMAGE, title_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MainRunning = False
            
            for button in Main_Buttons:
                button.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in Main_Buttons:
                    if button.clicked:
                        if button.text == "PLAY":
                            play.show_play()
                        elif button.text == "TUTORIAL":
                            tutorial.show_tutorial()
                        elif button.text == "SETTINGS":
                            settings.show_settings()
                        elif button.text == "QUIT":
                            MainRunning = False

        for button in Main_Buttons:
            button.draw()

        pygame.display.update()
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    main_menu()
