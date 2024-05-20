import pygame
import images
import settings
import play
import main

# Initialize Pygame
pygame.init()

# Colours
WHITE = (250, 250, 250)
BLACK = (26, 26, 42)
GREY = (200, 200, 200)
PURPLE = (213, 0, 255)
RED = (255, 0, 0)

RED_DARK = (255, 60, 0)
RED_LIGHT = (255, 90, 70)
BLUE_DARK = (0, 60, 255)
BLUE_LIGHT = (0, 160, 255)


Colour_Palettes = {
    "Red_Buttons": {
        "Text_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Background_Colour": {"Normal": RED_DARK, "Hover": RED_LIGHT},
        "Border_Colour": {"Normal": BLACK, "Hover": WHITE}
    },
    "Blue_Buttons": {
        "Text_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Background_Colour": {"Normal": BLUE_DARK, "Hover": BLUE_LIGHT},
        "Border_Colour": {"Normal": BLACK, "Hover": WHITE}
    },
    "Timer": {
        "Text_Colour": WHITE,
        "Background_Colour": BLUE_LIGHT,
        "Border_Colour": BLACK
    }
}



# Screen
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

def  Load_Immerman_Font(font_size):
    immermann_font_path = "Intergalactic-Intruders/Fonts/Immerman.tff"
    immerman_font = pygame.font.Font(immermann_font_path, font_size)
    return immerman_font


# Load title image
TITLE_IMAGE = images.load_title_image()

# Load tutorial image
TUTORIAL_IMAGE = images.load_tutorial_image()

# Load controls image
CONTROLS_IMAGE = images.load_controls_image()

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
BACK_BUTTON_X = 20
BACK_BUTTON_Y = 20
BACK_BUTTON_W = 100
BACK_BUTTON_H = 40


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

def draw_gunshot_button(screen, x, y, width, height, text):
    pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.draw.rect(screen, BLACK, (x, y, width, height), BUTTON_BORDER_WIDTH)  # Draw border
    text_surface = FONT.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)


# Back button
BACK_BUTTON = pygame.Rect(20, 20, 100, 40)

class Button:
    def __init__(self, screen, button_text, x, y, width, height, colour_palette):
        self.x, self.y, self.width, self.height = x, y, width, height
        self.border_coords = ((x, y), (x + width, y), (x + width, y + height), (x, y + height))
        self.border_thickness = 3
        self.screen = screen
        self.hovered = False
        self.colour_palette = colour_palette
        self.text = button_text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        Text_Colour = self.colour_palette["Text_Colour"]["Normal"]
        Hover_Text_Colour = self.colour_palette["Text_Colour"]["Hover"]
        Back_Colour = self.colour_palette["Background_Colour"]["Normal"]
        Hover_Back_Colour = self.colour_palette["Background_Colour"]["Hover"]
        Border_Colour = self.colour_palette["Border_Colour"]["Normal"]
        Hover_Border_Colour = self.colour_palette["Border_Colour"]["Hover"]

        if self.hovered:
            pygame.draw.rect(self.screen, Hover_Back_Colour, self.rect)
            text_surface = FONT.render(self.text, True, Hover_Text_Colour)
            pygame.draw.lines(self.screen, Hover_Border_Colour, True, self.border_coords, self.border_thickness)
        else:
            pygame.draw.rect(self.screen, Back_Colour, self.rect)
            text_surface = FONT.render(self.text, True, Text_Colour)
            pygame.draw.lines(self.screen, Border_Colour, True, self.border_coords, self.border_thickness)

        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.screen.blit(text_surface, text_rect)
        
class BackButton(Button):
    def __init__(self, screen, colour_palette, ReturnPage ):
        x = BACK_BUTTON.x 
        y = BACK_BUTTON.y
        button_text = "BACK"
        width = BACK_BUTTON.width
        height = BACK_BUTTON.height
        self.Returnpage = ReturnPage
        super().__init__(screen, button_text, x, y, width, height, colour_palette)     
    def ReturnTo(self):
        if self.Returnpage == "Main":
            main.main_menu()
        elif self.Returnpage == "PLAY":
            play.show_play()
        elif self.Returnpage == "SETTINGS":
            settings.show_settings()
        pygame.display.set_caption(self.Returnpage)

class Timer:
    def __init__(self, screen, time, x, y, width, height, fontsize):
        self.x, self.y, self.width, self.height = x, y, width, height
        self.border_coords = ((x, y), (x + width, y), (x + width, y + height), (x, y + height))
        self.border_thickness = 3
        self.screen = screen
        self.time = time
        self.fontsize = fontsize
        self.rect = pygame.Rect(x, y, width, height)
        self.colour_palette = Colour_Palettes["Timer"]

    def draw(self):
        Text_Colour = self.colour_palette["Text_Colour"]
        Back_Colour = self.colour_palette["Background_Colour"]
        Border_Colour = self.colour_palette["Border_Colour"]

        pygame.draw.rect(self.screen, Back_Colour, self.rect)
        text_surface = pygame.font.Font(None, self.fontsize).render(self.time, True, Text_Colour)
        pygame.draw.lines(self.screen, Border_Colour, True, self.border_coords, self.border_thickness)

        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.screen.blit(text_surface, text_rect)
