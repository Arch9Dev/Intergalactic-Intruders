import pygame
import constants
import audio
import display
import controls

def show_settings():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("SETTINGS")
    
    Audio_Button = constants.Button("Audio",0,0,0,0,constants.Colour_Palettes["Blue_Buttons"])
    Display_Button = constants.Button("Display",0,Audio_Button.rect.y,0,0,constants.Colour_Palettes["Blue_Buttons"])
    Controls_Button = constants.Button("Controls",0,Display_Button.rect.y,0,0,constants.Colour_Palettes["Blue_Buttons"])
    Back_Button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"Main")

    Settings_Buttons = [Audio_Button,Display_Button,Controls_Button,Back_Button]
    settings_running = True

    while settings_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for Buttons in Settings_Buttons:
                    Buttons.hovered = Buttons.rect.collidepoint(MousePos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Audio_Button.rect.collidepoint(event.pos):
                    audio.show_audio()  # Open audio settings
                elif Display_Button.rect.collidepoint(event.pos):
                    display.show_display()  # Open display settings
                elif Controls_Button.rect.collidepoint(event.pos):
                    controls.show_controls()  # Open controls settings
                elif Back_Button.rect.collidepoint(event.pos):
                    Back_Button.ReturnTo()

        screen.fill(constants.GREY)

        # Render title
        title_text = constants.TITLE_FONT.render("SETTINGS", True, constants.BLACK)
        title_rect = title_text.get_rect(center=(constants.SCREEN_WIDTH // 2, 50))
        screen.blit(title_text, title_rect)

        for buttons in Settings_Buttons:
            buttons.draw()

        pygame.display.update()
