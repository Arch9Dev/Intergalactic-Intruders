import pygame
import constants
import sounds

def Show_Audio():
    pygame.init()
    
    sounds.Space_Sound.play()
    
    screen = constants.screen
    pygame.display.set_caption("Audio Settings")

    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"], "settings")

    Audio_Buttons = [Back_button]
    
    audio_running = True

    
  

    Volume_Sliders_test = constants.sliderlist()
    Volume_Sliders_test.AddSlider("Main Volume :", "MAIN")
    Volume_Sliders_test.AddSlider("Music Volume :", "MUSIC")
    Volume_Sliders_test.AddSlider("SFX Volume :", "SFX")
    Volume_Sliders_test.FormatSliders()


    while audio_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()
                for Sliders in Volume_Sliders_test.Sliders:
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
                for Sliders in Volume_Sliders_test.Sliders:
                    if Sliders.Dragging:
                        Sliders.Drag(event.pos)
                        Sliders.Hovering_Slider_Track = True
                    else:
                        Sliders.Hovering_Slider_Track = Sliders.Slider_Track_Rect.collidepoint(event.pos)
                        Sliders.Hovering_MuteCheckbox = Sliders.Mute_Checkbox_Rect.collidepoint(event.pos)

        screen.blit(constants.AUDIO_IMAGE,(0,0))
        for sliders in Volume_Sliders_test.Sliders:
            sliders.draw()

        for Buttons in Audio_Buttons:
            Buttons.draw()
        
        pygame.display.update()

if __name__ == "__main__":
    Show_Audio()
