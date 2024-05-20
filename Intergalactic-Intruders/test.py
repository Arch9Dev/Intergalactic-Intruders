import pygame
import math
import random

pygame.init()

# Set up the screen
Screen_Width = 800
Screen_Height = 600
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))

# Set up the clock
clock = pygame.time.Clock()
last_time_check = pygame.time.get_ticks()
Time_Difficulty = 1
Difficulty = 1  # Adjust this value to change the game speed (1 for normal, >1 for faster, <1 for slower)

# Set up the fonts
font = pygame.font.Font('freesansbold.ttf', 20)
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

# Initialize game variables
Score_val = 0
PlayerImag = pygame.image.load('Intergalactic-Intruders/images/Player ship (1).gif')
Player_X = 370
Player_Y = 523
Player_Xchange = 0
Player_Ychange = 0
Accuracy = 100
Hits_Landed = 1
Shots_Taken = 1
Frames = 180

InvaderImag1 = pygame.image.load('Intergalactic-Intruders/images/Alion one (1) 1.gif')
InvaderImag2 = pygame.image.load('Intergalactic-Intruders/images/Alion two (1) 1.gif')
InvaderImag3 = pygame.image.load('Intergalactic-Intruders/images/Alinon three  (1) 1.gif')
InvaderImag4 = pygame.image.load('Intergalactic-Intruders/images/Mother Ship 1.gif')

Invader_X = []
Invader_Y = []
Invader_Xchange = []
Invader_Ychange = 50
InvaderCount = 20
RowHeight = 50  # Define a fixed row height

Invader_Rangom = []  # Store the rangom values for each invader

spawn_delay = 500  # Delay in milliseconds between invader spawns
last_spawn_time = pygame.time.get_ticks()

BulletImag = pygame.image.load('Intergalactic-Intruders/images/PlayerBullet.png')
Bullet_X = 0
Bullet_Y = 500
Bullet_Xchange = 0
Bullet_Ychange = 3
BulletStaet = "rest"

InvBulletImag = pygame.image.load('Intergalactic-Intruders/images/InvaderBullet.png')
InvBullet_X = []
InvBullet_Y = []
InvBullet_Xchange = 0
InvBullet_Ychange = 1
InvBulletStaet = []

def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    return distance <= 35

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
    global InvBulletStaet
    Screen.blit(InvBulletImag, (x, y))
    InvBulletStaet[i] = "fire"

def show_Score(x, y):
    Score = font.render("Points: " + str(Score_val), True, (255, 255, 255))
    Screen.blit(Score, (x, y))

def show_Difficulty(x, y, Frames):
    Score = font.render("Difficulty: " + str(round(Frames)), True, (255, 255, 255))
    Screen.blit(Score, (x, y))

def show_Acc(x, y):
    Score = font.render("Acc: " + str(Accuracy), True, (255, 255, 255))
    Screen.blit(Score, (x, y))

def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    Screen.blit(game_over_text, (190, 250))

# Main game loop
Running = True
while Running:
    Screen.fill((0, 0, 0))

    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - last_time_check

    if (elapsed_time >= 1000):
        # Increase Time_Difficulty by whatever every second
        if Frames < 300:
            Time_Difficulty *= 1.005
        else:
            Time_Difficulty *= 1.0025
        last_time_check = current_time  # Update the last time checked

    # accuracy stuff
    Accuracy = round((Hits_Landed / Shots_Taken) * 100)

    # Event handling
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
                    Bullet_X = Player_X - 2.5  # Adjust bullet's X-coordinate to the center of the player
                    Bullet_Y = Player_Y  # Set bullet's Y-coordinate to player's Y-coordinate
                    Bullet(Bullet_X, Bullet_Y)
                    Shots_Taken += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Player_Xchange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                Player_Ychange = 0

    # Update player position
    Player_X += Player_Xchange
    Player_Y += Player_Ychange

    # Boundary checking for player
    if Player_X <= 16:
        Player_X = 16
    elif Player_X >= 784:
        Player_X = 784

    if Player_Y <= 434:
        Player_Y = 434
    elif Player_Y >= 554:
        Player_Y = 554

    # Spawn invaders with a delay
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > spawn_delay and len(Invader_X) < InvaderCount:
        rangom = random.randint(1, 4)  # Choose a random image for this invader
        Invader_X.append(0)
        Invader_Y.append(30)
        Invader_Xchange.append(1.2)
        Invader_Rangom.append(rangom)  # Store the rangom value for this invader
        InvBullet_X.append(0)  # Initialize bullet X for this invader
        InvBullet_Y.append(0)  # Initialize bullet Y for this invader
        InvBulletStaet.append("rest")  # Initialize bullet state for this invader
        last_spawn_time = current_time

    # Update invader positions
    for i in range(len(Invader_X)):
        Invader_X[i] += Invader_Xchange[i]
        # Check for boundary collisions for individual invaders
        if Invader_X[i] >= 768:
            Invader_X[i] = 768
            Invader_Y[i] += RowHeight
            Invader_Xchange[i] *= -1
        elif Invader_X[i] <= 0:
            Invader_X[i] = 0
            Invader_Y[i] += RowHeight
            Invader_Xchange[i] *= -1

        # Shooting stuff goes here
        if pygame.key.get_pressed()[pygame.K_g]:
            InvBullet_X[i] = Invader_X[i]
            InvBullet_Y[i] = Invader_Y[i]
            InvaderBullet(InvBullet_X[i], InvBullet_Y[i], i)
            # Update bullet position
        if InvBullet_Y[i] <= 0:
            InvBullet_Y[i] = 600
            InvBulletStaet[i] = "rest"
        if InvBulletStaet[i] == "fire":
            InvaderBullet(InvBullet_X[i], InvBullet_Y[i], i)
            InvBullet_Y[i] += InvBullet_Ychange

    # Update bullet position
    if Bullet_Y <= 0:
        Bullet_Y = 600
        BulletStaet = "rest"
    if BulletStaet == "fire":
        Bullet(Bullet_X, Bullet_Y)
        Bullet_Y -= Bullet_Ychange

    # Check for collisions
    for i in range(len(Invader_X)):
        if abs(Player_Y - Invader_Y[i]) <= 35 and abs(Player_X - Invader_X[i]) <= 35:
            game_over()
            Running = False
            break

        if Invader_Y[i] >= 554:
            game_over()
            Running = False
            break

        collision = isCollision(Bullet_X, Invader_X[i], Bullet_Y, Invader_Y[i])
        if collision:
            Hits_Landed += 1
            Score_val += 1
            Bullet_Y = 600
            BulletStaet = "rest"
            Invader_X.pop(i)
            Invader_Y.pop(i)
            Invader_Xchange.pop(i)
            Invader_Rangom.pop(i)
            InvBullet_X.pop(i)
            InvBullet_Y.pop(i)
            InvBulletStaet.pop(i)
            break

    # Render player, invaders, and score
    Player(Player_X, Player_Y)
    for i in range(len(Invader_X)):
        Invader(Invader_X[i], Invader_Y[i], Invader_Rangom[i])  # Pass the assigned rangom value
    show_Score(5, 5)
    show_Difficulty(130, 5, Frames)
    show_Acc(300, 5)

    Frames = 180 * Difficulty * Time_Difficulty
    pygame.display.update()
    clock.tick(Frames)  # Limit frame rate based on difficulty

pygame.quit()
