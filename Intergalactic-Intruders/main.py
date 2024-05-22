import pygame
import tutorial
import settings
import play
import constants

def main_menu():
    
    pygame.init()

    # Initialize Pygame
    
    # Create the main menu screen
    #screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.RESIZABLE)
    screen = constants.screen
    pygame.display.set_caption("MAIN MENU")

    # Define buttons
    
    
    # Buttons
    play_button = constants.Button(screen, "PLAY", 0, 0,0,0, constants.Colour_Palettes["Red_Buttons"])
    tutorial_button = constants.Button(screen, "TUTORIAL", 0,  (play_button.Y + constants.Button_Gap),0,0, constants.Colour_Palettes["Red_Buttons"])
    settings_button = constants.Button(screen, "SETTINGS", 0, (tutorial_button.Y + constants.Button_Gap),0,0, constants.Colour_Palettes["Red_Buttons"])
    quit_button = constants.Button(screen, "QUIT", 0, (settings_button.Y + constants.Button_Gap),0,0,  constants.Colour_Palettes["Red_Buttons"])
    
    Main_Buttons = [play_button, tutorial_button, settings_button, quit_button]
    
    pygame.key.set_repeat(100)
    MainRunning = True

    # Main loop for the main menu
    while MainRunning:
        screen.fill(constants.BLUE_LIGHT)
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

main_menu()

#if __name__ == "__main__":
 #   main_menu()
