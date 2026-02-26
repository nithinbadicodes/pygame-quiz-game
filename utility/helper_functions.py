import pygame
import sys
import os
from data.constants import PREV_RECT,NEXT_RECT
from data.constants import nav_button_font


### DO NOT CHANGE
def get_prev_next_buttons():
    from utility.blueprints import Button


    ### PREVIOUS AND NEXT BUTTON
    prev_button = Button(PREV_RECT,font=nav_button_font,text="Prev page")
    next_button = Button(NEXT_RECT,font = nav_button_font,text="Next page") 
    return prev_button,next_button


### ------- Checks if type is pygame.Rect or pygame.Surface ----------
### DO NOT CHANGE
def get_rect(obj):
    if isinstance(obj, pygame.Rect):
        return obj
    elif isinstance(obj, pygame.Surface):
        return obj.get_rect()
    else:
        raise TypeError("Expected Rect or Surface")
    


def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        test_surface = font.render(test_line, True, (0, 0, 0))

        if test_surface.get_width() <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    if current_line:
        lines.append(current_line.strip())

    return lines



def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def create_image(img_path,x,y,width,height):
    loaded_image = pygame.image.load(resource_path(img_path))
    scaled_image = pygame.transform.scale(loaded_image,(width,height))

    image_rect = scaled_image.convert_alpha().get_rect()
    image_rect.center =  (x,y)

    return scaled_image,image_rect


