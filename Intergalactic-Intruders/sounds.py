import pygame

pygame.init()

# Load the sound with loop=True
Space_Sound = pygame.mixer.Sound("Intergalactic-Intruders/Sounds/SpaceAmbience.wav")
Space_Sound.set_volume(0.5)  # Set initial volume
Space_Sound.play(loops=-1)  # Play the sound with continuous looping

# Load gunshot sound
gunshot_sound = pygame.mixer.Sound("Intergalactic-Intruders/Sounds/gunshot.wav")

# Global variable to store main volume
MAIN_VOLUME = 0.5

# Function to play gunshot sound
def play_gunshot():
    # Set gunshot volume based on main volume
    gunshot_sound.set_volume(MAIN_VOLUME)
    # Play gunshot sound
    gunshot_sound.play()
