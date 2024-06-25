import pygame
import constants
import main
import test
import random

def show_GameOver(AccuracyIN, DifficultyIN, current_time, Intruders_killedin):
    pygame.init() 
    constants.SCREEN_WIDTH =1000
    constants.SCREEN_HEIGHT = 800
    constants.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    screen = constants.screen
   
    pygame.display.set_caption("GAME OVER")
    
    Page_label = constants.TitleLabel((screen.get_width()/2,screen.get_height()/5),130,"GAME OVER",constants.RED_DARKER,True,True)
    #these are just  Placeholder values
    Difficulty = {"Easy": 10,"Medium":20,"Hard":30}
    Level_Bonus = {"Easy" : 100  ,"Medium" : 200 ,"Hard" : 300 }
    ENDED_GAME_DIFFICULTY = "Medium" if DifficultyIN == 1 else "Easy" if  DifficultyIN <= 0.75 else "Hard"
    Intruders_killed = Intruders_killedin  
    Accuracy = AccuracyIN  #  Ps: percent in int 
    Time_Survived = current_time # PS: time in milliseconuds
    BONUS = random.randint(1,100) 
    SCORE = (Intruders_killed*Difficulty[ENDED_GAME_DIFFICULTY]) + ((Accuracy/100)*10) + ((int(Time_Survived/1000)/30)*50)
    FINAL_SCORE =  int(SCORE + BONUS + Level_Bonus[ENDED_GAME_DIFFICULTY])
    
    Score_Text = """
 Intruders killed : 
 Accuracy : 
 Time  : 
 Level Bonus : 
 BONUS : 
 
 FINAL SCORE :""" 

    Score_Numbers =f"""
 {Intruders_killed} 
 {AccuracyIN}% 
 {int(Time_Survived/1000)} 
 {Level_Bonus[ENDED_GAME_DIFFICULTY]} 
 {BONUS} 
    
 {FINAL_SCORE} 
    """
    
    offset  = screen.get_width()/15
    left_offset =   offset
    Right_offset = screen.get_width() - (constants.BUTTON_WIDTH + offset*2)
    Mid_offset = left_offset/2 + Right_offset/2
    Height_Offset = screen.get_height()/6*4
    ReTry_Button = constants.Button("PLAY\nAGAIN",left_offset,Height_Offset,offset/3,offset/3,constants.Colour_Palettes["Green_Buttons"])
    QUIT_Button = constants.Button("QUIT",Right_offset,Height_Offset,offset/3,offset/3,constants.Colour_Palettes["Red_Buttons"])
    Home_Button = constants.Button("HOME",Mid_offset,Height_Offset,offset/3,offset/3,constants.Colour_Palettes["Orange_Buttons"])
    
    GameOver_Buttons =[ReTry_Button,QUIT_Button,Home_Button]

    Score_Output_Text = constants.Screen_Text((left_offset,screen.get_height()/6*1.75),32,Score_Text,constants.WHITE,False)
    Score_Output_Numbers = constants.Screen_Text((Right_offset,screen.get_height()/6*1.75),32,Score_Numbers,constants.WHITE,False)
    display_running = True
    while display_running:
        screen.blit(constants.GAMEOVER_IMAGE, (0,0))
                    
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
                            quit()
                        elif Home_Button.clicked:
                            main.main_menu()
                        elif ReTry_Button.clicked:
                            test.show_test() # type: ignore

                
    
        for button in GameOver_Buttons:
            button.draw()        # Render display content

        Score_Output_Text.draw()
        Score_Output_Numbers.draw()
        pygame.display.update()
