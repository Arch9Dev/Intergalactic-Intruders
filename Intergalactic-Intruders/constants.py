import pygame
import images


# Initialize Pygame
pygame.init()


# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
PURPLE = (213, 0, 255)
RED = (255, 0, 0)

# SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Button dimensions
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_GAP = 20
BUTTON_BORDER_WIDTH = 2


# Fonts
FONT = pygame.font.Font(None, 36)
TITLE_FONT = pygame.font.Font(None, 48)
def load_xolonium_font(font_size):
    # Load the custom font
    xolonium_font_path = "Intergalactic-Intruders/Fonts/Xolonium.ttf"
    xolonium_font = pygame.font.Font(xolonium_font_path, font_size)
    return xolonium_font


# Load title image
TITLE_IMAGE = images.load_title_image()


# Load tutorial image
TUTORIAL_IMAGE = images.load_tutorial_image()

# Game text
GAME_TEXT = [
    "GAME PAGE PLACE HOLDER"
]


# Setting text
SETTINGS_TEXT = [
    "SETTINGS PAGE PLACE HOLDER"
]


# Tutorial text
TUTORIAL_TEXT = [
        "                YOUR MISSION IS SIMPLE                        ",
        "",
        "DEFEND YOUR BASE FROM THE APPROACHING WAVES OF ALIEN INTRUDERS",
        "",
        "USE YOUR SHIP'S LASER BLASTERS TO SHOOT DOWN THE INTRUDERS"
        "",
        "BEFORE THEY CAN REACH YOU AND START DESTROYING YOUR DEFENSES",
        "",
        "ALONG THE WAY YOU CAN GAIN UPGRADES",
        "",
        "WHICH MAY BE HELPFUL IN SUCCEEDING THE MISSION",
        "",
        "GOOD LUCK SOLDIER"
]


# Audio text
AUDIO_TEXT = [
    "AUDIO SETTINGS PAGE PLACE HOLDER"
]


# Display text
DISPLAY_TEXT = [
    "DISPLAY SETTINGS PAGE PLACE HOLDER"
]


# Controls text
CONTROLS_TEXT = [
    "CONTROLS SETTINGS PAGE PLACE HOLDER"
]

# Levels text
LEVELS_TEXT = [
    "LEVELS PLACE HOLDER"
]


# Time Trial Text
TIMETRIAL_TEXT = [
    "TIME TRIAL PLACE HOLDER"
]

# Back button
BACK_BUTTON = pygame.Rect(20, 20, 100, 40)

# Slider positions and sizes
SLIDER_WIDTH = 200
SLIDER_HEIGHT = 10

MAIN_VOLUME_SLIDER_POS = (SCREEN_WIDTH // 2, 200)
MUSIC_SLIDER_POS = (SCREEN_WIDTH // 2, 300)
SOUND_EFFECTS_SLIDER_POS = (SCREEN_WIDTH // 2, 400)



def draw_circle(screen, colour, position, radius):
    pygame.draw.circle(screen, colour, position, radius)

def draw_button(screen, x, y, width, height, text):
    pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.draw.rect(screen, BLACK, (x, y, width, height), BUTTON_BORDER_WIDTH)  # Draw border
    text_surface = FONT.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
