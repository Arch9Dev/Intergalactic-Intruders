import pygame
import os

# Initialize Pygame
pygame.init()

# Load title image
def load_title_image():
    title_image_path = os.path.join("Intergalactic-Intruders", "images", "title.png")
    title_image = pygame.image.load(title_image_path)
    return pygame.transform.scale(title_image, (600, 600))