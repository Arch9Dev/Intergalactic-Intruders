import pygame
import constants
import play
import gameplay

def show_GameOver():
    pygame.init()
    screen = constants.screen
    pygame.display.set_caption("GAME OVER")
    
    Page_label = constants.TitleLable((screen.get_width()/2,screen.get_height()/5),130,"GAME OVER",constants.RED_DARKER,True,True)
    #these are just  Placeholder values
    Intruders_killed = 15  
    Accuracy = 90  #  Ps: percent in int 
    Time_Survived = 1250000 # PS: time in milliseconuds
    Level_Bonus = 16 
    BONUS = 100  
    FINAL_SCORE = int(round((Intruders_killed/Accuracy)*(Time_Survived/1000)*Level_Bonus,2) *100+BONUS) 
   
    Score_Text = f"""
    Intruders killed : {Intruders_killed}
    Accuracy : {Accuracy}%
    Time  : {int(Time_Survived/1000)}
    Level Bonus : {Level_Bonus}
 
    BONUS : {BONUS}
 
    FINAL SCORE : {FINAL_SCORE}"""
    Score_Output = constants.Screen_Text((screen.get_width()/22,screen.get_height()/6*1.75),32,Score_Text,constants.WHITE,False)
    offset  = screen.get_width()/15
    left_offset =  0 + offset
    Right_offset = screen.get_width() - (constants.BUTTON_WIDTH + offset*2)
    Height_Offset = screen.get_height()/6*4
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
        Score_Output.draw()

        pygame.display.update()



if __name__ == "__main__":
   show_GameOver()