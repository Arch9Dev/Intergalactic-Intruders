# images.py
import pygame
import os

# Initialize Pygame
pygame.init()

# Load title image
def load_title_image():
    title_image_path = os.path.join("Intergalactic-Intruders", "images", "logo4.png")
    title_image_path = os.path.join("Intergalactic-Intruders", "images", "logo4.png")
    title_image = pygame.image.load(title_image_path)
    return pygame.transform.scale(title_image, (500, 400))


# Load tutorial image
def load_tutorial_image():
    tutorial_image_path = os.path.join("Intergalactic-Intruders", "images", "TutorialText.png")
    tutorial_image = pygame.image.load(tutorial_image_path)
    return pygame.transform.scale(tutorial_image, (500, 500) )

# Load controls image
def load_controls_image():
    controls_image_path = os.path.join("Intergalactic-Intruders", "images", "controls.png")
    controls_image = pygame.image.load(controls_image_path)
    return pygame.transform.scale(controls_image, (600, 400))



def load_background_image():
    newBG_path = os.path.join("Intergalactic-Intruders", "images", "NewBG.png")
    newBG_image = pygame.image.load(newBG_path)
    return pygame.transform.scale(newBG_image, (1000, 800))

# Load intro image
def load_intro_image():
    intro_image_path = os.path.join("Intergalactic-Intruders", "images", "intro.png")
    intro_image = pygame.image.load(intro_image_path)
    return pygame.transform.scale(intro_image, (1000, 800))
