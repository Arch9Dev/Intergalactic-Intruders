import pygame
import constants
import gameplay


def show_difficulty():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("DIFFICULTY")
    
    
    # Define Buttons:
    Button_X = (constants.SCREEN_WIDTH - constants.BUTTON_WIDTH) // 2
    Button_Y = 300
    Button_Gap = constants.BUTTON_HEIGHT + constants.BUTTON_GAP
    Button_W = constants.BUTTON_WIDTH
    Button_H = constants.BUTTON_HEIGHT
    
    easy_button = constants.Button(screen, "EASY", Button_X, Button_Y, Button_W, Button_H, constants.Colour_Palettes["Red_Buttons"])
    medium_button = constants.Button(screen, "MEDIUM", Button_X, easy_button.Y + Button_Gap, Button_W, Button_H, constants.Colour_Palettes["Red_Buttons"])
    hard_button = constants.Button(screen, "HARD", Button_X, medium_button.Y + Button_Gap, Button_W, Button_H, constants.Colour_Palettes["Red_Buttons"])
    
    
    Difficulty_Buttons = [easy_button, medium_button, hard_button]
    
    pygame.key.set_repeat(100)
    
    
    difficulty_running = True
    while difficulty_running:
        screen.fill(constants.BLUE_LIGHT)
        title_rect = constants.TITLE_IMAGE.get_rect(center=(constants.SCREEN_WIDTH // 2, 150))
        screen.blit(constants.TITLE_IMAGE, title_rect)
               
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for button in Difficulty_Buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
                    
            if event.type == pygame.QUIT:
                difficulty_running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.rect.collidepoint(event.pos):
                    gameplay.show_gameplay() # EASY
                if medium_button.rect.collidepoint(event.pos):
                    gameplay.show_gameplay() # MEDIUM
                if hard_button.rect.collidepoint(event.pos):
                    gameplay.show_gameplay() # HARD                    


        
        for button in Difficulty_Buttons:
            button.draw()
        

        # Render title image
        title_rect = constants.TITLE_IMAGE.get_rect(center=(constants.SCREEN_WIDTH // 2, 150))
        screen.blit(constants.TITLE_IMAGE, title_rect)


        pygame.display.update()

    pygame.quit()
    quit()
