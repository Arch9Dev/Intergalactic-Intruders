import pygame
import constants
import workin_game
import levels



def show_difficulty(Time_trial, level):
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("DIFFICULTY")


    easy_button = constants.Button("EASY", 0, 0, 0, 0, constants.Colour_Palettes["Green_Buttons"])
    medium_button = constants.Button("MEDIUM", 0, easy_button.rect.y , 0, 0, constants.Colour_Palettes["Orange_Buttons"])
    hard_button = constants.Button("HARD", 0, medium_button.rect.y , 0, 0, constants.Colour_Palettes["Red_Buttons"])
    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"levels")

    
    Difficulty_Buttons = [easy_button, medium_button, hard_button, Back_button]
    
    pygame.key.set_repeat(100)
    
    
    difficulty_running = True
    while difficulty_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0,0))
        screen.blit(constants.TITLE_IMAGE, constants.Logo_POS)
               
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for button in Difficulty_Buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
                    
            if event.type == pygame.QUIT:
                difficulty_running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in Difficulty_Buttons:
                    button.handle_event(event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in Difficulty_Buttons:
                        if button.clicked:
                            if button.text == "EASY":
                                workin_game.show_test(Time_trial, level, 0.75)
                            elif button.text == "MEDIUM":
                                workin_game.show_test(Time_trial, level, 1)
                            elif button.text == "HARD":
                                workin_game.show_test(Time_trial, level, 1.25)
                        if Back_button.rect.collidepoint(event.pos):
                            Back_button.ReturnTo()
        for button in Difficulty_Buttons:
            button.draw()
        


        pygame.display.update()

    pygame.quit()
    quit()
