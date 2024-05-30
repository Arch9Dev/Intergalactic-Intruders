import pygame
import constants
import sounds

def show_audioTest():
    pygame.init()
    
    sounds.Space_Sound.play()
    
    screen = constants.screen
    pygame.display.set_caption("Audio Settings Test")

    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"settings")
    Audio_Buttons =[Back_button]
    
    audio_running = True

    # Initial slider values set to the middle
    volume_value = 0.5
    #music_value = 0.5
    #sound_effects_value = 0.5

    # Apply initial volumes
   # sounds.set_volume(volume_value)
   # sounds.set_space_sound_volume(music_value)
    #sounds.set_gunshot_sound_volume(sound_effects_value)

    Volume_Slider =  constants.Slider(volume_value," Volume Slider Test ",500,200)

    while audio_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()
                elif Volume_Slider.Circle_Rect.collidepoint(event.pos):
                    Volume_Slider.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if Volume_Slider.dragging :
                    Volume_Slider.dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if Volume_Slider.dragging :
                    Volume_Slider.Drag(event.pos)
        
        

        
        y_offset = 50

        for line in constants.AUDIO_TEXT:
            text_surface = constants.FONT.render(line, True, constants.BLACK)
            text_rect = text_surface.get_rect(center=(constants.SCREEN_WIDTH // 2, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += 30
        
        Volume_Slider.draw()
        Back_button.draw()
        pygame.display.update()


   
