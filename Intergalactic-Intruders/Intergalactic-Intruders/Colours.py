import enum
class  SetColours(enum.Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (200, 200, 200)
    PURPLE = (213, 0, 255)
    RED = (255, 0, 0)
    #New Colours 
    Red_Dark = (175, 0, 35)
    Red_Light = (255,0,45)
    Blue_Dark = (0,0,127)
    Blue_Light =(0,70,255)

Colour_Palettes ={
    "Red_Buttons" : {
        "Text_Colour" : {"Normal" : SetColours.BLACK , "Hover" : SetColours.WHITE}, 
        "Background_Colour" :  {"Normal" : SetColours.Red_Dark , "Hover" : SetColours.Red_Light},
        "Border_Colour" : {"Normal" : SetColours.BLACK , "Hover" : SetColours.WHITE}},
    "Blue_Buttons" : {
        "Text_Colour" : {"Normal" : SetColours.BLACK , "Hover" : SetColours.WHITE}, 
        "Background_Colour" :  {"Normal" : SetColours.Blue_Dark , "Hover" : SetColours.Blue_Light},
        "Border_Colour" : {"Normal" : SetColours.BLACK , "Hover" : SetColours.WHITE}},
    "Timer" :{
        "Text_Colour" : SetColours.WHITE  ,  
        "Background_Colour" :  SetColours.Blue_Light,
        "Border_Colour" : SetColours.BLACK
    }
}


