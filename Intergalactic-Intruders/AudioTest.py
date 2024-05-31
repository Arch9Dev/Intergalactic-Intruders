import pygame
import constants
import sounds

def show_audioTest():
    pygame.init()
    
    sounds.Space_Sound.play()
    
    screen = constants.screen
    pygame.display.set_caption("Audio Settings Test")

    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"settings")
    Gunshot_Button = constants.Button("TEST FIRE",constants.SCREEN_WIDTH // 2 - constants.BUTTON_WIDTH // 2, 500,0,0,constants.Colour_Palettes["Red_Buttons"])

    Audio_Buttons =[Back_button,Gunshot_Button]
    
    audio_running = True

    # Initial slider values set to the middle
    Main_value = 0.5
    Music_value = 0.5
    Sfx_value = 0.5

    # Apply initial volumes
    sounds.set_main_volume(Main_value)
    sounds.set_space_sound_volume(Music_value)
    sounds.set_gunshot_sound_volume(Sfx_value)
    
    Slider_X = 400
    Slider_Y = 250
    Slider_Gap = 75
    
    Main_Volume_Slider = constants.Slider(Main_value,"Main  Volume :",Slider_X,Slider_Y,"MAIN")
    Music_Volume_Slider = constants.Slider(Music_value,"Music Volume :",Slider_X,Slider_Y+Slider_Gap,"MUSIC")
    SFX_Volume_Slider = constants.Slider(Sfx_value,"SFX    Volume :",Slider_X,Slider_Y+Slider_Gap*2,"SFX")

    Volume_Sliders = [Main_Volume_Slider,Music_Volume_Slider,SFX_Volume_Slider]
    i = 0
   
    while audio_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()
                if Gunshot_Button.rect.collidepoint(event.pos):
                    sounds.play_gunshot()
                for Sliders in Volume_Sliders:
                    if Sliders.Mute_Checkbox.collidepoint(event.pos):

                        Sliders.mute()
                    if Sliders.Circle_Rect.collidepoint(event.pos):
                        Sliders.Dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                for Sliders in Volume_Sliders:
                  Sliders.Dragging = False
            elif event.type == pygame.MOUSEMOTION:
                for Buttons in Audio_Buttons:
                    Buttons.hovered = Buttons.rect.collidepoint(event.pos)
                for Sliders in Volume_Sliders:
                  if Sliders.Dragging == True:
                      Sliders.Drag(event.pos)
        
        

        
        y_offset = 50

        for line in constants.AUDIO_TEXT:
            text_surface = constants.FONT.render(line, True, constants.BLACK)
            text_rect = text_surface.get_rect(center=(constants.SCREEN_WIDTH // 2, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += 30
        
        for Sliders in Volume_Sliders:
            Sliders.draw()
            

        for Buttons in Audio_Buttons:
            Buttons.draw()
        pygame.display.update()


   
