import pygame
import tutorial
import settings
import play
import constants
import game_test
import Colours

def main_menu():
    # Initialize Pygame
    pygame.init()
    
    # Create the main menu screen
    screen_width = constants.SCREEN_WIDTH
    screen_height = constants.SCREEN_HEIGHT
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("MAIN MENU")

    pygame.key.set_repeat(100)

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
                    #game.show_game()  # Open game screen
                    game_test.test()
                elif tutorial_button.collidepoint(event.pos):
                    tutorial.show_tutorial()  # Open tutorial screen
                elif settings_button.collidepoint(event.pos):
                    settings.show_settings()  # Open settings screen
                elif quit_button.collidepoint(event.pos):
                    pygame.quit
                    quit()


        screen.fill(Colours.SetColours.Blue_Light.value)


        # Render title image
        title_rect = constants.TITLE_IMAGE.get_rect(center=(screen_width // 2, 150))
        screen.blit(constants.TITLE_IMAGE, title_rect) 
        # Render buttons
        Button_X = (screen_width - constants.BUTTON_WIDTH)// 2
        Button_Y = 300 
        Button_Gap =  constants.BUTTON_HEIGHT+ constants.BUTTON_GAP
        Button_W = constants.BUTTON_WIDTH
        Button_H = constants.BUTTON_HEIGHT

        play_button = constants.Button(screen,"Play",Button_X,Button_Y ,Button_W,Button_H,Colours.Colour_Palettes["Red_Buttons"] )
        tutorial_button = constants.Button(screen,"TUTORIAL",Button_X,(Button_Y+ Button_Gap) ,Button_W,Button_H,Colours.Colour_Palettes["Red_Buttons"] )
        settings_button = constants.Button(screen,"SETTINGS",Button_X,(Button_Y + (Button_Gap*2)),Button_W,Button_H,Colours.Colour_Palettes["Red_Buttons"] )
        quit_button = constants.Button(screen,"QUIT",((screen_width - Button_W) -20),((screen_width - Button_H) -20),Button_W,Button_H,Colours.Colour_Palettes["Red_Buttons"] )

        play_button.draw()
        tutorial_button.draw()
        settings_button.draw()
        quit_button.draw()
       # constants.draw_button(screen, play_button.x, play_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "PLAY" )
        #constants.draw_button(screen, tutorial_button.x, tutorial_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "TUTORIAL")
      #  constants.draw_button(screen, settings_button.x, settings_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "SETTINGS")
       # constants.draw_button(screen, quit_button.x, quit_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "QUIT")

        pygame.display.update()


if __name__ == "__main__":
    main_menu()