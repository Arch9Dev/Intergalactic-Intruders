import pygame
import images
import Colours

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
FONT = pygame.font.Font("Intergalactic-Intruders\Font\immermann.ttf", 36)
TITLE_FONT = pygame.font.Font(None, 48)


# Load title image
TITLE_IMAGE = images.load_title_image()

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
    "TUTORIAL PAGE PLACE HOLDER"
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

class Button:
   
    def __init__(self,screen, Button_Text, x, y, width, height,  Colour_Palette = Colours.Button_Colours):
        self.x, self.y, self.width, self.height = x, y, width, height
        self.border_coords = ((x, y), (x+width, y), (x+width, y+height), (x, y+height))
        self.border_thickness = 3
        self.screen = screen
        self.hovered = False
        self.Colour_Palette = Colour_Palette 
        self.Text = Button_Text
        self.rect = pygame.Rect( x, y, width, height) 
    def draw(self):
        screen = self.screen
        Text_Colour = self.Colour_Palette.Get_Text_Colour()
        Hover_Text_Colour = self.Colour_Palette.Get_Hover_Text_Colour()
        Back_Colour = self.Colour_Palette.Get_Back_Colour()
        Hover_BackColour = self.Colour_Palette.Get_Hover_Back_Colour()
        Border_Colour = self.Colour_Palette.Get_Border_Colour()
        if self.hovered :
            pygame.draw.rect(screen, Hover_BackColour, self.rect)
            text_surface = FONT.render(self.Text, True, Hover_Text_Colour)
        else:
            pygame.draw.rect(screen, Back_Colour, self.rect)
            text_surface = FONT.render(self.Text, True, Text_Colour)
        
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        pygame.draw.lines(screen, Border_Colour, True, self.border_coords, self.border_thickness)
        screen.blit(text_surface, text_rect)

        

def draw_button(screen, x, y, width, height, text, Background = None):
    if Background != None:
        pygame.draw.rect(screen, Background, (x, y, width, height))
        pygame.draw.rect(screen, BLACK, (x, y, width, height), BUTTON_BORDER_WIDTH)  # Draw border
        text_surface = FONT.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
        screen.blit(text_surface, text_rect)
    else:
        pygame.draw.rect(screen, RED, (x, y, width, height))
        pygame.draw.rect(screen, BLACK, (x, y, width, height), BUTTON_BORDER_WIDTH)  # Draw border
        text_surface = FONT.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
        screen.blit(text_surface, text_rect)