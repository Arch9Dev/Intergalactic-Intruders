import pygame
import constants
import audio
from test import show_test # type: ignore
import display
import controls

def show_settings():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("SETTINGS")
    if constants.FULLSCREEN :
       if pygame.display.is_fullscreen() == False:
            pygame.display.toggle_fullscreen()
    Return_Page = "main"
    Audio_Button = constants.Button("AUDIO",0,0,0,0,constants.Colour_Palettes["Green_Buttons"])
    Display_Button = constants.Button("DISPLAY",0,Audio_Button.rect.y,0,0,constants.Colour_Palettes["Green_Buttons"])
    Tutorial_Button = constants.Button("TUTORIAL",0,Display_Button.rect.y,0,0,constants.Colour_Palettes["Green_Buttons"])
    if constants.paused:
        Return_Page = "Paused"
    Back_Button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],F"{Return_Page}")
    Settings_Buttons = [Audio_Button,Display_Button,Tutorial_Button,Back_Button]
    settings_running = True

    while settings_running:
        screen.blit(constants.SETTINGS_IMAGE, (0,0))
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
                    audio.Show_Audio()
                elif Display_Button.rect.collidepoint(event.pos):
                    display.show_display()  # Open display settings
                elif Tutorial_Button.rect.collidepoint(event.pos):
                    controls.show_controls()  # Open controls settings
                elif Back_Button.rect.collidepoint(event.pos):
                    Back_Button.ReturnTo()


        for buttons in Settings_Buttons:
            buttons.draw()

        pygame.display.update()