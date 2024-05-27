import pygame
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
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("MAIN MENU")
    
    # Define buttons
    Button_X = (constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2
    Button_Y = 300
    Button_Gap = constants.BUTTON_HEIGHT + constants.BUTTON_GAP
    Button_W = constants.BUTTON_WIDTH
    Button_H = constants.BUTTON_HEIGHT
    
    # Buttons
    play_button = constants.Button(screen, "PLAY", Button_X, Button_Y, Button_W, Button_H, constants.Colour_Palettes["Red_Buttons"])
    tutorial_button = constants.Button(screen, "TUTORIAL", Button_X, play_button.y + Button_Gap, Button_W, Button_H, constants.Colour_Palettes["Red_Buttons"])
    settings_button = constants.Button(screen, "SETTINGS", Button_X, tutorial_button.y + Button_Gap, Button_W, Button_H, constants.Colour_Palettes["Red_Buttons"])
    quit_button = constants.Button(screen, "QUIT", Button_X, settings_button.y + Button_Gap, Button_W, Button_H, constants.Colour_Palettes["Red_Buttons"])
    
    Main_Buttons = [play_button, tutorial_button, settings_button, quit_button]
    
    pygame.key.set_repeat(100)
    MainRunning = True
    
    # Main loop for the main menu
    while MainRunning:
        screen.fill(constants.BLUE_LIGHT)
        title_rect = constants.TITLE_IMAGE.get_rect(center=(constants.SCREEN_WIDTH // 2, 170))
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
