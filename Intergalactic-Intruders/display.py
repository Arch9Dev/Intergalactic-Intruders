import pygame
import constants

def show_display():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("DISPLAY")
    
    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"Settings")
    Display_Buttons =[Back_button]
    display_running = True
    while display_running:
       
                    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for button in Display_Buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()

        screen.fill(constants.GREY)
        for button in Display_Buttons:
            button.draw()        # Render display content
        y_offset = 50
        for line in constants.DISPLAY_TEXT:
            text_surface = constants.FONT.render(line, True, constants.BLACK)
            text_rect = text_surface.get_rect(center=(constants.SCREEN_WIDTH // 2, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += 30

        # Render back button with border
        
        pygame.display.update()
