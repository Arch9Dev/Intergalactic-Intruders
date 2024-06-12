from typing import __all__
import pygame
import images
from sounds import *
from PageList import pagelist
import asyncio

Coords = tuple[float,float]
Colour = tuple[int,int,int]

# Initialize Pygame
pygame.init()

# SCREEN
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND_IMAGE = images.load_background_image()
NEWBG = images.load_background_image()

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
GREEN_DARK = (20, 180, 40)
GREEN_DARKER = (60, 150, 0)
GREEN_LIGHT = (20, 230, 6)
ORANGE_DARK = (255, 195, 0)
ORANGE_DARKER = (255, 111, 0)
ORANGE_LIGHT = (255, 235, 0)

Volume_Type = {
    "GET":
    {
        "MAIN" : get_main_volume,
        "MUSIC" : get_space_sound_volume,
        "SFX" : get_gunshot_sound_volume
    },
    "SET":
    {
        "MAIN" : set_main_volume,
        "MUSIC" : set_space_sound_volume,
        "SFX" : set_gunshot_sound_volume
    },
}

Colour_Palettes = {
    "Red_Buttons": {
        "Text_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Background_Colour": {"Normal": RED_DARK, "Hover": RED_LIGHT},
        "Border_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Border_Colour_two": {"Normal": BLACK, "Hover": BLACK}
    },
    "Green_Buttons": {
        "Text_Colour": {"Normal": BLACK, "Hover": BLACK},
        "Background_Colour": {"Normal": GREEN_LIGHT, "Hover": GREEN_LIGHT},
        "Border_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Border_Colour_two": {"Normal": BLACK, "Hover": BLACK}
    },
    "Blue_Buttons": {
        "Text_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Background_Colour": {"Normal": BLUE_LIGHT, "Hover": BLUE_DARK},
        "Border_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Border_Colour_two": {"Normal": BLACK, "Hover": WHITE}
    },
    "Orange_Buttons":{
        "Text_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Background_Colour": {"Normal": ORANGE_LIGHT, "Hover": ORANGE_DARK},
        "Border_Colour": {"Normal": BLACK, "Hover": WHITE},
        "Border_Colour_two": {"Normal": BLACK, "Hover": BLACK}
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
BUTTON_GAP = 70
BUTTON_BORDER_WIDTH = 4
BUTTON_X = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
BUTTON_Y = 350
#BUTTON_GAP = BUTTON_HEIGHT + BUTTON_GAP
BUTTON_W = BUTTON_WIDTH
BUTTON_H = BUTTON_HEIGHT

# Fonts
def FontResizable(FontSize):
    return pygame.font.Font("Intergalactic-Intruders/Font/immermann.ttf", FontSize)
FONT = pygame.font.Font("Intergalactic-Intruders/Font/immermann.ttf", 36)
TITLE_FONT = pygame.font.Font(None, 48)

def load_xolonium_font(font_size):
    # Load the custom font
    xolonium_font_path = "Intergalactic-Intruders/Font/xolonium.ttf"
    xolonium_font = pygame.font.Font(xolonium_font_path, font_size)
    return xolonium_font

def load_immermann_font(font_size):
    immermann_font_path = 'Intergalactic-Intruders/Font/Immermann.ttf'
    immerman_font = pygame.font.Font(immermann_font_path, font_size)
    return immerman_font


# Load title image
TITLE_IMAGE = images.load_title_image()
Logo_POS_Y = 170
Logo_POS = (TITLE_IMAGE.get_rect(center=(SCREEN_WIDTH // 2, 170)))

# Load intro image
INTRO_IMAGE = images.load_intro_image()

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



#Deprecated
# Slider positions and sizes
SLIDER_WIDTH = 400
SLIDER_HEIGHT = 10
#Deprecated
MAIN_VOLUME_SLIDER_POS = (SCREEN_WIDTH // 2, 200)
MUSIC_SLIDER_POS = (SCREEN_WIDTH // 2, 300)
SOUND_EFFECTS_SLIDER_POS = (SCREEN_WIDTH // 2, 400)
#Deprecated
def draw_circle(screen, colour, position, radius):
    pygame.draw.circle(screen, colour, position, radius)


#Deprecated
def draw_button(screen, x, y, width, height, text):#Deprecated
    pygame.draw.rect(screen, RED_DARK, (x, y, width, height))
    pygame.draw.rect(screen, BLACK, (x, y, width, height), BUTTON_BORDER_WIDTH)  # Draw border
    text_surface = FONT.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
#Deprecated
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


class Slider :
    def __init__(self,Label_Text : str ,Slider_Pos_X : float,Slider_Pos_Y : float,Type_Name : str) :
        #Needed Var's
        self.screen = screen
        self.Volume_Value = Volume_Type["GET"][Type_Name]()
        self.Muted = False if self.Volume_Value > 0 else True 
        self.Dragging = False
        self.Hovering_Slider_Track = False
        self.Hovering_MuteCheckbox = False
        self.TYPE = Type_Name
        self.Slider_Track_Thickness = 12
        self.Slider_Track_Length = 400
        #Colours
        self.Slider_Colours ={
            "Colour_Slider_Track" : {
                "NORMAL": {"FillTrack": GREY, "BackTrack":BLACK},
                "HOVERING":{"FillTrack": WHITE, "BackTrack":BLACK},
                "MUTED": GREY 
            },
            "Colour_Slider_Thumb" : {
                "NORMAL": {"Center":BLACK,"Ring":WHITE},
                "DRAGGING":{"Center":WHITE,"Ring":BLACK},
                "MUTED":{"Center":GREY,"Ring":GREY}
            },
            "Background_Box": {"UNMUTED": BLUE_LIGHT, "MUTED":RED_LIGHT},
            "Mute_Checkbox": {
                "UNMUTED":{
                    "NORMAL":  {"Center":GREY,"Border":WHITE},
                    "HOVERING": {"Center":WHITE,"Border":GREY}
                },
                "MUTED":{
                    "NORMAL": {"Center":GREY,"Border":WHITE,"Cross": WHITE},
                    "HOVERING": {"Center":WHITE,"Border":GREY,"Cross": GREY}
                    },
            } 
        }
        #label
        self.Label = FONT.render(Label_Text,True,BLACK)
        Label_Gap_X = self.Label.get_width()+50
        Label_Gap_Y = self.Label.get_height() / 2
        self.Label_POS = (Slider_Pos_X - Label_Gap_X, Slider_Pos_Y - Label_Gap_Y  ) 
        #background Box
        BackgroundBox_TopLeft = (self.Label_POS[0],self.Label_POS[1])
        BackgroundBox_WidthHeight =( self.Slider_Track_Length + 50 + self.Label.get_width() ,self.Label.get_height())
        self.BackgroundBox  = pygame.Rect(BackgroundBox_TopLeft,BackgroundBox_WidthHeight).inflate(22,19)
        
        #Slider Track
        Slider_Track_TopLeft  = (Slider_Pos_X - 15, self.BackgroundBox.centery - self.Slider_Track_Thickness  /2 )
        Slider_Track_WidthHeight =( self.Slider_Track_Length, self.Slider_Track_Thickness)
        self.Slider_Track_Rect  = pygame.Rect(Slider_Track_TopLeft ,Slider_Track_WidthHeight)        
        self.SLIDER_Track_POS = [self.Slider_Track_Rect.x,self.Slider_Track_Rect.y] 
        
        #Slider_Thumb
        self.Slider_Thumb_Radius =  self.Slider_Track_Thickness
        Slider_Thumb_X =  Slider_Pos_X + self.Volume_Value * self.Slider_Track_Length
        Slider_Thumb_Y =  self.Slider_Track_Rect.centery
        Slider_Thumb_Rect_TopLeft =(Slider_Thumb_X-self.Slider_Thumb_Radius,Slider_Pos_Y-self.Slider_Thumb_Radius,)
        Slider_Thumb_Rect_WidthHeight = (self.Slider_Thumb_Radius*2, self.Slider_Thumb_Radius*2)
        self.Slider_Thumb_Rect = pygame.Rect(Slider_Thumb_Rect_TopLeft,Slider_Thumb_Rect_WidthHeight)        
        self.Slider_Thumb_Pos = (Slider_Thumb_X,Slider_Thumb_Y)
        
        #Slider Track Fill (Volume indicator) 
        Slider_Track_Fill_TopLeft = self.SLIDER_Track_POS[0],self.SLIDER_Track_POS[1]
        Slider_Track_Fill_WidthHeight = (self.Slider_Thumb_Rect.centerx-self.SLIDER_Track_POS[0], self.Slider_Track_Rect.height)
        self.Slider_Track_Fill_Rect = pygame.Rect(Slider_Track_Fill_TopLeft,Slider_Track_Fill_WidthHeight)
        
        #Mute_Checkbox
        Mute_Checkbox_TopLeft = (self.BackgroundBox.topright[0]+self.BackgroundBox.height*0.7/2, self.BackgroundBox.topright[1] )
        Mute_Checkbox_WidthHeight =(self.BackgroundBox.height,self.BackgroundBox.height)
        self.Mute_Checkbox_Rect = pygame.Rect(Mute_Checkbox_TopLeft,Mute_Checkbox_WidthHeight)
        self.Cross_1 =  (self.Mute_Checkbox_Rect.topleft[0]+7,self.Mute_Checkbox_Rect.topleft[1]+7),(self.Mute_Checkbox_Rect.bottomright[0]-7,self.Mute_Checkbox_Rect.bottomright[1]-7)
        self.Cross_2 = (self.Mute_Checkbox_Rect.topright[0]-7,self.Mute_Checkbox_Rect.topright[1]+7),(self.Mute_Checkbox_Rect.bottomleft[0]+7,self.Mute_Checkbox_Rect.bottomleft[1]-7)
    def CheckMute(self):
        self.Muted = False if self.Volume_Value > 0 else True 

    def mute(self):
        if self.Muted == True:
            self.Volume_Value = 0.01
            self.Muted = False 
        else:
            self.Muted =True
            # volume
            Volume_Type["SET"][self.TYPE](0)
            self.Volume_Value = 0
            self.Volume_Value = max(0,min(1,self.Volume_Value))
            Volume_Type["SET"][self.TYPE](self.Volume_Value)
            # Slider_Thumb
            self.Slider_Thumb_Pos = (int(self.SLIDER_Track_POS[0] +  self.Volume_Value * self.Slider_Track_Length ), self.Slider_Track_Rect.centery)
            Slider_Thumb_Rect_POSX = (self.Slider_Thumb_Pos[0]-self.Slider_Thumb_Radius,self.Slider_Thumb_Pos[1]-self.Slider_Thumb_Radius)
            Slider_Thumb_Rect_POSY = (self.Slider_Thumb_Radius*2, self.Slider_Thumb_Radius*2)
            self.Slider_Thumb_Rect = pygame.Rect(Slider_Thumb_Rect_POSX ,Slider_Thumb_Rect_POSY)
            #Slider Track Fill (Volume indicator) 
            Slider_Track_Fill_TopLeft = self.SLIDER_Track_POS[0],self.SLIDER_Track_POS[1]
            Slider_Track_Fill_WidthHeight = (self.Slider_Thumb_Rect.centerx-self.SLIDER_Track_POS[0], self.Slider_Track_Rect.height)
            self.Slider_Track_Fill_Rect = pygame.Rect(Slider_Track_Fill_TopLeft,Slider_Track_Fill_WidthHeight)
            
    def Drag(self, POS):
        if self.Muted == False :
            self.Drag_Pos = [POS[0],POS[1]]
            # volume
            self.Volume_Value = (self.Drag_Pos[0]-(self.SLIDER_Track_POS[0] )) / self.Slider_Track_Length
            self.Volume_Value = max(0,min(1,self.Volume_Value))
            Volume_Type['SET'][self.TYPE](self.Volume_Value)
            # Slider_Thumb
            self.Slider_Thumb_Pos = (int(self.SLIDER_Track_POS[0] +  self.Volume_Value * self.Slider_Track_Length ), self.Slider_Track_Rect.centery)
            Slider_Thumb_Rect_POSX = (self.Slider_Thumb_Pos[0]-self.Slider_Thumb_Radius,self.Slider_Thumb_Pos[1]-self.Slider_Thumb_Radius)
            Slider_Thumb_Rect_POSY = (self.Slider_Thumb_Radius*2, self.Slider_Thumb_Radius*2)
            self.Slider_Thumb_Rect = pygame.Rect(Slider_Thumb_Rect_POSX ,Slider_Thumb_Rect_POSY)
            #Slider Track Fill (Volume indicator) 
            Slider_Track_Fill_TopLeft = self.SLIDER_Track_POS[0],self.SLIDER_Track_POS[1]
            Slider_Track_Fill_WidthHeight = (self.Slider_Thumb_Rect.centerx-self.SLIDER_Track_POS[0], self.Slider_Track_Rect.height)
            self.Slider_Track_Fill_Rect = pygame.Rect(Slider_Track_Fill_TopLeft,Slider_Track_Fill_WidthHeight)

    def draw(self):

        Colour_Slider_Thumb = self.Slider_Colours["Colour_Slider_Thumb"]
        Colour_Slider_Track = self.Slider_Colours["Colour_Slider_Track"]
        Colour_Background = self.Slider_Colours["Background_Box"]
        Colour_Mute_Checkbox = self.Slider_Colours["Mute_Checkbox"]
        test1 = (self.Cross_1[0][0],self.Cross_1[0][1])
        test2 = self.Cross_1[0][0]

        CrossCords = [[self.Cross_1[0],self.Cross_1[1]],[self.Cross_2[0],self.Cross_2[1]]]
        def Draw_Checkbox(Muted :bool,Hovered : bool):
            if Muted:
                if Hovered:
                    pygame.draw.rect(self.screen,Colour_Mute_Checkbox["MUTED"]["HOVERING"]["Center"],self.Mute_Checkbox_Rect,0,15)
                    pygame.draw.line(self.screen,Colour_Mute_Checkbox["MUTED"]["HOVERING"]["Cross"],CrossCords[0][0],CrossCords[0][1],5)
                    pygame.draw.line(self.screen,Colour_Mute_Checkbox["MUTED"]["HOVERING"]["Cross"],CrossCords[1][0],CrossCords[1][1],5)
                    pygame.draw.rect(self.screen,Colour_Mute_Checkbox["MUTED"]["HOVERING"]["Border"],self.Mute_Checkbox_Rect,5,15)
                else:
                    pygame.draw.rect(self.screen,Colour_Mute_Checkbox["MUTED"]["NORMAL"]["Center"],self.Mute_Checkbox_Rect,0,15)
                    pygame.draw.line(self.screen,Colour_Mute_Checkbox["MUTED"]["NORMAL"]["Cross"],CrossCords[0][0],CrossCords[0][1],5)
                    pygame.draw.line(self.screen,Colour_Mute_Checkbox["MUTED"]["NORMAL"]["Cross"],CrossCords[1][0],CrossCords[1][1],5)
                    pygame.draw.rect(self.screen,Colour_Mute_Checkbox["MUTED"]["NORMAL"]["Border"],self.Mute_Checkbox_Rect,5,15)
            else:
                if Hovered:
                    pygame.draw.rect(self.screen,Colour_Mute_Checkbox["UNMUTED"]["HOVERING"]["Center"],self.Mute_Checkbox_Rect,0,15)
                    pygame.draw.rect(self.screen,Colour_Mute_Checkbox["UNMUTED"]["HOVERING"]["Border"],self.Mute_Checkbox_Rect,5,15)
                else:
                    pygame.draw.rect(self.screen,Colour_Mute_Checkbox["UNMUTED"]["NORMAL"]["Center"],self.Mute_Checkbox_Rect,0,15)
                    pygame.draw.rect(self.screen,Colour_Mute_Checkbox["UNMUTED"]["NORMAL"]["Border"],self.Mute_Checkbox_Rect,5,15)
        def Draw_SliderBar(Muted : bool,Hovered : bool):
            if Muted:
                pygame.draw.rect(self.screen,Colour_Slider_Track["MUTED"],self.Slider_Track_Rect,border_radius=10)
            elif Hovered:
                pygame.draw.rect(self.screen,Colour_Slider_Track["HOVERING"]["BackTrack"],self.Slider_Track_Rect,border_radius=10)
                pygame.draw.rect(self.screen,Colour_Slider_Track["HOVERING"]["FillTrack"],self.Slider_Track_Fill_Rect,border_radius=10)
            else:
                pygame.draw.rect(self.screen,Colour_Slider_Track["NORMAL"]["BackTrack"],self.Slider_Track_Rect,border_radius=10)            
                pygame.draw.rect(self.screen,Colour_Slider_Track["NORMAL"]["FillTrack"],self.Slider_Track_Fill_Rect,border_radius=10)

        def Draw_Slider_Thumb(Muted : bool,Dragging : bool,):
            if Muted:
                pygame.draw.circle(screen,Colour_Slider_Thumb["MUTED"]["Ring"],self.Slider_Thumb_Pos,self.Slider_Thumb_Radius)
                pygame.draw.circle(screen,Colour_Slider_Thumb["MUTED"]["Center"],self.Slider_Thumb_Pos,self.Slider_Thumb_Radius*0.7)
            elif Dragging:
                pygame.draw.circle(screen,Colour_Slider_Thumb["DRAGGING"]["Ring"],self.Slider_Thumb_Pos,self.Slider_Thumb_Radius)
                pygame.draw.circle(screen,Colour_Slider_Thumb["DRAGGING"]["Center"],self.Slider_Thumb_Pos,self.Slider_Thumb_Radius*0.7)
            else:
                pygame.draw.circle(screen,Colour_Slider_Thumb["NORMAL"]["Ring"],self.Slider_Thumb_Pos,self.Slider_Thumb_Radius)
                pygame.draw.circle(screen,Colour_Slider_Thumb["NORMAL"]["Center"],self.Slider_Thumb_Pos,self.Slider_Thumb_Radius*0.7)
        def Draw_BackgroundBox(Muted : bool):
            if Muted :
                pygame.draw.rect(self.screen,Colour_Background["MUTED"],self.BackgroundBox,border_radius=7)
            else:
                pygame.draw.rect(self.screen,Colour_Background["UNMUTED"],self.BackgroundBox,border_radius=7)
        def Draw_Label():
            self.screen.blit(self.Label,self.Label_POS)

        Draw_Checkbox(self.Muted,self.Hovering_MuteCheckbox)
        Draw_BackgroundBox(self.Muted)
        Draw_Label()
        Draw_SliderBar(self.Muted,self.Hovering_Slider_Track)
        Draw_Slider_Thumb(self.Muted,self.Dragging)

class TileLable:
    def __init__(self, X_Y : Coords, Fontsize : int,Lable_Text : str,Text_Colour: Colour,Background_Colour : Colour,AA :bool):
        Label_Font = load_immermann_font(Fontsize)
        self.Lable = Label_Font.render(Lable_Text,AA,Text_Colour,Background_Colour)
        self.X_Y = X_Y
    def draw(self):
        self.Lable.get_rect(center = self.X_Y)
        screen.blit(self.Lable,self.X_Y)
    





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

