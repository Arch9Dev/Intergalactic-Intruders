from typing import Any
import pygame
import images
from PageList import pagelist


# Initialize Pygame
pygame.init()

# SCREEN
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND_IMAGE = images.load_background_image()


#Colours
WHITE = (250, 249, 246)
BLACK = (26, 26, 42)
GREY = (190, 176, 167)
RED_DARK = (255, 60, 0)
RED_DARKER = (208, 48, 0)
RED_LIGHT = (255, 0, 60)
BLUE_DARK = (0, 60, 255)
BLUE_DARKER = (0, 60, 200)
BLUE_LIGHT = (70, 235, 255)
GREEN_DARK = (20, 180, 40)#this is a darker green based o the test colour
GREEN_DARKER = (60, 150, 0)
GREEN_LIGHT = (20, 230, 6)#this now the test colour
ORANGE_DARK = (255, 195, 0)
ORANGE_DARKER = (255, 111, 0)
ORANGE_LIGHT = (255, 235, 0)



Colour_Palettes = {
    "Red_Buttons": {
        "Text_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Background_Colour": {"Normal": RED_DARK, "Hover": RED_LIGHT},
        "Border_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Border_Colour_two": {"Normal": WHITE, "Hover": BLACK}
    },
    "Green_Buttons": {
        "Text_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Background_Colour": {"Normal": GREEN_LIGHT, "Hover": GREEN_DARK},
        "Border_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Border_Colour_two": {"Normal": WHITE, "Hover": BLACK}
    },
    "Blue_Buttons": {
        "Text_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Background_Colour": {"Normal": BLUE_LIGHT, "Hover": BLUE_DARK},
        "Border_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Border_Colour_two": {"Normal": WHITE, "Hover": BLACK}
    },
    "Orange_Buttons":{
        "Text_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Background_Colour": {"Normal": ORANGE_LIGHT, "Hover": ORANGE_DARK},
        "Border_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Border_Colour_two": {"Normal": WHITE, "Hover": BLACK}
    },
    "Timer": {
        "Text_Colour": WHITE,
        "Background_Colour": BLUE_LIGHT,
        "Border_Colour": BLACK
    }
}






# Button dimensions
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_GAP = 20
BUTTON_BORDER_WIDTH = 4


# Back Button
BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
BUTTON_Y = 300
BUTTON_GAP = BUTTON_HEIGHT + BUTTON_GAP
BUTTON_W = BUTTON_WIDTH
BUTTON_H = BUTTON_HEIGHT

# Fonts
def FontResizable(FontSize):
    return pygame.font.Font("Intergalactic-Intruders\Font\immermann.ttf", FontSize)
FONT = pygame.font.Font("Intergalactic-Intruders\Font\immermann.ttf", 36)
TITLE_FONT = pygame.font.Font(None, 48)

def load_xolonium_font(font_size):
    # Load the custom font
    xolonium_font_path = "Intergalactic-Intruders\Fonts\Xolonium.ttf"
    xolonium_font = pygame.font.Font(xolonium_font_path, font_size)
    return xolonium_font

def load_immermann_font(font_size):
    immermann_font_path = "Intergalactic-Intruders/Fonts/Immermann.ttf"
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




# Slider positions and sizes
SLIDER_WIDTH = 200
SLIDER_HEIGHT = 10

MAIN_VOLUME_SLIDER_POS = (SCREEN_WIDTH // 2, 200)
MUSIC_SLIDER_POS = (SCREEN_WIDTH // 2, 300)
SOUND_EFFECTS_SLIDER_POS = (SCREEN_WIDTH // 2, 400)

def draw_circle(screen, colour, position, radius):
    pygame.draw.circle(screen, colour, position, radius)



def draw_button(screen, x, y, width, height, text):
    pygame.draw.rect(screen, RED_DARK, (x, y, width, height))
    pygame.draw.rect(screen, BLACK, (x, y, width, height), BUTTON_BORDER_WIDTH)  # Draw border
    text_surface = FONT.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

def draw_gunshot_button(screen, x, y, width, height, text):
    pygame.draw.rect(screen, RED_DARK, (x, y, width, height))
    pygame.draw.rect(screen, BLACK, (x, y, width, height), BUTTON_BORDER_WIDTH)  # Draw border
    text_surface = FONT.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)


# Back button
BACK_BUTTON = pygame.Rect(20, 20, 100, 40)

class Button:
    def __init__(self, button_text, Offset_X, Offset_Y, width_Offset, height_Offset, colour_palette):
        self.X = Offset_X if Offset_X != 0 else BUTTON_X
        self.Y = (Offset_Y + BUTTON_GAP) if Offset_Y != 0 else BUTTON_Y
        self.width = (BUTTON_WIDTH + width_Offset)
        self.height = (BUTTON_HEIGHT + height_Offset)
        self.border_thickness = BUTTON_BORDER_WIDTH
        self.screen = screen
        self.hovered = False
        self.clicked = False
        self.colour_palette = colour_palette
        self.text = button_text
        self.rect = pygame.Rect(self.X, self.Y, self.width, self.height)
        self.border_radius = 15

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and self.clicked:
            self.clicked = False

    def draw(self):
        Text_Colour = self.colour_palette["Text_Colour"]["Normal"]
        Hover_Text_Colour = self.colour_palette["Text_Colour"]["Hover"]
        Back_Colour = self.colour_palette["Background_Colour"]["Normal"]
        Hover_Back_Colour = self.colour_palette["Background_Colour"]["Hover"]
        Border_Colour = self.colour_palette["Border_Colour"]["Normal"]
        Hover_Border_Colour = self.colour_palette["Border_Colour"]["Hover"]
        Border_Colour_Two = self.colour_palette["Border_Colour_two"]["Normal"]
        Hover_Border_Colour_Two = self.colour_palette["Border_Colour_two"]["Hover"]

        if self.clicked:
            adjusted_rect = self.rect.inflate(-5, -5)  # Slightly smaller to indicate press
            pygame.draw.rect(self.screen, Hover_Back_Colour, adjusted_rect, border_radius=self.border_radius)
            pygame.draw.rect(self.screen, Hover_Border_Colour, adjusted_rect, self.border_thickness, border_radius=self.border_radius)
            text_surface = FONT.render(self.text, True, Hover_Text_Colour)
        elif self.hovered:
            shadow_rect = self.rect.inflate(10, 10)  # Slightly larger for shadow effect
            shadow_rect.topleft = (self.rect.left + 5, self.rect.top + 5)
            pygame.draw.rect(self.screen, (50, 50, 50), shadow_rect, border_radius=self.border_radius)  # Shadow color
            pygame.draw.rect(self.screen, Hover_Back_Colour, self.rect.inflate(5, 5), border_radius=self.border_radius)
            pygame.draw.rect(self.screen, Hover_Border_Colour_Two, self.rect.inflate(10, 10), self.border_thickness, self.border_radius)
            pygame.draw.rect(self.screen, Hover_Border_Colour, self.rect.inflate(5, 5), self.border_thickness, self.border_radius)
            text_surface = FONT.render(self.text, True, Hover_Text_Colour)
        else:
            pygame.draw.rect(self.screen, Back_Colour, self.rect, border_radius=self.border_radius)
            pygame.draw.rect(self.screen, Border_Colour_Two, self.rect.inflate(5,5), self.border_thickness, self.border_radius)

            pygame.draw.rect(self.screen, Border_Colour, self.rect, self.border_thickness, border_radius=self.border_radius)

            text_surface = FONT.render(self.text, True, Text_Colour)

        text_rect = text_surface.get_rect(center=(self.X + self.width // 2, self.Y + self.height // 2))
        self.screen.blit(text_surface, text_rect)


class QuitButton(Button):
    def __init__(self, colour_palette):
        Corner_Offset = 40
        Offset_X = (SCREEN_WIDTH - (BACK_BUTTON.width + Corner_Offset))
        Offset_Y = (SCREEN_HEIGHT - (BUTTON_GAP + BACK_BUTTON.height + Corner_Offset))
        width_Offset = (BACK_BUTTON.width - BUTTON_WIDTH)
        height_Offset =(BACK_BUTTON.height - BUTTON_HEIGHT)
        button_text = "QUIT"
        super().__init__(button_text, Offset_X, Offset_Y, width_Offset, height_Offset, colour_palette)
    def Quit():
        pygame.quit()
        quit()

class BackButton(Button):
    def __init__(self,  colour_palette, ReturnPage  ):
        Corner_Offset = 40
        Offset_X = (SCREEN_WIDTH - (BACK_BUTTON.width + Corner_Offset))
        Offset_Y = (SCREEN_HEIGHT - (BUTTON_GAP + BACK_BUTTON.height + Corner_Offset))
        width_Offset = (BACK_BUTTON.width - BUTTON_WIDTH)
        height_Offset =(BACK_BUTTON.height - BUTTON_HEIGHT)
        button_text = "BACK"
        self.Returnpage = ReturnPage
        super().__init__(button_text, Offset_X, Offset_Y, width_Offset, height_Offset, colour_palette)   
    def ReturnTo(self):
        ReturnTo_pagelist = pagelist(self.Returnpage)
        ReturnTo_pagelist.switching()
        pygame.display.set_caption(F"{self.Returnpage}")

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


