import pygame
import constants
import sounds

def Show_Audio():
    pygame.init()
    
    sounds.Space_Sound.play()
    
    screen = constants.screen
    pygame.display.set_caption("Audio Settings")

    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"settings")

    Audio_Buttons = [Back_button]
    
    audio_running = True

    # Initial slider values set to the middle


    # Apply initial volumes

    
    Slider_X = 400
    Slider_Y = 250
    Slider_Gap = 75
    
    Main_Volume_Slider = constants.Slider(" Main Volume :",Slider_X,Slider_Y,"MAIN")
    Music_Volume_Slider = constants.Slider(" Music Volume :",Slider_X,Slider_Y+Slider_Gap,"MUSIC")
    SFX_Volume_Slider = constants.Slider(" SFX  Volume :",Slider_X,Slider_Y+Slider_Gap*2,"SFX")
    Volume_Sliders = [Main_Volume_Slider,Music_Volume_Slider,SFX_Volume_Slider]
    Volume_Sliders_test = constants.sliderlist()
    Volume_Sliders_test.AddSlider("Main Volume :","MAIN")
    Volume_Sliders_test.AddSlider("Music Volume :","MUSIC")
    Volume_Sliders_test.AddSlider("SFX Volume :","SFX")

    Volume_Sliders_test.FormatSliders()
    i = 0
    Page_label = constants.TitleLable((screen.get_width()/2,100),72,"AUDIO SETTINGS",constants.BLUE_DARK,True,True)

    while audio_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()
                for Sliders in Volume_Sliders_test:
                    if Sliders.Mute_Checkbox_Rect.collidepoint(event.pos):
                        Sliders.mute()
                    if Sliders.Slider_Thumb_Rect.collidepoint(event.pos):
                        Sliders.Dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                for Sliders in Volume_Sliders_test.Sliders:
                  Sliders.Dragging = False
                  Sliders.CheckMute()
            elif event.type == pygame.MOUSEMOTION:
                for Buttons in Audio_Buttons:
                    Buttons.hovered = Buttons.rect.collidepoint(event.pos)
                for Sliders in Volume_Sliders_test:
                    
                    if Sliders.Dragging == True:
                      Sliders.Drag(event.pos)
                      Sliders.Hovering_Slider_Track = True
                    else:
                        Sliders.Hovering_Slider_Track = Sliders.Slider_Track_Rect.collidepoint(event.pos)                      
                        Sliders.Hovering_MuteCheckbox = Sliders.Mute_Checkbox_Rect.collidepoint(event.pos)                      

        
        Page_label.draw()
        
        #Volume_Sliders_test.draw()
        for sliders in Volume_Sliders_test:
            sliders.draw()
            

        for Buttons in Audio_Buttons:
            Buttons.draw()
        pygame.display.update()


if __name__ == "__main__":
    Show_Audio()
