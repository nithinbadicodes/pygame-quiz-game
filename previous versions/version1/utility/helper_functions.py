import pygame
from data.constants import WINDOW_WIDTH
from data.constants import PREV_RECT,NEXT_RECT


### DO NOT CHANGE
def get_prev_next_buttons():
    from utility.blueprints import Button


    ### PREVIOUS AND NEXT BUTTON
    prev_button = Button(PREV_RECT,text="Prev page")
    next_button = Button(NEXT_RECT,text="Next page") 
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
