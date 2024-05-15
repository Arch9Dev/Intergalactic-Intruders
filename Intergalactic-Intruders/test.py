import pygame
import random
import math
from pygame import mixer

pygame.init()

# Set up the screen
Screen_Width = 800
Screen_Height = 600
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))

# Set up the clock
clock = pygame.time.Clock()
FPS = 90  # Adjust this value as needed

# Set up the fonts
font = pygame.font.Font('freesansbold.ttf', 20)
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

# Initialize game variables
Score_val = 0
PlayerImag = pygame.image.load('Intergalactic-Intruders\images\Player ship (1).gif')
Player_X = 370
Player_Y = 523
Player_Xchange = 0

InvaderImag = []
Invader_X = []
Invader_Y = []
Invader_Xchange = []
Invader_Ychange = []
InvaderCount = 8

for num in range(InvaderCount):
    InvaderImag.append(pygame.image.load('Intergalactic-Intruders\images\Player ship (1).gif'))
    Invader_X.append(random.randint(64, 737))
    Invader_Y.append(random.randint(30, 180))
    Invader_Xchange.append(1.2)
    Invader_Ychange.append(50)

BulletImag = pygame.image.load('Intergalactic-Intruders\images\Player ship (1).gif')
Bullet_X = 0
Bullet_Y = 500
Bullet_Xchange = 0
Bullet_Ychange = 3
BulletStaet = "rest"


def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    if distance <= 50:
        return True
    else:
        return False


def Player(x, y):
    Screen.blit(PlayerImag, (x - 16, y + 10))


def Invader(x, y, i):
    Screen.blit(InvaderImag[i], (x, y))


def Bullet(x, y):
    global BulletStaet
    Screen.blit(BulletImag, (x, y))
    BulletStaet = "fire"


def show_Score(x, y):
    Score = font.render("Points: " + str(Score_val), True, (255, 255, 255))
    Screen.blit(Score, (x, y))


def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    Screen.blit(game_over_text, (190, 250))


# Main game loop
Running = True
while Running:
    Screen.fill((0, 0, 0))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player_Xchange = -1.7
            if event.key == pygame.K_RIGHT:
                Player_Xchange = 1.7
            if event.key == pygame.K_SPACE:
                if BulletStaet is "rest":
                    Bullet_X = Player_X
                    Bullet(Bullet_X, Bullet_Y)
        if event.type == pygame.KEYUP:
            Player_Xchange = 0

    # Update player position
    Player_X += Player_Xchange
    
    # Update invader positions
    for i in range(InvaderCount):
        Invader_X[i] += Invader_Xchange[i]

    # Update bullet position
    if Bullet_Y <= 0:
        Bullet_Y = 600
        BulletStaet = "rest"
    if BulletStaet is "fire":
        Bullet(Bullet_X, Bullet_Y)
        Bullet_Y -= Bullet_Ychange

    # Check for collisions
    for i in range(InvaderCount):
        if Invader_Y[i] >= 450:
            if abs(Player_X - Invader_X[i]) < 80:
                game_over()
                break

        if Invader_X[i] >= 735 or Invader_X[i] <= 0:
            Invader_Xchange[i] *= -1
            Invader_Y[i] += Invader_Ychange[i]

        collision = isCollision(Bullet_X, Invader_X[i], Bullet_Y, Invader_Y[i])
        if collision:
            Score_val += 1
            Bullet_Y = 600
            BulletStaet = "rest"
            Invader_X[i] = random.randint(64, 736)
            Invader_Y[i] = random.randint(30, 200)
            Invader_Xchange[i] *= -1

        Invader(Invader_X[i], Invader_Y[i], i)

    # Boundary checking for player
    if Player_X <= 16:
        Player_X = 16
    elif Player_X >= 785:
        Player_X = 785
    
    #if Player_Y <= bottom boundary:
        #Player_Y = bottom boundary
    #elif Player_Y >= top boundary:
        #Player_Y = top boundary:

    # Render player and score
    Player(Player_X, Player_Y)
    show_Score(5, 5)
    
    pygame.display.update()
    clock.tick(FPS)  # Limit frame rate
