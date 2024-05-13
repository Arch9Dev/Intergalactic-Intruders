import enum
# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
PURPLE = (213, 0, 255)
RED = (255, 0, 0)
Blue_dark = (0,70,255)
Blue_Light =(0,177,255)

class Button_Colours(enum.Enum):
    def  __init__(self,Text_Colour, Hover_Text_Colour, Back_Colour, Hover_Back_Colour, Border_Colour) :
        self.Text_Colour = Text_Colour
        self.Hover_Text_Colour = Hover_Text_Colour
        self.Back_Colour = Back_Colour 
        self.Hover_Back_Colour = Hover_Back_Colour 
        self.Border_Colour = Border_Colour
    def  Get_Text_Colour(self):
        return self.Text_Colour
    def  Get_Hover_Text_Colour(self):
        return self.Hover_Text_Colour 
    def Get_Back_Colour(self):
        return self.Back_Colour
    def  Get_Hover_Back_Colour(self):
        return self.Hover_Back_Colour
    def  Get_Border_Colour(self):
        return self.Border_Colour

Blue_Buttons = Button_Colours(BLACK,WHITE,Blue_Light,Blue_dark,BLACK)
