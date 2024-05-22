import pygame
import constants

def show_tutorial():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("TUTORIAL")
    

    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"main")
    Tutorial_Buttons =[Back_button]
    xolonium_font = constants.load_xolonium_font(24)
    
    # Get the tutorial text from constants.py
    text_content = constants.TUTORIAL_TEXT

    # Calculate the total height of the text
    line_height = 30
    total_text_height = len(text_content) * line_height

    # Calculate the starting vertical position to center the text vertically
    starting_y = (constants.SCREEN_HEIGHT - total_text_height) // 2

    # Calculate the starting horizontal position to center the text horizontally with margins
    starting_x = (constants.SCREEN_WIDTH - (xolonium_font.size("W")[0] * max(len(line) for line in text_content))) // 2

    tutorials_running = True
    while tutorials_running:
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

                
        screen.fill(constants.BLUE_DARK)
        for button in Tutorial_Buttons:
            button.draw()

        # Render tutorial
        y_offset = starting_y
        for line in text_content:
            text_surface = xolonium_font.render(line, True, constants.BLACK)
            text_rect = text_surface.get_rect(midtop=(constants.SCREEN_WIDTH // 2, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += line_height
       
        # Render back button with border
        
        pygame.display.update()

