import pygame
import constants

def show_tutorial():
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("TUTORIAL")
    
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
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if constants.BACK_BUTTON.collidepoint(event.pos):
                    pygame.display.set_caption("MAIN MENU")
                    return  # Return to settings page when the "Back" button is clicked
                
        screen.fill(constants.PURPLE)

        # Render tutorial
        y_offset = starting_y
        for line in text_content:
            text_surface = xolonium_font.render(line, True, constants.BLACK)
            text_rect = text_surface.get_rect(midtop=(constants.SCREEN_WIDTH // 2, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += line_height
       
        # Render back button with border
        pygame.draw.rect(screen, constants.RED, constants.BACK_BUTTON)
        pygame.draw.rect(screen, constants.BLACK, constants.BACK_BUTTON, 2)  # Draw border
        back_text = constants.FONT.render("BACK", True, constants.BLACK)
        screen.blit(back_text, (constants.BACK_BUTTON.x + 20, constants.BACK_BUTTON.y + 10))

        pygame.display.update()

