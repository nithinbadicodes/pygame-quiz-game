import pygame

### ==================== DO NOT MODIFY ============================

pygame.init()
pygame.font.init()



### WINDOW DIMENSIONS
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700


### FONTS
font = pygame.font.SysFont('segoe ui',20)

title_font      = pygame.font.SysFont('segoe ui', 36)
button_font     = pygame.font.SysFont('segoe ui', 17)
option_button_font     = pygame.font.SysFont('segoe ui', 16)
front_button_font     = pygame.font.SysFont('segoe ui', 22)
popup_button_font     = pygame.font.SysFont('segoe ui', 18)
nav_button_font     = pygame.font.SysFont('segoe ui', 18)
difficulty_font = pygame.font.SysFont('segoe ui', 30)
question_box_font = pygame.font.SysFont('segoe ui', 26)
end_score_font = pygame.font.SysFont('segoe ui',22)
default_font   = pygame.font.SysFont('segoe ui', 20)


#### FIX --> ONE VARIABLES FOR DIFFERENT STATES 
# STATES OF BUTTON
IDLE = "idle"
HOVERED = "hovered"
PRESSED = "pressed"
DISABLED = "disabled"
SELECTED = "selected"



### ===================== COLOR SYSTEM =====================

# -------- Foundation (Backgrounds) --------
FRONT_BG_COLOR = (10, 18, 38)      # front page
QUIZ_BG_COLOR  = (15, 20, 45)      # quiz page (slightly deeper)
END_BG_COLOR = (10, 18, 38)       # end page


# -------- Surface Panels (Non-Interactive UI) --------
SURFACE_DARK_COLOR  = (18, 28, 60)   # title boxes / deeper panels
SURFACE_COLOR       = (28, 40, 85)   # question box
SURFACE_LIGHT_COLOR = (35, 50, 95)   # popup panels / elevated surfaces

TITLE_BOX_COLOR    = SURFACE_DARK_COLOR
QUESTION_BOX_COLOR = SURFACE_COLOR
QUIZ_POPUP_COLOR   = SURFACE_LIGHT_COLOR
FINAL_BOX_COLOR    = SURFACE_COLOR
FRONT_POPUP_COLOR       = (25, 40, 80)



# -------- Accent (Interactive Elements Only) --------
BASE_COLOR     = (255, 145, 40)   # idle button
HOVER_COLOR    = (255, 170, 70)    # hovered button
PRESSED_COLOR  = (220, 115, 20)     
SELECTED_COLOR = (255, 200, 120)    # selected button


# -------- Overlays --------
FRONT_OVERLAY_BG_COLOR      = (20, 30, 65, 140)   # subtle front tint
QUIZ_POPUP_OVERLAY_COLOR    = (5, 10, 25, 180)    # darker modal overlay


# -------- Text Colors --------
TEXT_COLOR = (180, 145, 170)        # default dummy text color
PRIMARY_TEXT_COLOR   = (235, 240, 255)   # titles, question text
SECONDARY_TEXT_COLOR = (190, 200, 230)   # softer labels
BUTTON_TEXT_COLOR    = (25, 25, 35)      # text on orange buttons


# -------- Utility --------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

### ========================================================



## -------------------- FRONT PAGE ------------------------

### CHANGES -----------
# --- POPUP POSITION (overlay style) ---


FRONT_PAGE_OFFSET = 50


FRONT_DIFFICULTY_TOP = (WINDOW_HEIGHT // 2) + 20
POPUP_DIFFICULTY_TOP = FRONT_DIFFICULTY_TOP - 10


## POPUP WIDTH AND HEIGHT
POPUP_DIFFICULTY_WIDTH = 400
POPUP_DIFFICULTY_HEIGHT = 150

## POPUP INNER DIMENSIONS
POPUP_RECT_PADDING = 20
POPUP_COL_GAP = 15

usable_width_popup_rect = POPUP_DIFFICULTY_WIDTH - 2 * POPUP_RECT_PADDING


## POPUP BUTTON WIDTH AND HEIGHT
POPUP_DIFFICULTY_BUTTON_WIDTH = (usable_width_popup_rect - 2 * POPUP_COL_GAP) // 3
POPUP_DIFFICULTY_BUTTON_HEIGHT = 80


POPUP_LEFT = FRONT_PAGE_OFFSET  # matches difficulty button x


FRONT_POPUP_RECT = pygame.Rect(
    POPUP_LEFT,
    POPUP_DIFFICULTY_TOP,
    POPUP_DIFFICULTY_WIDTH,
    POPUP_DIFFICULTY_HEIGHT
)




POPUP_DIFFICULTY_BUTTON_TOP = (
    POPUP_DIFFICULTY_TOP
    + (POPUP_DIFFICULTY_HEIGHT - POPUP_DIFFICULTY_BUTTON_HEIGHT) // 2
)


## DIFFICULTY BUTTON POSITIONS
EASY_BUTTON_X = POPUP_LEFT + POPUP_RECT_PADDING
MEDIUM_BUTTON_X = EASY_BUTTON_X + POPUP_DIFFICULTY_BUTTON_WIDTH + POPUP_COL_GAP
HARD_BUTTON_X = MEDIUM_BUTTON_X + POPUP_DIFFICULTY_BUTTON_WIDTH + POPUP_COL_GAP


# POPUP/Button rects
FRONT_POPUP_RECT = pygame.Rect(FRONT_PAGE_OFFSET, FRONT_DIFFICULTY_TOP, 
                               POPUP_DIFFICULTY_WIDTH, 
                               POPUP_DIFFICULTY_HEIGHT)

EASY_BUTTON_RECT = pygame.Rect(EASY_BUTTON_X,
                               POPUP_DIFFICULTY_BUTTON_TOP,
                               POPUP_DIFFICULTY_BUTTON_WIDTH,
                               POPUP_DIFFICULTY_BUTTON_HEIGHT)
MEDIUM_BUTTON_RECT = pygame.Rect(MEDIUM_BUTTON_X,
                                 POPUP_DIFFICULTY_BUTTON_TOP,
                                 POPUP_DIFFICULTY_BUTTON_WIDTH,
                                 POPUP_DIFFICULTY_BUTTON_HEIGHT)
HARD_BUTTON_RECT = pygame.Rect(HARD_BUTTON_X,
                               POPUP_DIFFICULTY_BUTTON_TOP,
                               POPUP_DIFFICULTY_BUTTON_WIDTH,
                               POPUP_DIFFICULTY_BUTTON_HEIGHT)




### NON POPUP RECTS
PLAY_BUTTON_RECT = pygame.Rect(FRONT_PAGE_OFFSET,WINDOW_HEIGHT//2 - 50,400,50)
DIFFICULTY_BUTTON_RECT = pygame.Rect(FRONT_PAGE_OFFSET,FRONT_DIFFICULTY_TOP,400,50)
EXIT_BUTTON_RECT = pygame.Rect(FRONT_PAGE_OFFSET,FRONT_DIFFICULTY_TOP + 100,400,50)


## TEXT BOX INFORMATION
FRONT_TEXT_BOX_OFFEST = 20
## Text box rects
TITLE_BOX_RECT = pygame.Rect(FRONT_TEXT_BOX_OFFEST,160,
                             WINDOW_WIDTH-2*FRONT_TEXT_BOX_OFFEST,100)
MODE_BOX_RECT = pygame.Rect(FRONT_TEXT_BOX_OFFEST,WINDOW_HEIGHT - 150,
                            WINDOW_WIDTH-2*FRONT_TEXT_BOX_OFFEST,80)




### ------------------------ QUIZ PAGE ----------------------


## QUIZ MARGINS
QUIZ_LEFT_MARGIN = 20
QUIZ_TOP_MARGIN = 40

### CONTAINER DIMENSIONS
CONTAINER_WIDTH = WINDOW_WIDTH - 2*QUIZ_LEFT_MARGIN
CONTAINER_HEIGHT = WINDOW_HEIGHT - 2*QUIZ_TOP_MARGIN
CONTAINER_SPACING = 25

## NAVBAR DIMENSIONS
NAV_BUTTON_WIDTH = 110
NAV_BAR_HEIGHT = 50
NAV_BAR_SPACING = 30


### NAVBAR RECTS
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

END_PAGE_OFFSET = 30

## Rects
SCORE_BOX_RECT = pygame.Rect(END_PAGE_OFFSET,WINDOW_HEIGHT//2 - 200,
                             WINDOW_WIDTH-2*END_PAGE_OFFSET,50)
# DIFFICULTY_BOX_RECT = pygame.Rect(END_PAGE_OFFSET,WINDOW_HEIGHT//2 - 100,
#                                   WINDOW_WIDTH-2*END_PAGE_OFFSET,120)
REMARK_BOX_RECT = pygame.Rect(END_PAGE_OFFSET,WINDOW_HEIGHT//2 - 120,
                                  WINDOW_WIDTH-2*END_PAGE_OFFSET,160)

RETURN_BUTTON_RECT = pygame.Rect(END_PAGE_OFFSET,WINDOW_HEIGHT//2 + 100,
                                 WINDOW_WIDTH-2*END_PAGE_OFFSET,50)

END_EXIT_BUTTON_RECT = pygame.Rect(END_PAGE_OFFSET,WINDOW_HEIGHT//2 + 175,
                                   WINDOW_WIDTH-2*END_PAGE_OFFSET,50)




