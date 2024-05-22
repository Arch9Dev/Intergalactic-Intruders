import pygame
import constants
import gameplay


def show_difficulty():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("DIFFICULTY")
    
    


    
    easy_button = constants.Button("EASY", 0, 0, 0, 0, constants.Colour_Palettes["Green_Buttons"])
    medium_button = constants.Button("MEDIUM", 0, easy_button.rect.y , 0, 0, constants.Colour_Palettes["Blue_Buttons"])
    hard_button = constants.Button("HARD", 0, medium_button.rect.y , 0, 0, constants.Colour_Palettes["Red_Buttons"])
    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"levels")

    
    Difficulty_Buttons = [easy_button, medium_button, hard_button,Back_button]
    
    pygame.key.set_repeat(100)
    
    
    difficulty_running = True
    while difficulty_running:
        screen.fill(constants.Alabaster)
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
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()                    


        
        for button in Difficulty_Buttons:
            button.draw()
        

        # Render title image
        title_rect = constants.TITLE_IMAGE.get_rect(center=(constants.SCREEN_WIDTH // 2, 150))
        screen.blit(constants.TITLE_IMAGE, title_rect)


        pygame.display.update()

    pygame.quit()
    quit()
