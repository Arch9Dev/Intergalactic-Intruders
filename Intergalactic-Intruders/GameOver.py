import pygame
import constants
import play
import gameplay

def show_GameOver():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("GAME OVER")
    
    Page_label = constants.TitleLable((screen.get_width()/2,screen.get_height()/3),130,"GAME OVER",constants.RED_DARKER,True,True)

    offset  = screen.get_width()/15
    left_offset =  0 + offset
    Right_offset = screen.get_width() - (constants.BUTTON_WIDTH + offset*2)
    Height_Offset = screen.get_width()/6 *3
    ReTry_Button = constants.Button("RETRY",left_offset,Height_Offset,offset,offset,constants.Colour_Palettes["Green_Buttons"])
    QUIT_Button = constants.Button("QUIT",Right_offset,Height_Offset,offset,offset,constants.Colour_Palettes["Red_Buttons"])

    GameOver_Buttons =[ReTry_Button,QUIT_Button]
    display_running = True
    while display_running:
        screen.blit(constants.BACKGROUND_IMAGE, (0,0))
                    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MousePos = pygame.mouse.get_pos()
            for button in GameOver_Buttons:
                button.handle_event(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in GameOver_Buttons:
                  if button.clicked:
                        if QUIT_Button.clicked:
                            play.show_play()
                        elif ReTry_Button.clicked:
                            gameplay.show_gameplay()

                
    
        for button in GameOver_Buttons:
            button.draw()        # Render display content

        Page_label.draw()


        pygame.display.update()



if __name__ == "__main__":
   show_GameOver()