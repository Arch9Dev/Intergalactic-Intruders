import pygame
import constants

def show_tutorial():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("TUTORIAL")
    

    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"main")
    Tutorial_Buttons =[Back_button]
    xolonium_font = constants.Font(24,"xolonium")
    
    # Get the tutorial text from constants.py

    # Calculate the total height of the text
    line_height = 30

    # Calculate the starting vertical position to center the text vertically

    # Calculate the starting horizontal position to center the text horizontally with margins
    Page_Title_Text = constants.TitleLable((screen.get_width()/2,screen.get_height()/7),72,"TUTORIAL",constants.BLUE_DARK,True,True)
    tutorial_TEXT = constants.TUTORIAL_Screen_Text(36,constants.WHITE)
    tutorials_running = True
    while tutorials_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for button in Tutorial_Buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()

                
        for button in Tutorial_Buttons:
            button.draw()

        tutorial_TEXT.draw()
        Page_Title_Text.draw()
        # Render back button with border
        
        pygame.display.update()

