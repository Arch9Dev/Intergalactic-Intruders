import pygame
import os


# Initialize Pygame
pygame.init()


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
PURPLE = (213, 0, 255)
RED = (255, 0, 0)


# Button dimensions
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_GAP = 20
BUTTON_BORDER_WIDTH = 2


# Fonts
FONT = pygame.font.Font(None, 36)
TITLE_FONT = pygame.font.Font(None, 48)


# Load title image
TITLE_IMAGE = pygame.image.load(os.path.join("Intergalactic-Intruders", "images", "title.png"))
TITLE_IMAGE = pygame.transform.scale(TITLE_IMAGE, (600, 600))


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


# Back button
BACK_BUTTON = pygame.Rect(20, 20, 100, 40)


def draw_button(screen, x, y, width, height, text):
    pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.draw.rect(screen, BLACK, (x, y, width, height), BUTTON_BORDER_WIDTH)  # Draw border
    text_surface = FONT.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
