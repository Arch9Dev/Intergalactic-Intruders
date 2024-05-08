import pygame
import constants
import audio
import display
import controls

def show_settings():
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Settings")

    settings_running = True
    while settings_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if audio_button.collidepoint(event.pos):
                    audio.show_audio()  # Open audio settings
                elif display_button.collidepoint(event.pos):
                    display.show_display()  # Open display settings
                elif controls_button.collidepoint(event.pos):
                    controls.show_controls()  # Open controls settings
                elif constants.BACK_BUTTON.collidepoint(event.pos):
                    return  # Return to main menu when the "Back" button is clicked

        screen.fill(constants.PURPLE)

        # Render title
        title_text = constants.TITLE_FONT.render("SETTINGS", True, constants.BLACK)
        title_rect = title_text.get_rect(center=(screen_width // 2, 50))
        screen.blit(title_text, title_rect)

        # Render buttons
        audio_button = pygame.Rect((screen_width - constants.BUTTON_WIDTH) // 2, 200, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        display_button = pygame.Rect((screen_width - constants.BUTTON_WIDTH) // 2, 200 + constants.BUTTON_HEIGHT + constants.BUTTON_GAP, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        controls_button = pygame.Rect((screen_width - constants.BUTTON_WIDTH) // 2, 200 + 2 * (constants.BUTTON_HEIGHT + constants.BUTTON_GAP), constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)

        constants.draw_button(screen, audio_button.x, audio_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "Audio")
        constants.draw_button(screen, display_button.x, display_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "Display")
        constants.draw_button(screen, controls_button.x, controls_button.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "Controls")
        
        # Render back button with border
        pygame.draw.rect(screen, constants.RED, constants.BACK_BUTTON)
        pygame.draw.rect(screen, constants.BLACK, constants.BACK_BUTTON, 2)  # Draw border
        back_text = constants.FONT.render("Back", True, constants.BLACK)
        screen.blit(back_text, (constants.BACK_BUTTON.x + 20, constants.BACK_BUTTON.y + 10))

        pygame.display.update()
