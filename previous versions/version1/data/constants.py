import pygame



pygame.init()
pygame.font.init()

#### FIX --> ONE VARIABLES FOR DIFFERENT STATES 

# STATES OF BUTTON
IDLE = "idle"
HOVERED = "hovered"
PRESSED = "pressed"
DISABLED = "disabled"
SELECTED = "selected"





### COLORS

BLACK = (0,0,0),
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


BG_COLOR = (100,100,100)



## BUTTON COLORS
BASE_COLOR=(46, 56, 86)
HOVER_COLOR=(89, 94, 109)
PRESSED_COLOR=(70, 75, 95)
SELECTED_COLOR = (120,2,250)


TEXT_COLOR=(255, 255, 255)
HOVER_TEXT_COLOR = (30,40,50)


## FRONT AND END PAGE


## QUIZ PAGE
QUIZ_BG_COLOR = (120,5,200)





### DIMENSIONS
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700


### FONTS
font = pygame.font.SysFont('arial',20)
title_font = pygame.font.SysFont('arial',35)
button_font = pygame.font.SysFont('arial',25)
difficulty_font = pygame.font.SysFont('arial',30)





### RECTS

## -------------------- FRONT PAGE ------------------------

# Button rects
FRONT_POPUP_RECT = pygame.Rect(20, 120, 260, 360)
EASY_BUTTON_RECT = pygame.Rect(50,160,200,80)
MEDIUM_BUTTON_RECT = pygame.Rect(50,255,200,80)
HARD_BUTTON_RECT = pygame.Rect(50,355,200,80)

PLAY_BUTTON_RECT = pygame.Rect(50,WINDOW_HEIGHT//2 - 50,400,50)
DIFFICULTY_BUTTON_RECT = pygame.Rect(50,(WINDOW_HEIGHT//2) + 20,400,50)


## Text box rects
TITLE_BOX_RECT = pygame.Rect(50,WINDOW_HEIGHT//2 - 200,400,50)
MODE_BOX_RECT = pygame.Rect(50,WINDOW_HEIGHT - 150,WINDOW_WIDTH - 100,100)




### ------------------------ QUIZ PAGE ----------------------

QUIZ_LEFT_MARGIN = 20
QUIZ_TOP_MARGIN = 20


CONTAINER_WIDTH = WINDOW_WIDTH - 2*QUIZ_LEFT_MARGIN
CONTAINER_HEIGHT = WINDOW_HEIGHT - 2*QUIZ_TOP_MARGIN
CONTAINER_SPACING = 25


NAV_BUTTON_WIDTH = 100
NAV_BAR_HEIGHT = 50
NAV_BAR_SPACING = 30

PREV_RECT = pygame.Rect(QUIZ_LEFT_MARGIN,
                        QUIZ_TOP_MARGIN,
                        NAV_BUTTON_WIDTH,
                        NAV_BAR_HEIGHT)
NEXT_RECT = SUBMIT_RECT = pygame.Rect(WINDOW_WIDTH-(NAV_BUTTON_WIDTH+QUIZ_LEFT_MARGIN),
                        QUIZ_TOP_MARGIN,
                        NAV_BUTTON_WIDTH,
                        NAV_BAR_HEIGHT)

HINT_RECT = pygame.Rect(QUIZ_LEFT_MARGIN + 2*NAV_BUTTON_WIDTH + 2*NAV_BAR_SPACING,
                        QUIZ_TOP_MARGIN,
                        50,50)


# container_rect = pygame.Rect(10,10,WINDOW_WIDTH,100)
QNO_RECT = pygame.Rect(QUIZ_LEFT_MARGIN + NAV_BUTTON_WIDTH + NAV_BAR_SPACING,
                       QUIZ_TOP_MARGIN,
                       NAV_BUTTON_WIDTH,
                       NAV_BAR_HEIGHT)



QUESTION_TOP_MARGIN = QUIZ_TOP_MARGIN + NAV_BAR_HEIGHT + CONTAINER_SPACING
QUESTION_BOX_WIDTH = WINDOW_WIDTH - 2 * QUIZ_LEFT_MARGIN
QUESTION_BOX_HEIGHT = 300









QUIZ_POPUP_RECT = pygame.Rect(
            2*QUIZ_LEFT_MARGIN,
            QUESTION_TOP_MARGIN + 100,
            QUESTION_BOX_WIDTH - 2*QUIZ_LEFT_MARGIN,
            QUESTION_BOX_HEIGHT - 100 - QUIZ_LEFT_MARGIN
            )



COLUMN_GAP = 30
ROW_GAP = 30

# OPTIONS_TOP =  QUESTION_BOX_HEIGHT + NAV_BAR_HEIGHT  + 2* CONTAINER_SPACING
OPTIONS_TOP =  QUESTION_TOP_MARGIN + QUESTION_BOX_HEIGHT + CONTAINER_SPACING
AVAILABLE_HEIGHT = WINDOW_HEIGHT - OPTIONS_TOP  # remaining height for options area


# ---- CALCULATIONS ----

button_width = (CONTAINER_WIDTH - COLUMN_GAP) // 2
button_height = (AVAILABLE_HEIGHT - ROW_GAP - QUIZ_TOP_MARGIN) // 2

left_x = QUIZ_LEFT_MARGIN
right_x = QUIZ_LEFT_MARGIN + button_width + COLUMN_GAP

top_y = OPTIONS_TOP
bottom_y = OPTIONS_TOP + button_height + ROW_GAP


# ---- OPTION BUTTON RECTS ----

OPTIONS_RECTS = [
    # Top Left
    pygame.Rect(left_x, top_y,
                button_width, button_height),

    # Top Right
    pygame.Rect(right_x, top_y,
                button_width, button_height),

    # Bottom Left
    pygame.Rect(left_x, bottom_y,
                button_width, button_height),

    # Bottom Right
    pygame.Rect(right_x, bottom_y,
                button_width, button_height),
]












### -----------------------  FINAL PAGE ---------------------


## Rects
SCORE_BOX_RECT = pygame.Rect(50,WINDOW_HEIGHT//2 - 200,400,50)
DIFFICULTY_BOX_RECT = pygame.Rect(50,WINDOW_HEIGHT//2 - 100,400,120)

RETURN_BUTTON_RECT = pygame.Rect(50,WINDOW_HEIGHT//2 + 200,400,50)
