import pygame
import constants
import sounds

def show_audio():
    pygame.init()
    
    sounds.Space_Sound.play()
    
    screen = constants.screen
    pygame.display.set_caption("Audio Settings")
    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"settings")
    Audio_Buttons =[Back_button]

    audio_running = True

    # Initial slider values set to the middle
    main_volume_value = 0.5
    music_value = 0.5
    sound_effects_value = 0.5

    # Apply initial volumes
    sounds.set_main_volume(main_volume_value)
    sounds.set_space_sound_volume(music_value)
    sounds.set_gunshot_sound_volume(sound_effects_value)

    # Define the radius of the circle
    circle_radius = 10

    # Determine the initial positions of the circles
    main_volume_circle_pos = (constants.MAIN_VOLUME_SLIDER_POS[0] + main_volume_value * constants.SLIDER_WIDTH - 100, constants.MAIN_VOLUME_SLIDER_POS[1] + 50)
    music_circle_pos = (constants.MUSIC_SLIDER_POS[0] + music_value * constants.SLIDER_WIDTH - 100, constants.MUSIC_SLIDER_POS[1] + 50)
    sound_effects_circle_pos = (constants.SOUND_EFFECTS_SLIDER_POS[0] + sound_effects_value * constants.SLIDER_WIDTH - 100, constants.SOUND_EFFECTS_SLIDER_POS[1] + 50)

    # Variables to track dragging state
    dragging_main_volume = False
    dragging_music = False
    dragging_sound_effects = False

    while audio_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()
                elif main_volume_circle_rect.collidepoint(event.pos):
                    dragging_main_volume = True
                elif music_circle_rect.collidepoint(event.pos):
                    dragging_music = True
                elif sound_effects_circle_rect.collidepoint(event.pos):
                    dragging_sound_effects = True
                elif gunshot_button_rect.collidepoint(event.pos):
                    sounds.play_gunshot()
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging_main_volume = False   
                dragging_music = False
                dragging_sound_effects = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging_main_volume:
                    main_volume_value = (event.pos[0] - (constants.MAIN_VOLUME_SLIDER_POS[0] - 100)) / constants.SLIDER_WIDTH
                    main_volume_value = max(0, min(1, main_volume_value))
                    main_volume_circle_pos = (int(constants.MAIN_VOLUME_SLIDER_POS[0] + main_volume_value * constants.SLIDER_WIDTH - 100), main_volume_circle_pos[1])
                    sounds.set_main_volume(main_volume_value)
                elif dragging_music:
                    music_value = (event.pos[0] - (constants.MUSIC_SLIDER_POS[0] - 100)) / constants.SLIDER_WIDTH
                    music_value = max(0, min(1, music_value))
                    music_circle_pos = (int(constants.MUSIC_SLIDER_POS[0] + music_value * constants.SLIDER_WIDTH - 100), music_circle_pos[1])
                    sounds.set_space_sound_volume(music_value)
                elif dragging_sound_effects:
                    sound_effects_value = (event.pos[0] - (constants.SOUND_EFFECTS_SLIDER_POS[0] - 100)) / constants.SLIDER_WIDTH
                    sound_effects_value = max(0, min(1, sound_effects_value))
                    sound_effects_circle_pos = (int(constants.SOUND_EFFECTS_SLIDER_POS[0] + sound_effects_value * constants.SLIDER_WIDTH - 100), sound_effects_circle_pos[1])
                    sounds.set_gunshot_sound_volume(sound_effects_value)


        # Render audio content
        y_offset = 50
        for line in constants.AUDIO_TEXT:
            text_surface = constants.FONT.render(line, True, constants.BLACK)
            text_rect = text_surface.get_rect(center=(constants.SCREEN_WIDTH // 2, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += 30

        # Render sliders with labels
        main_volume_label = constants.FONT.render("Main Volume", True, constants.BLACK)
        music_label = constants.FONT.render("Music", True, constants.BLACK)
        sound_effects_label = constants.FONT.render("Sound Effects", True, constants.BLACK)

        # Draw labels
        screen.blit(main_volume_label, (constants.MAIN_VOLUME_SLIDER_POS[0] - 300, constants.MAIN_VOLUME_SLIDER_POS[1] + 20))
        screen.blit(music_label, (constants.MUSIC_SLIDER_POS[0] - 300, constants.MUSIC_SLIDER_POS[1] + 20))
        screen.blit(sound_effects_label, (constants.SOUND_EFFECTS_SLIDER_POS[0] - 300, constants.SOUND_EFFECTS_SLIDER_POS[1] + 20))

        # Draw sliders
        pygame.draw.rect(screen, constants.BLACK, (constants.MAIN_VOLUME_SLIDER_POS[0] - 100, constants.MAIN_VOLUME_SLIDER_POS[1] + 40, constants.SLIDER_WIDTH, constants.SLIDER_HEIGHT))
        pygame.draw.rect(screen, constants.BLACK, (constants.MUSIC_SLIDER_POS[0] - 100, constants.MUSIC_SLIDER_POS[1] + 40, constants.SLIDER_WIDTH, constants.SLIDER_HEIGHT))
        pygame.draw.rect(screen, constants.BLACK, (constants.SOUND_EFFECTS_SLIDER_POS[0] - 100, constants.SOUND_EFFECTS_SLIDER_POS[1] + 40, constants.SLIDER_WIDTH, constants.SLIDER_HEIGHT))

        # Render white circles on sliders
        main_volume_circle_pos = (constants.MAIN_VOLUME_SLIDER_POS[0] + main_volume_value * constants.SLIDER_WIDTH - 100, constants.MAIN_VOLUME_SLIDER_POS[1] + 50)
        main_volume_circle_rect = pygame.draw.circle(screen, constants.WHITE, main_volume_circle_pos, circle_radius)
        music_circle_rect = pygame.draw.circle(screen, constants.WHITE, music_circle_pos, circle_radius)
        sound_effects_circle_rect = pygame.draw.circle(screen, constants.WHITE, sound_effects_circle_pos, circle_radius)

        # Render gunshot button
        gunshot_button_rect = pygame.Rect(constants.SCREEN_WIDTH // 2 - constants.BUTTON_WIDTH // 2, 500, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        constants.draw_gunshot_button(screen, gunshot_button_rect.x, gunshot_button_rect.y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT, "GUNSHOT")

        Back_button.draw()

        pygame.display.update()
