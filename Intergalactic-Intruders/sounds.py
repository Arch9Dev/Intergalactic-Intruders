import pygame

pygame.init()

# Load the sound with loop=True
Space_Sound = pygame.mixer.Sound("Intergalactic-Intruders/Sounds/SpaceAmbience.wav")
Space_Sound.set_volume(0.5)  # Set initial volume
Space_Sound.play(loops=-1)  # Play the sound with continuous looping

# Load gunshot sound
gunshot_sound = pygame.mixer.Sound("Intergalactic-Intruders/Sounds/gunshot.wav")

# Global variables to store volumes
MAIN_VOLUME = 0.5
MUSIC_VOLUME = 0.5
SOUND_EFFECTS_VOLUME = 0.5

# Function to set main volume
def set_main_volume(volume):
    global MAIN_VOLUME
    MAIN_VOLUME = volume

# Function to set music volume
def set_music_volume(volume):
    global MUSIC_VOLUME
    MUSIC_VOLUME = volume
    # Adjust music volume based on main volume
    Space_Sound.set_volume(MAIN_VOLUME * MUSIC_VOLUME)

# Function to set sound effects volume
def set_sound_effects_volume(volume):
    global SOUND_EFFECTS_VOLUME
    SOUND_EFFECTS_VOLUME = volume
    # Adjust sound effects volume based on main volume
    gunshot_sound.set_volume(MAIN_VOLUME * SOUND_EFFECTS_VOLUME)

def play_gunshot():
    # Set gunshot volume based on main volume
    gunshot_sound.set_volume(MAIN_VOLUME)
    # Play gunshot sound
    gunshot_sound.play()


