import pygame
import constants
import tutorial
import settings
import play
import constants
import sounds


def main_menu():
    # Initialize Pygame
    pygame.init()

    
    # Initialize sound settings
    sounds.set_main_volume(sounds.get_main_volume())
    sounds.set_space_sound_volume(sounds.get_space_sound_volume())
    sounds.set_gunshot_sound_volume(sounds.get_gunshot_sound_volume())
    
    # Create the main menu screen
    screen = constants.screen
    pygame.display.set_caption("MAIN MENU")

    # Buttons
    play_button = constants.Button( "PLAY", 0, 0,0,0, constants.Colour_Palettes["Orange_Buttons"])
    tutorial_button = constants.Button( "TUTORIAL", 0,  play_button.rect.y,0,0, constants.Colour_Palettes["Orange_Buttons"])
    settings_button = constants.Button( "SETTINGS", 0, tutorial_button.rect.y,0,0, constants.Colour_Palettes["Orange_Buttons"])
    quit_button = constants.QuitButton( constants.Colour_Palettes["Orange_Buttons"])
    
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
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for button in Main_Buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
                    
            if event.type == pygame.QUIT:
                MainRunning = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(event.pos):
                    play.show_play()
                elif tutorial_button.rect.collidepoint(event.pos):
                    tutorial.show_tutorial()
                elif settings_button.rect.collidepoint(event.pos):
                    settings.show_settings()
                elif quit_button.rect.collidepoint(event.pos):
                    MainRunning = False
        
        for button in Main_Buttons:
            button.draw()
        
        pygame.display.update()
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    main_menu()
