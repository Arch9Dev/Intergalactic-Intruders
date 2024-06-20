
from PIL import Image, ImageFont, ImageDraw
import pygame

def textOutline(text: str, FontSize : int, thickness: int, Ouline_Colour: tuple, Text_Colour: tuple ):
    
    sizer = pygame.font.Font("Intergalactic-Intruders/Font/Xolonium.ttf", size=FontSize)
    textsize = sizer.render(" "+text+" ",0,(000,000,000))
    font = ImageFont.truetype(font="Intergalactic-Intruders/Font/Xolonium.ttf", size=FontSize) 
    im = Image.new('RGBA', (textsize.get_width()+thickness, textsize.get_height()+thickness))
    drawer = ImageDraw.Draw(im)

    fill_color = Ouline_Colour
    stroke_color = Text_Colour

    drawer.text((0, 0), text, font=font, fill=fill_color, stroke_width=thickness, stroke_fill=stroke_color)
    return  pygame.image.fromstring(im.tobytes(),im.size,'RGBA')

