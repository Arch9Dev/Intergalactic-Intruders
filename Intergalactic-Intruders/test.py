import pygame
import math
import random

pygame.init()

# Screen stuff
Screen_Width = 800
Screen_Height = 1000
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))
background_image = pygame.image.load('Intergalactic-Intruders/images/gameback1.png')

# Barrier stuff 
barrier_image = pygame.image.load('Intergalactic-Intruders/images/barrier.png')
barrier_width = 175
barrier_height = 100
barrier_y = 650
barriers = [
    (68.75, barrier_y),
    (68.75 + barrier_width + 68.75, barrier_y),
    (68.75 + 2 * (barrier_width + 68.75), barrier_y)
]

# General backend
clock = pygame.time.Clock()
last_time_check = pygame.time.get_ticks()
Time_Difficulty = 1
Difficulty = 1
Frames = 180
Time_trial = 'false'
Max_Invaders_YN = 'false'
Current_Invaders = 0

# UI stuff
font = pygame.font.Font('freesansbold.ttf', 20)
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
Score_val = 0
Accuracy = 100
Hits_Landed = 1
Shots_Taken = 1

# Player Variables
PlayerImag = pygame.image.load('Intergalactic-Intruders/images/Player ship (1).gif')
player_hitbox = (PlayerImag.get_width(), PlayerImag.get_height())
Player_X = 370
Player_Y = 923
Player_Xchange = 0
Player_Ychange = 0
Player_Health = 3

# Player Bullet stuff
BulletImag = pygame.image.load('Intergalactic-Intruders/images/PlayerBullet.png')
Bullet_X = 0
Bullet_Y = 500
Bullet_Xchange = 0
Bullet_Ychange = 3
BulletStaet = "rest"
bullet_hitbox = (BulletImag.get_width(), BulletImag.get_height())

# Invader variables
InvaderImag1 = pygame.image.load('Intergalactic-Intruders/images/Alion one (1) 1.gif')
InvaderImag2 = pygame.image.load('Intergalactic-Intruders/images/Alion two (1) 1.gif')
InvaderImag3 = pygame.image.load('Intergalactic-Intruders/images/Alinon three  (1) 1.gif')
InvaderImag4 = pygame.image.load('Intergalactic-Intruders/images/Mother Ship 1.gif')
Invader_X = []
Invader_Y = []
Invader_Xchange = []
Invader_Ychange = 50
InvaderCount = 30
RowHeight = 50
Invader_Rangom = []
spawn_delay = 500
last_spawn_time = pygame.time.get_ticks()
invader_hitbox = (64, 64)

# Invader Bullet stuff
InvBulletImag = pygame.image.load('Intergalactic-Intruders/images/InvaderBullet.png')
InvBullet_Xchange = 0
InvBullet_Ychange = 1
Invader_Bullets = [[] for _ in range(InvaderCount)]
Bullet_Limit = 50
Fire_rate = 7500
last_shot_times = []

#Powerup stuff
"""
Powerups needed:
    Health back
    Bullet speed up
    Fire strength up
    Player move speed up
    Shield regen
"""



# Functions innit
def isCollision_PlayerBullet(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    return distance <= 33

def isCollision_InvBullet(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    return distance <= 33

def isCollision_Barrier(x1, y1, barrier_rect):
    return barrier_rect.collidepoint(x1, y1)

def Player(x, y):
    Screen.blit(PlayerImag, (x - 16, y + 10))

def Invader(x, y, rangom):
    if rangom == 1:
        Screen.blit(InvaderImag1, (x, y))
    elif rangom == 2:
        Screen.blit(InvaderImag2, (x, y))
    elif rangom == 3:
        Screen.blit(InvaderImag3, (x, y))
    elif rangom == 4:
        Screen.blit(InvaderImag4, (x, y))

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

def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    Screen.blit(game_over_text, (190, 250))

def player_hit():
    global Player_Health, Running
    Player_Health -= 1
    if Player_Health <= 0:
        game_over()
        Running = False

# Main game loop
Running = True
while Running:
    Screen.blit(background_image, (0, 0))
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - last_time_check

    if Time_trial == 'true':
        if elapsed_time >= 1000:
            if Frames < 300:
                Time_Difficulty *= 1.005
            else:
                Time_Difficulty *= 1.0025
            last_time_check = current_time

    Accuracy = round((Hits_Landed / Shots_Taken) * 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
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
                    Bullet_X = Player_X - 2.5
                    Bullet_Y = Player_Y
                    Bullet(Bullet_X, Bullet_Y)
                    Shots_Taken += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Player_Xchange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                Player_Ychange = 0

    Player_X += Player_Xchange
    Player_Y += Player_Ychange

    if Player_X <= 16:
        Player_X = 16
    elif Player_X >= 784:
        Player_X = 784

    if Player_Y <= 834:
        Player_Y = 834
    elif Player_Y >= 954:
        Player_Y = 954

    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > spawn_delay and len(Invader_X) < InvaderCount and Max_Invaders_YN == 'false':
        rangom = random.randint(1, 4)
        Invader_X.append(0)
        Invader_Y.append(30)
        Invader_Xchange.append(1.7)
        Invader_Rangom.append(rangom)
        last_shot_times.append(current_time)
        last_spawn_time = current_time
        Current_Invaders += 1
        if Current_Invaders >= InvaderCount and Time_trial == 'false':
            Max_Invaders_YN = 'true'

    for i in range(len(Invader_X)):
        Invader_X[i] += Invader_Xchange[i]
        if Invader_X[i] >= 768:
            Invader_X[i] = 768
            Invader_Y[i] += RowHeight
            Invader_Xchange[i] *= -1
        elif Invader_X[i] <= 0:
            Invader_X[i] = 0
            Invader_Y[i] += RowHeight
            Invader_Xchange[i] *= -1

    for i in range(len(Invader_X)):
        if len(Invader_Bullets[i]) < Bullet_Limit:
            if current_time - last_shot_times[i] >= Fire_rate + random.randint(-Fire_rate//2, Fire_rate):
                Invader_Bullets[i].append([Invader_X[i], Invader_Y[i]])
                last_shot_times[i] = current_time

    for i in range(len(Invader_X)):
        for bullet in Invader_Bullets[i]:
            InvaderBullet(bullet[0], bullet[1], i)
            bullet[1] += InvBullet_Ychange
            if bullet[1] >= 1000:
                Invader_Bullets[i].remove(bullet)
                print('bullet removed')

    if Bullet_Y <= 0:
        Bullet_Y = 1000
        BulletStaet = "rest"
    if BulletStaet == "fire":
        Bullet(Bullet_X, Bullet_Y)
        Bullet_Y -= Bullet_Ychange

    for i in range(len(Invader_X)):
        collision = isCollision_PlayerBullet(Bullet_X, Invader_X[i], Bullet_Y, Invader_Y[i])
        if collision:
            Hits_Landed += 1
            Score_val += 1
            Bullet_Y = 1000
            BulletStaet = "rest"
            Invader_X.pop(i)
            Invader_Y.pop(i)
            Invader_Xchange.pop(i)
            Invader_Rangom.pop(i)
            last_shot_times.pop(i)
            break

    for i in range(len(Invader_X)):
        for bullet in Invader_Bullets[i]:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], *bullet_hitbox)
            for barrier in barriers[:]:
                barrier_rect = pygame.Rect(barrier[0], barrier[1], barrier_width, barrier_height)
                if isCollision_Barrier(bullet[0], bullet[1], barrier_rect):
                    Invader_Bullets[i].remove(bullet)
                    break

    for i in range(len(Invader_X)):
        invader_rect = pygame.Rect(Invader_X[i], Invader_Y[i], *invader_hitbox)
        for barrier in barriers[:]:
            barrier_rect = pygame.Rect(barrier[0], barrier[1], barrier_width, barrier_height)
            if invader_rect.colliderect(barrier_rect):
                barriers.remove(barrier)
                break

    player_rect = pygame.Rect(Player_X, Player_Y, *player_hitbox)
    for i in range(len(Invader_X)):
        for bullet in Invader_Bullets[i][:]:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], *bullet_hitbox)
            if bullet_rect.colliderect(player_rect):
                Invader_Bullets[i].remove(bullet)
                player_hit()
                break

    Player(Player_X, Player_Y)
    for i in range(len(Invader_X)):
        Invader(Invader_X[i], Invader_Y[i], Invader_Rangom[i])
    for barrier in barriers:
        Screen.blit(barrier_image, barrier)
    show_Score(5, 5)
    show_Difficulty(130, 5, Frames)
    show_Acc(300, 5)
    show_Health(420, 5)

    Frames = 180 * Difficulty * Time_Difficulty
    pygame.display.update()
    clock.tick(Frames)
pygame.quit()