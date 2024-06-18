import pygame
import constants
import audio

import display
import controls

def show_settings():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("SETTINGS")
    
    Audio_Button = constants.Button("AUDIO",0,0,0,0,constants.Colour_Palettes["Green_Buttons"])
    Display_Button = constants.Button("DISPLAY",0,Audio_Button.rect.y,0,0,constants.Colour_Palettes["Green_Buttons"])
    Controls_Button = constants.Button("CONTROLS",0,Display_Button.rect.y,0,0,constants.Colour_Palettes["Green_Buttons"])
    Back_Button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"Main")
    Title_cords =  (screen.get_width()/2, screen.get_height()/5 )
    Settings_Title = constants.TitleLable(Title_cords,72,"SETTINGS",constants.BLUE_DARK,True,True)
    Settings_Buttons = [Audio_Button,Display_Button,Controls_Button,Back_Button]
    settings_running = True

    while settings_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0,0))
        screen.blit(constants.TITLE_IMAGE, constants.Logo_POS)
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
                elif Controls_Button.rect.collidepoint(event.pos):
                    controls.show_controls()  # Open controls settings
                elif Back_Button.rect.collidepoint(event.pos):
                    Back_Button.ReturnTo()

        # Render title
   
        Settings_Title.draw()
        for buttons in Settings_Buttons:
            buttons.draw()

        pygame.display.update()
