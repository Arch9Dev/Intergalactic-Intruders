import pygame
import math
import random
import sounds
import os
import constants
import GameOver
import main
import settings
from PIL import Image, ImageSequence

def show_test():
    pygame.init()
    Screen_Width = 800
    Screen_Height = 1000
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    Screen = pygame.display.set_mode((Screen_Width, Screen_Height))
    
    background_image = pygame.image.load('Intergalactic-Intruders/images/gameback1.png')
    Pause_X = Screen_Width / 2 - 110
    Pause_Y = Screen_Height / 3 

    resume_button = constants.Button("Resume",Pause_X, Pause_Y-100,20,0,constants.Colour_Palettes["Red_Buttons"])
    settings_button = constants.Button("Settings",Pause_X, Pause_Y,20,0,constants.Colour_Palettes["Red_Buttons"])
    main_menu_button = constants.Button("Main Menu",Pause_X, Pause_Y+100,20,0,constants.Colour_Palettes["Red_Buttons"])
    PauseButtons =[resume_button,settings_button,main_menu_button]

    level = 1
    clock = pygame.time.Clock()
    last_time_check = pygame.time.get_ticks()
    Time_Difficulty = 1
    Difficulty = 0.75 # 1 default, +/-0.5 for easy/hard respectively
    Frames = 180
    Time_trial = 'false' # true or false for time trial
    InvaderCount = 10 * level # max invaders that can spawn, max on screen for time trial
    Max_Invaders_YN = 'false'
    Current_Invaders = 0
    
    
    
    # Animation stuff
    Sprite_GIF_Path = {
        "Player_Ship" : r"Intergalactic-Intruders/images/Player.gif",
        "Alien1": r"Intergalactic-Intruders/images/Alien1.gif",
        "Alien2": r"Intergalactic-Intruders/images/Alien2.gif",
        "Alien3": r"Intergalactic-Intruders/images/Alien3.gif",
        "Alien4": r"Intergalactic-Intruders/images/Alien4.gif"
    }
    

    class AnimatedSpriteObject(pygame.sprite.Sprite):
        def __init__(self, X, Y, images):
            pygame.sprite.Sprite.__init__(self)
            self.images = images
            self.image = self.images[0]
            self.rect = self.image.get_rect(midbottom = (X, -Y))
            self.image_index = 0
        def update(self, PosX, PosY):
            self.rect.x = PosX
            self.rect.y = PosY
            self.image_index += 1
            self.image = self.images[self.image_index % len(self.images)]

    def loadGIF(filename):
        pilImage = Image.open(filename)
        AnimationFrames = []
        for Frames in ImageSequence.Iterator(pilImage):
            Frames = Frames.convert('RGBA')
            pygameImage = pygame.image.fromstring(
                Frames.tobytes(), Frames.size, 'RGBA').convert_alpha()
            AnimationFrames.append(pygameImage)
        return AnimationFrames

    def AnimatedSpriteGroup(SpriteFileName,PosX,PosY):
        SpriteGIFFrameList = loadGIF(SpriteFileName)
        animated_sprite = AnimatedSpriteObject(PosX,PosY,SpriteGIFFrameList)
        return (pygame.sprite.Group(animated_sprite)) # type: ignore

    # Barrier stuff
    barrier_image = { # one for each health point
            8: pygame.image.load('Intergalactic-Intruders/images/Bunker/sprite_Bunker00.png'),
            7: pygame.image.load('Intergalactic-Intruders/images/Bunker/sprite_Bunker01.png'),
            6: pygame.image.load('Intergalactic-Intruders/images/Bunker/sprite_Bunker02.png'),
            5: pygame.image.load('Intergalactic-Intruders/images/Bunker/sprite_Bunker03.png'),
            4: pygame.image.load('Intergalactic-Intruders/images/Bunker/sprite_Bunker04.png'),
            3: pygame.image.load('Intergalactic-Intruders/images/Bunker/sprite_Bunker05.png'),
            2: pygame.image.load('Intergalactic-Intruders/images/Bunker/sprite_Bunker06.png'),
            1: pygame.image.load('Intergalactic-Intruders/images/Bunker/sprite_Bunker07.png')
    }
    
    BarrierSize = (Screen_Width * 0.21875, Screen_Height * 0.075)
    barrier_image = {health: pygame.transform.scale(img, BarrierSize) for health, img in barrier_image.items()}
    barrier_health = 8
    barrier_width = Screen_Width * 0.21875
    barrier_height = Screen_Height * 0.075
    barrier_y = Screen_Height * 0.65
    barriers = [
        [(Screen_Width - (barrier_width * 3))/4, barrier_y, barrier_health],
        [(Screen_Width - (barrier_width * 3))/4 + barrier_width + (Screen_Width - (barrier_width * 3))/4, barrier_y, barrier_health],
        [(Screen_Width - (barrier_width * 3))/4 + 2 * (barrier_width + (Screen_Width - (barrier_width * 3))/4), barrier_y, barrier_health]
    ]


    # UI stuff
    font = pygame.font.Font('freesansbold.ttf', 20)
    game_over_font = pygame.font.Font('freesansbold.ttf', 64)
    Score_val = 0
    Accuracy = 100
    Hits_Landed = 1
    Shots_Taken = 1
    countdown_font = pygame.font.Font('freesansbold.ttf', 64)
    countdown_active = True
    countdown_start_time = pygame.time.get_ticks()
    countdown_duration = 3000  # 3 seconds
    paused = False
    DifEasy = pygame.image.load('Intergalactic-Intruders/images/DifEasy.png')
    DifNormal = pygame.image.load('Intergalactic-Intruders/images/DifNormal.png')
    DifHard = pygame.image.load('Intergalactic-Intruders/images/DifHard.png') # type: ignore

    # Player Variables
    PlayerImag = AnimatedSpriteGroup(Sprite_GIF_Path["Player_Ship"],Screen_Width//2,Screen_Height//2)
    hitbox_Image = pygame.image.load('Intergalactic-Intruders/images/Player.gif')
    PlayerSize = (Screen_Width * 0.04, Screen_Height * 0.032)
    player_hitbox = (hitbox_Image.get_width(), hitbox_Image.get_height())
    Player_X = (Screen_Width / 2)
    Player_Y = Screen_Height * 0.9
    global Player_Health
    Player_Health = 3
    Player_Xchange = 0
    Player_Ychange = 0
    Original_Player_Xchange = Screen_Width * 0.002125
    Original_Player_Ychange = Screen_Height * 0.0017

    # Player Bullet stuff
    BulletImag = pygame.image.load('Intergalactic-Intruders/images/PlayerBullet.png')
    BulletSize = (Screen_Width * 0.0125, Screen_Height * 0.02)
    BulletImag = pygame.transform.scale(BulletImag, BulletSize) 
    Bullet_X = 0
    Bullet_Y = Screen_Height
    Bullet_Xchange = 0
    global Original_Bullet_Ychange
    Original_Bullet_Ychange = Screen_Height * 0.003
    Bullet_Ychange = Screen_Height * 0.003
    BulletStaet = "rest"
    bullet_hitbox = (BulletImag.get_width(), BulletImag.get_height())
    bullet_damage = 1
    Original_Bullet_damage = 1

    # Invader variables
    inv_hitbox_image = pygame.image.load('Intergalactic-Intruders/images/Alien4.gif')
    InvaderImag1 = AnimatedSpriteGroup(Sprite_GIF_Path["Alien1"],Screen_Width//2,Screen_Height//2)
    InvaderImag2 = AnimatedSpriteGroup(Sprite_GIF_Path["Alien2"],Screen_Width//2,Screen_Height//2)
    InvaderImag3 = AnimatedSpriteGroup(Sprite_GIF_Path["Alien3"],Screen_Width//2,Screen_Height//2)
    InvaderImag4 = AnimatedSpriteGroup(Sprite_GIF_Path["Alien4"],Screen_Width//2,Screen_Height//2)
    Invader_X = []
    Invader_Y = []
    Invader_Xchange = []
    Invader_Ychange = Screen_Height * 0.05
    RowHeight = Screen_Height * 0.05
    Invader_Rangom = []
    Invader_Health = []
    spawn_delay = 500 # delay between invader spawns
    last_spawn_time = pygame.time.get_ticks()
    invader_hitbox = (inv_hitbox_image.get_height(), inv_hitbox_image.get_width())

    # Invader Bullet stuff
    InvBulletImag = pygame.image.load('Intergalactic-Intruders/images/InvaderBullet.png')
    InvBulletSize = (Screen_Width * 0.0125, Screen_Height * 0.02)
    InvBulletImag = pygame.transform.scale(InvBulletImag, BulletSize) 
    Inv_Bullet_Hitbox = (InvBulletImag.get_width(), InvBulletImag.get_height())
    InvBullet_Xchange = 0
    InvBullet_Ychange = Screen_Height * 0.001
    Invader_Bullets = [[] for _ in range(InvaderCount)]
    Bullet_Limit = InvaderCount * 5
    Fire_rate = 10000 # invader firerate in 1/1000s sec
    last_shot_times = []

    # Powerup Stuff
    powerup_speed = Screen_Height * 0.001
    powerup_images = {
        "ShotPower": pygame.image.load('Intergalactic-Intruders/images/ShotPower.png'),
        "ShieldRegen": pygame.image.load('Intergalactic-Intruders/images/ShieldRegen.png'),
        "MoveSpeed": pygame.image.load('Intergalactic-Intruders/images/MoveSpeed.png'),
        "HealthUp": pygame.image.load('Intergalactic-Intruders/images/HealthUp.png'),
        "BulletSpeed": pygame.image.load('Intergalactic-Intruders/images/BulletSpeed.png')
    }
    active_powerups = []
    Timer_ShotPower = 0
    Timer_MoveSpeed = 0
    Timer_BulletSpeed = 0


    # ---------------------------------
    #            FUNCTIONS
    # ---------------------------------
    def isCollision_PlayerBullet(x1, x2, y1, y2):
        distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
        return distance <= 33

    def isCollision_InvBullet(x1, x2, y1, y2):
        distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
        return distance <= 33

    def isCollision_Barrier(x1, y1, barrier_rect):
        return barrier_rect.collidepoint(x1, y1)

    def Player(x, y):
        PlayerImag.update(x - 16, y + 10)

    def Invader(x, y, rangom):
        if rangom == 1:
            InvaderImag1.update(x, y)
        elif rangom == 2:
            InvaderImag2.update(x, y)
        elif rangom == 3:
            InvaderImag3.update(x, y)
        elif rangom == 4:
            InvaderImag4.update(x, y)

    def Bullet(x, y):
        global BulletStaet
        Screen.blit(BulletImag, (x, y))
        BulletStaet = "fire"

    def InvaderBullet(x, y, i):
        Screen.blit(InvBulletImag, (x, y))

    def show_Score(x, y):
        Score = font.render("Points: " + str(Score_val), True, (255, 255, 255))
        Screen.blit(Score, (x, y))

    def show_Difficulty(x, y, Frames):
        Score = font.render("Difficulty: " + str(round(Frames)), True, (255, 255, 255))
        Screen.blit(Score, (x, y))

    def show_Acc(x, y):
        Score = font.render("Acc: " + str(Accuracy) + '%', True, (255, 255, 255))
        Screen.blit(Score, (x, y))

    def show_Health(x, y):
        health_text = font.render("Health: " + str(Player_Health), True, (255, 255, 255))
        Screen.blit(health_text, (x, y))

    def game_over_menu():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
            Intruders_killed = InvaderCount-len(Invader_X)
            GameOver.show_GameOver(Accuracy,Difficulty,current_time,Intruders_killed)


    def player_hit():
        global Player_Health, Running
        Player_Health -= 1
        sounds.play_playerhit()
        if Player_Health <= 0:
            action = game_over_menu()
            if action == "retry":
                pass
            elif action == "main_menu":
                print('menu')
            elif action == "exit":
                pygame.quit()
                quit()
                
    def spawn_powerup(x, y):
        powerup_type = random.choice(list(powerup_images.keys()))
        powerup_image = powerup_images[powerup_type]
        active_powerups.append((powerup_image, x, y, powerup_type))

    def isCollision_PlayerPowerup(player_rect, powerup_rect):
        return player_rect.colliderect(powerup_rect)

    def apply_powerup(powerup_type):
        global Player_Health, Bullet_Ychange, Player_Xchange, Player_Ychange, Original_Player_Xchange, Original_Player_Ychange, bullet_damage, barriers, Timer_ShotPower, Timer_BulletSpeed, Timer_MoveSpeed
        sounds.play_powerup
        if powerup_type == "ShotPower":
            bullet_damage = Original_Bullet_damage
            bullet_damage *= 2
            Timer_ShotPower = pygame.time.get_ticks() + 10000
        elif powerup_type == "ShieldRegen":
            barriers = [
                [(Screen_Width - (barrier_width * 3))/4, barrier_y, barrier_health],
                [(Screen_Width - (barrier_width * 3))/4 + barrier_width + (Screen_Width - (barrier_width * 3))/4, barrier_y, barrier_health],
                [(Screen_Width - (barrier_width * 3))/4 + 2 * (barrier_width + (Screen_Width - (barrier_width * 3))/4), barrier_y, barrier_health]
            ]
        elif powerup_type == "MoveSpeed":
            Original_Player_Xchange = Player_Xchange
            Original_Player_Ychange = Player_Ychange
            Player_Xchange *= 2
            Player_Ychange *= 2
            Timer_MoveSpeed = pygame.time.get_ticks() + 10000
        elif powerup_type == "HealthUp":
            Player_Health += 3 - Player_Health
        elif powerup_type == "BulletSpeed":
            Bullet_Ychange = Original_Bullet_Ychange
            Bullet_Ychange *= 2
            Timer_BulletSpeed = pygame.time.get_ticks() + 10000

    def draw_powerups():
        for powerup in active_powerups:
            Screen.blit(powerup[0], (powerup[1], powerup[2]))

    def remove_powerup(powerup_type):
        global Player_Xchange, Player_Ychange, Original_Player_Xchange, Original_Player_Ychange, Bullet_Ychange, Original_Bullet_Ychange, bullet_damage
        if powerup_type == "MoveSpeed":
            Player_Xchange = Original_Player_Xchange
            Player_Ychange = Original_Player_Ychange
        if powerup_type == "BulletSpeed":
            Bullet_Ychange = Original_Bullet_Ychange
        if powerup_type == "ShotPower":
            bullet_damage = Original_Bullet_damage

    def powerup_expired(hi):
        if (hi == 'MoveSpeed'):
            if Timer_MoveSpeed <= pygame.time.get_ticks():
                return True
        if (hi == 'BulletSpeed'):
            if Timer_BulletSpeed <= pygame.time.get_ticks():
                return True
        if (hi == 'ShotPower'):
            if Timer_ShotPower <= pygame.time.get_ticks():
                return True

    def display_powerup_icons():
        if Timer_BulletSpeed >= pygame.time.get_ticks():
            Screen.blit(pygame.image.load('Intergalactic-Intruders/images/BulletSpeed.png'), (Screen_Width * 0.95, Screen_Height * 0.005))
        if Timer_MoveSpeed >= pygame.time.get_ticks():
            Screen.blit(pygame.image.load('Intergalactic-Intruders/images/MoveSpeed.png'), (Screen_Width * 0.9, Screen_Height * 0.005))
        if Timer_ShotPower >= pygame.time.get_ticks():
            Screen.blit(pygame.image.load('Intergalactic-Intruders/images/ShotPower.png'), (Screen_Width * 0.85, 5))


    def show_pause_menu():
        Pasue_BOX_Width = PauseButtons[0].width +40
        Pasue_BOX_Height = PauseButtons[0].height*6
        pygame.draw.rect(Screen,constants.WHITE,(Pause_X-20,Pause_Y-50,Pasue_BOX_Width,Pasue_BOX_Height) ,border_radius = 15 )
        for buttons in PauseButtons:
            buttons.draw()

        

        

    # ---------------------------------
    #            MAIN LOOP
    # ---------------------------------
    Running = True
    while Running:
        # Screen init stuff
        Screen.blit(background_image, (0, 0))
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - last_time_check
        Accuracy = round((Hits_Landed / Shots_Taken) * 100)
        if (Difficulty <= 1):
            Screen.blit(DifEasy, (5, 25))
        elif (Difficulty >= 1):
            Screen.blit(DifNormal, (5, 25))
        elif (Difficulty >= 2):
            Screen.blit(DifHard, (5, 25))
         
        # Countdown before game start
        if countdown_active:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Running = False
            current_time = pygame.time.get_ticks()
            time_elapsed = current_time - countdown_start_time
            if time_elapsed >= countdown_duration + 1000:
                countdown_active = False
            else:
                countdown_text = ""
                if time_elapsed >= countdown_duration:
                    countdown_text = countdown_font.render("GO!", True, (255, 255, 255))
                else:
                    countdown_number = 3 - time_elapsed // 1000

                    countdown_text = countdown_font.render(str(countdown_number), True, (255, 255, 255))
                    
                Textwidth = countdown_text.get_width()/2
                Textheight = countdown_text.get_height()
                countdownrect = pygame.rect.Rect(Screen_Width // 2 -(Textwidth/2 +20) ,Screen_Height // 2 ,Textwidth*2,Textheight)
                pygame.draw.rect(Screen,constants.BLACK,countdownrect.inflate(40,40),border_radius=15)
                pygame.draw.rect(Screen,constants.WHITE,countdownrect.inflate(40,40),5,border_radius=15)
                Screen.blit(countdown_text, countdownrect)
        # Game Start
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False if paused else True
                    if paused == False:
                        if event.key == pygame.K_LEFT:
                            Player_Xchange = -1.7
                        if event.key == pygame.K_RIGHT:
                            Player_Xchange = 1.7
                        if event.key == pygame.K_UP:
                            Player_Ychange = -1.7
                        if event.key == pygame.K_DOWN:
                            Player_Ychange = 1.7
                        if event.key == pygame.K_SPACE:
                            if BulletStaet == "rest":
                                BulletStaet = "fire"
                                Bullet_X = Player_X - (BulletImag.get_width() / 2)
                                Bullet_Y = Player_Y
                                Bullet(Bullet_X, Bullet_Y)
                                Shots_Taken += 1
                                sounds.play_gunshot()
                for button in PauseButtons:
                    button.handle_event(event)        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        Player_Xchange = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        Player_Ychange = 0
            # Pause menu stuff
            if paused:
                show_pause_menu()
                for button in PauseButtons:
                    if button.clicked:
                        if button.text == "Resume":
                            paused = False
                        elif button.text == "Settings":
                            constants.ResetScreen()
                            settings.show_settings()
                        elif button.text == "Main Menu":
                            constants.ResetScreen()
                            main.main_menu()

            # Game logic and update stuff
            else:
                menu = False
                # Time trial difficulty thing
                if Time_trial == 'true':
                    if elapsed_time >= 1000:
                        if Frames < 300:
                            Time_Difficulty *= 1.005
                        else:
                            Time_Difficulty *= 1.0025
                        last_time_check = current_time

                Player_X += Player_Xchange
                Player_Y += Player_Ychange

                # Player boundary yeah
                if Player_X <= Screen_Width * 0.02:
                    Player_X = Screen_Width * 0.02
                elif Player_X >= Screen_Width * 0.98:
                    Player_X = Screen_Width * 0.98

                if Player_Y <= Screen_Height * 0.750:
                    Player_Y = Screen_Height * 0.750
                elif Player_Y >= Screen_Height * 0.954:
                    Player_Y = Screen_Height * 0.954

                # Invader spawning \o/
                current_time = pygame.time.get_ticks()
                if current_time - last_spawn_time > spawn_delay and len(Invader_X) < InvaderCount and Max_Invaders_YN == 'false':
                    rangom = random.randint(1, 4)
                    Invader_X.append(0)
                    Invader_Y.append(Screen_Height * 0.03)
                    Invader_Xchange.append(Screen_Width * 0.001625)
                    Invader_Rangom.append(rangom)
                    Invader_Health.append(random.randint(1,3))
                    last_shot_times.append(current_time + random.randint(-5000, 5000))
                    last_spawn_time = current_time
                    Current_Invaders += 1
                    if Current_Invaders >= InvaderCount and Time_trial == 'false':
                        Max_Invaders_YN = 'true'

                # Invader movement
                for i in range(len(Invader_X)):
                    Invader_X[i] += Invader_Xchange[i]
                    if Invader_X[i] >= Screen_Width * 0.96:
                        Invader_X[i] = Screen_Width * 0.96
                        Invader_Y[i] += RowHeight
                        Invader_Xchange[i] *= -1
                    elif Invader_X[i] <= 0:
                        Invader_X[i] = 0
                        Invader_Y[i] += RowHeight
                        Invader_Xchange[i] *= -1

                # Invader shooting
                for i in range(len(Invader_X)):
                    if len(Invader_Bullets[i]) < Bullet_Limit:
                        if current_time - last_shot_times[i] >= Fire_rate + random.randint(-Fire_rate//2, Fire_rate):
                            Invader_Bullets[i].append([Invader_X[i], Invader_Y[i]])
                            last_shot_times[i] = current_time

                # Invader bullet mooovinnng
                for i in range(len(Invader_X)):
                    for bullet in Invader_Bullets[i]:
                        InvaderBullet(bullet[0], bullet[1], i)
                        bullet[1] += InvBullet_Ychange
                        if bullet[1] >= Screen_Height:
                            Invader_Bullets[i].remove(bullet)
                            print('bullet removed ', i)

                # Plyer bullet boundry
                if Bullet_Y <= 0:
                    Bullet_Y = Screen_Height
                    BulletStaet = "rest"
                if BulletStaet == "fire":
                    Bullet(Bullet_X, Bullet_Y)
                    Bullet_Y -= Bullet_Ychange

                # Powerups spawning stuff
                for powerup in active_powerups[:]:
                    powerup_image, x, y, powerup_type = powerup
                    y += powerup_speed
                    if y > Screen_Height:
                        active_powerups.remove(powerup)
                    else:
                        powerup_rect = pygame.Rect(x, y, powerup_image.get_width(), powerup_image.get_height())
                        if isCollision_PlayerPowerup(player_rect, powerup_rect):
                            apply_powerup(powerup_type)
                            active_powerups.remove(powerup)
                        else:
                            active_powerups[active_powerups.index(powerup)] = (powerup_image, x, y, powerup_type)

                for powerup in active_powerups[:]:
                    if powerup_expired(powerup):
                        remove_powerup(powerup[3])
                        active_powerups.remove(powerup)

                # Collision stuff for a while
                for i in range(len(Invader_X)):
                    collision = isCollision_PlayerBullet(Bullet_X, Invader_X[i], Bullet_Y, Invader_Y[i])
            
                    if collision:
                        Hits_Landed += 1
                        Score_val += 1
                        Bullet_Y = Screen_Height
                        BulletStaet = "rest"
                        Invader_Health[i] -= bullet_damage
                        if Invader_Health[i] <= 0:
                            if random.randint(1, 5) == 1:
                                spawn_powerup(Invader_X[i], Invader_Y[i])
                            Invader_X.pop(i)
                            Invader_Y.pop(i)
                            Invader_Xchange.pop(i)
                            Invader_Rangom.pop(i)
                            last_shot_times.pop(i)
                            if not countdown_active:
                                sounds.play_aliendeath()
                            break

                for i in range(len(Invader_X) - 1, -1, -1):
                    invader_rect = pygame.Rect(Invader_X[i], Invader_Y[i], *invader_hitbox)
                    for barrier in barriers[:]:
                        barrier_rect = pygame.Rect(barrier[0], barrier[1], barrier_width, barrier_height)
                        if invader_rect.colliderect(barrier_rect):
                            barriers.remove(barrier)
                            sounds.play_barrierdestroyed
                            Invader_Health[i] = 0
                            if Invader_Health[i] <= 0:
                                Invader_X.pop(i)
                                Invader_Y.pop(i)
                                Invader_Xchange.pop(i)
                                Invader_Rangom.pop(i)
                                last_shot_times.pop(i)
                                sounds.play_aliendeath()
                            break

                player_rect = pygame.Rect(Player_X, Player_Y, *player_hitbox)
                for i in range(len(Invader_X)):
                    for bullet in Invader_Bullets[i][:]:
                        bullet_rect = pygame.Rect(bullet[0], bullet[1], *Inv_Bullet_Hitbox)
                        if bullet_rect.colliderect(player_rect):
                            Invader_Bullets[i].remove(bullet)
                            player_hit()
                            break

                for i in range(len(Invader_X)):
                    for bullet in Invader_Bullets[i]:
                        bullet_rect = pygame.Rect(bullet[0], bullet[1], *Inv_Bullet_Hitbox)
                        for barrier in barriers[:]:
                            barrier_rect = pygame.Rect(barrier[0], barrier[1], barrier_width, barrier_height)
                            if isCollision_Barrier(bullet[0], bullet[1], barrier_rect):
                                Invader_Bullets[i].remove(bullet)
                                barrier[2] -= 1
                                print(barrier[2])
                                if barrier[2] <= 0:
                                    barriers.remove(barrier)
                                    sounds.play_barrierdestroyed()
                                break

                for barrier in barriers:
                    health = barrier[2]
                    if health > 0:
                        Screen.blit(barrier_image[health], (barrier[0], barrier[1]))
                # All done with collisino 

        # now just rendering stuff every frame
        
        Player(Player_X, Player_Y)
        PlayerImag.draw(Screen)
        for i in range(len(Invader_X)):
            Invader(Invader_X[i], Invader_Y[i], Invader_Rangom[i])
            if (Invader_Rangom[i] == 1):
                InvaderImag1.draw(Screen)
            if (Invader_Rangom[i] == 2):
                InvaderImag2.draw(Screen)
            if (Invader_Rangom[i] == 3):
                InvaderImag3.draw(Screen)
            if (Invader_Rangom[i] == 4):
                InvaderImag4.draw(Screen)
        
        for barrier in barriers:
            Screen.blit(barrier_image[barrier[2]], (barrier[0], barrier[1]))
        # UI Activities
        draw_powerups()
        show_Score(Screen_Width * 0.00625, Screen_Height * 0.005)
        show_Difficulty(Screen_Width * 0.1625, Screen_Height * 0.005, Frames)
        show_Acc(Screen_Width * 0.375, Screen_Height * 0.005)
        show_Health(Screen_Width * 0.525, Screen_Height * 0.005)
        display_powerup_icons()

        Frames = 180 * Difficulty * Time_Difficulty
        pygame.display.update()
        clock.tick(Frames)
        
    pygame.quit()