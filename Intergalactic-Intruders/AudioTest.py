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

    Audio_Buttons = [Back_button,Gunshot_Button]
    
    audio_running = True

    # Initial slider values set to the middle


    # Apply initial volumes

    
    Slider_X = 400
    Slider_Y = 250
    Slider_Gap = 75
    
    Main_Volume_Slider = constants.Slider("Main  Volume :",Slider_X,Slider_Y,"MAIN")
    Music_Volume_Slider = constants.Slider("Music Volume :",Slider_X,Slider_Y+Slider_Gap,"MUSIC")
    SFX_Volume_Slider = constants.Slider("SFX    Volume :",Slider_X,Slider_Y+Slider_Gap*2,"SFX")
    Volume_Sliders = [Main_Volume_Slider,Music_Volume_Slider,SFX_Volume_Slider]
    i = 0
    Page_label = constants.TileLable((screen.get_width()/3-15,75),72,"Audio Settings",constants.GREEN_LIGHT,None,True)

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
                    if Sliders.Mute_Checkbox_Rect.collidepoint(event.pos):
                        Sliders.mute()
                    if Sliders.Slider_Thumb_Rect.collidepoint(event.pos):
                        Sliders.Dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                for Sliders in Volume_Sliders:
                  Sliders.Dragging = False
                  Sliders.CheckMute()
            elif event.type == pygame.MOUSEMOTION:
                for Buttons in Audio_Buttons:
                    Buttons.hovered = Buttons.rect.collidepoint(event.pos)
                for Sliders in Volume_Sliders:
                    
                    if Sliders.Dragging == True:
                      Sliders.Drag(event.pos)
                      Sliders.Hovering_Slider_Track = True
                    else:
                        Sliders.Hovering_Slider_Track = Sliders.Slider_Track_Rect.collidepoint(event.pos)                      
                        Sliders.Hovering_MuteCheckbox = Sliders.Mute_Checkbox_Rect.collidepoint(event.pos)                      

        
        Page_label.draw()
        
        for Sliders in Volume_Sliders:
            Sliders.draw()
            
        constants.TileLable((100,100),24,"TESTING Hellow world ",constants.RED_LIGHT,None,True)

        for Buttons in Audio_Buttons:
            Buttons.draw()
        pygame.display.update()


   
