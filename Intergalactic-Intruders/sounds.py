import pygame

pygame.init()

# Load the sound with loop=True
Space_Sound = pygame.mixer.Sound("Intergalactic-Intruders/Sounds/SpaceAmbience.wav")
Space_Sound.set_volume(0.5)  # Set initial volume
Space_Sound.play(loops=-1)  # Play the sound with continuous looping

# Load gunshot sound# Load game sounds
gunshot_sound = pygame.mixer.Sound("Intergalactic-Intruders/Sounds/gunshot.wav") #Gunshot
gunshot_sound.set_volume(1.0)

AlienDeath_sound = pygame.mixer.Sound("Intergalactic-Intruders/Sounds/aliendeath.wav") #Alien Death
AlienDeath_sound.set_volume(1.0)

BarrierDestroyed_sound = pygame.mixer.Sound("Intergalactic-Intruders/Sounds/BarrierDestroyed.wav") # Barrier Destroyed
BarrierDestroyed_sound.set_volume(1.0)

PlayerHit_sound = pygame.mixer.Sound("Intergalactic-Intruders/Sounds/BarrierDestroyed.wav") # Player hit
PlayerHit_sound.set_volume(1.0)

PowerUp_sound = pygame.mixer.Sound("Intergalactic-Intruders/Sounds/PowerUp.wav")
PowerUp_sound.set_volume(1.0)


# Global variable to store main volume
MAIN_VOLUME = 0.5

# Variables to store individual volumes
music_volume = 0.5
sound_effects_volume = 0.5

def play_gunshot():
    gunshot_sound.play()
    
def play_aliendeath():
    AlienDeath_sound.play()
    
def play_barrierdestroyed():
    BarrierDestroyed_sound.play()

def play_playerhit():
    PlayerHit_sound.play()
    
def play_powerup():
    PowerUp_sound.play()

def set_main_volume(volume):
    global MAIN_VOLUME
    MAIN_VOLUME = volume
    # Adjust the volume for all sounds
    Space_Sound.set_volume(MAIN_VOLUME * music_volume)
    gunshot_sound.set_volume(MAIN_VOLUME * sound_effects_volume)

def set_space_sound_volume(volume):
    global music_volume
    music_volume = volume
    Space_Sound.set_volume(MAIN_VOLUME * music_volume)

def set_soundfx(volume):
    global sound_effects_volume
    sound_effects_volume = volume
    gunshot_sound.set_volume(MAIN_VOLUME * sound_effects_volume)
    AlienDeath_sound.set_volume(MAIN_VOLUME * sound_effects_volume)
    BarrierDestroyed_sound.set_volume(MAIN_VOLUME * sound_effects_volume)
    PlayerHit_sound.set_volume(MAIN_VOLUME * sound_effects_volume)
    PowerUp_sound.set_volume(MAIN_VOLUME * sound_effects_volume)

def get_main_volume():
    return MAIN_VOLUME

def get_space_sound_volume():
    return music_volume

def get_SFX_Volume():
    return sound_effects_volume



# MORE SOUNDS NEED ADDING