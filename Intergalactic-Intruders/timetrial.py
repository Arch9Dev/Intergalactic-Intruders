import pygame
import constants


def show_timetrial(Time_trial):
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("TIME TRIAL")
    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"play")
    TimeTrial_Buttons = [Back_button]

    tutorials_running = True
    while tutorials_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for button in TimeTrial_Buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()
                    
        for button in TimeTrial_Buttons:
            button.draw()        # Render display content
        y_offset = 50
        for line in constants.TIMETRIAL_TEXT:
            text_surface = constants.FONT.render(line, True, constants.BLACK)
            text_rect = text_surface.get_rect(center=(constants.SCREEN_WIDTH // 2, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += 30

        # Render back button with border
        
        pygame.display.update()