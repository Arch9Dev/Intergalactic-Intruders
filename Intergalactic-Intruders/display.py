import pygame
import constants

def show_display():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("DISPLAY")
    fullscreen_Button = constants.Button("FULL SCREEN",screen.get_width()/2-100,screen.get_height()/7*5,0,0,constants.Colour_Palettes["Green_Buttons"])

    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"Settings")
    Display_Buttons =[Back_button,fullscreen_Button]
    display_running = True

    Slider= constants.Gammer_Slider(screen.get_width()/2-100,screen.get_height()/5*3)
    while display_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0,0))
                    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                if Slider.Dragging :
                    Slider.Drag(event.pos)
                    Slider.Hovering_Slider_Track = True
                if Slider.Slider_Track_Rect.collidepoint(event.pos):
                    Slider.Hovering_Slider_Track = True
                else:
                    Slider.Hovering_Slider_Track = False
                for button in Display_Buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Slider.Slider_Thumb_Rect.collidepoint(event.pos):
                    Slider.Dragging =True
                if fullscreen_Button.rect.collidepoint(event.pos):
                   # pygame.display.toggle_fullscreen()
                    #constants.FULLSCREEN = pygame.display.is_fullscreen()
                    pass
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()
            if event.type == pygame.MOUSEBUTTONUP:
                Slider.Dragging = False
                
        for button in Display_Buttons:
            button.draw()        # Render display content
               
        
        Slider.draw()
        
        

       
        pygame.display.update() 


        pygame.display.update()

