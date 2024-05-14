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

    # Making buttons
    # Button Vars
    Button_X = (screen_width - constants.BUTTON_WIDTH)// 2
    Button_Y = 300 
    Button_Gap =  constants.BUTTON_HEIGHT+ constants.BUTTON_GAP
    Button_W = constants.BUTTON_WIDTH
    Button_H = constants.BUTTON_HEIGHT
    # Buttons
    play_button = constants.Button(screen,"Play",Button_X,Button_Y ,Button_W,Button_H,Colours.Colour_Palettes["Red_Buttons"] )
    tutorial_button = constants.Button(screen,"TUTORIAL",Button_X,(play_button.y + Button_Gap) ,Button_W,Button_H,Colours.Colour_Palettes["Red_Buttons"] )
    settings_button = constants.Button(screen,"SETTINGS",Button_X,(tutorial_button.y + Button_Gap),Button_W,Button_H,Colours.Colour_Palettes["Red_Buttons"] )
    quit_button = constants.Button(screen,"QUIT",580,(settings_button.y + Button_Gap),Button_W,Button_H,Colours.Colour_Palettes["Red_Buttons"] )
    
    Main_Buttons = [play_button,tutorial_button,settings_button,quit_button]

            
    
    pygame.key.set_repeat(100)
    MainRunning = True
    # Main loop for the main menu
    while MainRunning:
        # Render title image
        screen.fill(Colours.SetColours.Blue_Light.value)
        title_rect = constants.TITLE_IMAGE.get_rect(center=(screen_width // 2, 150))
        screen.blit(constants.TITLE_IMAGE, title_rect) 
        
        #screen 
        i = 0
       
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                while  i < len(Main_Buttons):
                    Main_Buttons[i].hovered = Main_Buttons[i].rect.collidepoint(MousePos)
                    i += 1

            if event.type == pygame.QUIT:
                # Quit the game if the close button is clicked
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if any button is clicked
                if play_button.rect.collidepoint(event.pos):
                    #game.show_game()  # Open game screen
                    Main_Buttons.clear
                    Main = False
                    game_test.test()

                elif tutorial_button.rect.collidepoint(event.pos):
                    tutorial.show_tutorial()  # Open tutorial screen
                elif settings_button.rect.collidepoint(event.pos):
                    settings.show_settings()  # Open settings screen
                elif quit_button.rect.collidepoint(event.pos):
                    pygame.quit
                    quit()
        i = 0
        while  i < len(Main_Buttons):
            Main_Buttons[i].draw()
            i += 1


       
       
      

        pygame.display.update()
    Main_Buttons.clear

if __name__ == "__main__":
    main_menu()
