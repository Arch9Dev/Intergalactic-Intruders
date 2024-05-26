import pygame
import math
import random

pygame.init()

# Set up the screen
Screen_Width = 800
Screen_Height = 1000
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))

# Load the background image
background_image = pygame.image.load('Intergalactic-Intruders/images/gameback1.png')

# Load the barrier image
barrier_image = pygame.image.load('Intergalactic-Intruders/images/barrier.png')

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
Player_Y = 923
Player_Xchange = 0
Player_Ychange = 0
Player_Health = 3  # Player's health
Accuracy = 100
Hits_Landed = 1
Shots_Taken = 1
Frames = 180
Time_trial = 'false'
Max_Invaders_YN = 'false'
Current_Invaders = 0
CoconutImg = 'true'

InvaderImag1 = pygame.image.load('Intergalactic-Intruders/images/Alion one (1) 1.gif')
InvaderImag2 = pygame.image.load('Intergalactic-Intruders/images/Alion two (1) 1.gif')
InvaderImag3 = pygame.image.load('Intergalactic-Intruders/images/Alinon three  (1) 1.gif')
InvaderImag4 = pygame.image.load('Intergalactic-Intruders/images/Mother Ship 1.gif')

Invader_X = []
Invader_Y = []
Invader_Xchange = []
Invader_Ychange = 50
InvaderCount = 30
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

# Initialize bullet lists for each invader
InvBullet_Xchange = 0
InvBullet_Ychange = 1  # Define InvBullet_Ychange here
Invader_Bullets = [[] for _ in range(InvaderCount)]
Bullet_Limit = 50  # Maximum number of bullets each invader can handle
Fire_rate = 7500

last_shot_times = []  # Track the last shot time for each invader

# Define barriers
barrier_width = 175
barrier_height = 100
barrier_y = 750  # Arbitrary height positioning for the barriers
barriers = [
    (68.75, barrier_y),
    (68.75 + barrier_width + 68.75, barrier_y),
    (68.75 + 2 * (barrier_width + 68.75), barrier_y)
]

# Define hitbox sizes
player_hitbox = (PlayerImag.get_width(), PlayerImag.get_height())
invader_hitbox = (64, 64)  # Assuming invaders are 64x64 pixels
bullet_hitbox = (BulletImag.get_width(), BulletImag.get_height())

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
if CoconutImg == 'true':
    while Running:
        # Blit the background image
        Screen.blit(background_image, (0, 0))

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - last_time_check

        if Time_trial == 'true':
            if elapsed_time >= 1000:
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

        if Player_Y <= 834:
            Player_Y = 834
        elif Player_Y >= 954:
            Player_Y = 954

        # Spawn invaders with a delay
        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time > spawn_delay and len(Invader_X) < InvaderCount and Max_Invaders_YN == 'false':
            rangom = random.randint(1, 4)  # Choose a random image for this invader
            Invader_X.append(0)
            Invader_Y.append(30)
            Invader_Xchange.append(1.7)
            Invader_Rangom.append(rangom)
            last_shot_times.append(current_time)  # Initialize the last shot time for this invader
            last_spawn_time = current_time
            Current_Invaders += 1
            if Current_Invaders >= InvaderCount and Time_trial == 'false':
                Max_Invaders_YN = 'true'

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

        # Inside the loop where invaders fire bullets:
        for i in range(len(Invader_X)):
            # Check if invader can fire a bullet
            if len(Invader_Bullets[i]) < Bullet_Limit:
                if current_time - last_shot_times[i] >= Fire_rate + random.randint(-Fire_rate//2, Fire_rate):
                    Invader_Bullets[i].append([Invader_X[i], Invader_Y[i]])
                    last_shot_times[i] = current_time

        # Inside the loop where you update invader bullet positions:
        for i in range(len(Invader_X)):
            for bullet in Invader_Bullets[i]:
                InvaderBullet(bullet[0], bullet[1], i)
                bullet[1] += InvBullet_Ychange
                if bullet[1] >= 1000:  # Check if bullet has reached bottom of the screen
                    Invader_Bullets[i].remove(bullet)
                    print('bullet removed')

        # Update player bullet position
        if Bullet_Y <= 0:
            Bullet_Y = 1000
            BulletStaet = "rest"
        if BulletStaet == "fire":
            Bullet(Bullet_X, Bullet_Y)
            Bullet_Y -= Bullet_Ychange

        # Check for collisions with player bullet
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

        # Check for collisions with invader bullets and barriers
        for i in range(len(Invader_X)):
            for bullet in Invader_Bullets[i]:
                bullet_rect = pygame.Rect(bullet[0], bullet[1], *bullet_hitbox)
                for barrier in barriers[:]:
                    barrier_rect = pygame.Rect(barrier[0], barrier[1], barrier_width, barrier_height)
                    if isCollision_Barrier(bullet[0], bullet[1], barrier_rect):
                        Invader_Bullets[i].remove(bullet)
                        break

        # Check for collisions between invaders and barriers
        for i in range(len(Invader_X)):
            invader_rect = pygame.Rect(Invader_X[i], Invader_Y[i], *invader_hitbox)
            for barrier in barriers[:]:
                barrier_rect = pygame.Rect(barrier[0], barrier[1], barrier_width, barrier_height)
                if invader_rect.colliderect(barrier_rect):
                    barriers.remove(barrier)
                    break

        # Check for collisions with invader bullets and player
        player_rect = pygame.Rect(Player_X, Player_Y, *player_hitbox)
        for i in range(len(Invader_X)):
            for bullet in Invader_Bullets[i][:]:
                bullet_rect = pygame.Rect(bullet[0], bullet[1], *bullet_hitbox)
                if bullet_rect.colliderect(player_rect):
                    Invader_Bullets[i].remove(bullet)
                    player_hit()
                    break

        # Render player, invaders, barriers, score, and health
        Player(Player_X, Player_Y)
        for i in range(len(Invader_X)):
            Invader(Invader_X[i], Invader_Y[i], Invader_Rangom[i])  # Pass the assigned rangom value
        for barrier in barriers:
            Screen.blit(barrier_image, barrier)
        show_Score(5, 5)
        show_Difficulty(130, 5, Frames)
        show_Acc(300, 5)
        show_Health(420, 5)  # Display player's health

        Frames = 180 * Difficulty * Time_Difficulty
        pygame.display.update()
        clock.tick(Frames)  # Limit frame rate based on difficulty
pygame.quit()