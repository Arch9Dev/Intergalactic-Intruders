import pygame
import constants

def show_display():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("DISPLAY")

    Colours ={
        0 : {"name": "WHITE","colour":(250, 249, 246)}, 
        1 : {"name": "BLACK","colour":(26, 26, 42)}, 
        2 : {"name": "GREY","colour":(190, 176, 167)},
        3 : {"name": "RED_DARK","colour":(255, 60, 0)},
        4 : {"name": "RED_DARKER","colour":(208, 48, 0)},
        5 : {"name": "RED_LIGHT","colour":(255, 0, 60)},
        6 : {"name": "BLUE_DARK","colour":(0, 60, 255)},
        7 : {"name": "BLUE_DARKER","colour":(0, 60, 200)},
        8 : {"name": "BLUE_LIGHT","colour":(70, 235, 255)},
        9 : {"name": "GREEN_DARK","colour":(20, 180, 40)},
        10 : {"name": "GREEN_DARKER","colour":(60, 150, 0)},
        11 : {"name": "GREEN_LIGHT","colour":(20, 230, 6)},
        12 : {"name": "ORANGE_DARK","colour":(255, 195, 0)},
        13 : {"name": "ORANGE_DARKER","colour":(255, 111, 0)},
        14 : {"name": "ORANGE_LIGHT","colour":(255, 235, 0)},
    }
    Page_label = constants.TitleLable((screen.get_width()/2,75),72,"DISPLAY SETTINGS",constants.BLUE_DARKER,True,True)

    lable_list = [Page_label]
    for i in Colours:

        lable_list.append(constants.TitleLable( ((25* i)+25,(50 * i)+50),15,Colours[i]["name"],Colours[i]["colour"],True,True))   
        

    
    Back_button = constants.BackButton(constants.Colour_Palettes["Red_Buttons"],"Settings")
    Display_Buttons =[Back_button]
    display_running = True
    while display_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0,0))
                    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
                for button in Display_Buttons:
                    button.hovered = button.rect.collidepoint(MousePos)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Back_button.rect.collidepoint(event.pos):
                    Back_button.ReturnTo()
        for button in Display_Buttons:
            button.draw()        # Render display content
        for lables in lable_list:
            lables.draw()
        Page_label.draw()

        # Render back button with border
        
        pygame.display.update()
