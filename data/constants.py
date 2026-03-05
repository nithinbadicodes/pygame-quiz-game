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
nav_button_font     = pygame.font.SysFont('segoe ui', 22)
difficulty_font = pygame.font.SysFont('segoe ui', 30)
instruction_font = pygame.font.SysFont('segoe ui', 19)
question_box_font = pygame.font.SysFont('segoe ui', 26)
end_page_font = pygame.font.SysFont('segoe ui',22)
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

TITLE_BOX_COLOR    = SURFACE_DARK_COLOR     # Title box color (Start page)
QUESTION_BOX_COLOR = SURFACE_COLOR          # Question box color (Quiz page)
QUIZ_POPUP_COLOR   = SURFACE_LIGHT_COLOR    # Hint box popup color (Quiz page)
FINAL_BOX_COLOR    = SURFACE_COLOR          # Remark box (End page)
FRONT_POPUP_COLOR       = (25, 40, 80)



# -------- Accent (Interactive Elements Only) --------
BASE_COLOR     = (255, 145, 40)   # idle button
HOVER_COLOR    = (255, 170, 70)    # hovered button
PRESSED_COLOR  = (220, 115, 20)     
SELECTED_COLOR = (255, 200, 120)    # selected button

# -------- Option colors --------
CORRECT_COLOR = (40,215,80)
WRONG_COLOR = (215,40,80)

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

FRONT_PAGE_OFFSET = 50
HINT_SIZE = 50

FRONT_DIFFICULTY_TOP = (WINDOW_HEIGHT // 2) + 20




### NON POPUP RECTS
FRONT_BUTTON_WIDTH = 400
FRONT_BUTTON_HEIGHT = 50
FRONT_PAGE_ROW_GAP = 20

PLAY_BUTTON_TOP = WINDOW_HEIGHT//2 - 50

PLAY_BUTTON_RECT = pygame.Rect(FRONT_PAGE_OFFSET,
                               PLAY_BUTTON_TOP,
                               FRONT_BUTTON_WIDTH,
                               FRONT_BUTTON_HEIGHT)


# ----Difficulty button above instruction button---
# DIFFICULTY_BUTTON_RECT = pygame.Rect(FRONT_PAGE_OFFSET,FRONT_DIFFICULTY_TOP,400,50)

# ----Exit button on front page removed---------
# EXIT_BUTTON_RECT = pygame.Rect(FRONT_PAGE_OFFSET,FRONT_DIFFICULTY_TOP + 85,400,50)


## TEXT BOX INFORMATION
FRONT_TEXT_BOX_OFFSET = 20
FRONT_TEXT_BOX_TOP = 160
TEXT_BOX_WIDTH = WINDOW_WIDTH-2*FRONT_TEXT_BOX_OFFSET
## Text box rects
TITLE_BOX_RECT = pygame.Rect(FRONT_TEXT_BOX_OFFSET,FRONT_TEXT_BOX_TOP,
                             TEXT_BOX_WIDTH,100)
MODE_BOX_RECT = pygame.Rect(FRONT_TEXT_BOX_OFFSET,WINDOW_HEIGHT - 150,
                            TEXT_BOX_WIDTH,80)

## ========== INSTRUCTION BUTTON RECT ===========
INSTRUCTION_BUTTON_TOP = PLAY_BUTTON_TOP + FRONT_BUTTON_HEIGHT + FRONT_PAGE_ROW_GAP


INSTRUCTION_BUTTON_RECT = pygame.Rect(FRONT_PAGE_OFFSET,
                                      INSTRUCTION_BUTTON_TOP,
                                      FRONT_BUTTON_WIDTH,
                                      FRONT_BUTTON_HEIGHT)



# ------------Prev position difficulty button above then instruction button---------
# INSTRUCTION_BUTTON_RECT = pygame.Rect(FRONT_PAGE_OFFSET,FRONT_DIFFICULTY_TOP + 85,400,50)


# -------Prev instruction button under difficulty text box------------
# INSTRUCTION_INNER_BUTTON_WIDTH = 240
# INSTRUCTION_INNER_BUTTON_HEIGHT = 40
# INSTRUCTION_BUTTON_RECT = pygame.Rect(INSTRUCTION_BUTTON_LEFT,
#                                       INSTRUCTION_BUTTON_TOP,
#                                       INSTRUCTION_BUTTON_WIDTH,
#                                       INSTRUCTION_BUTTON_HEIGHT)


## INSTRUCTION POPUP RECT DETAILS
INSTRUCTION_POPUP_WIDTH = TEXT_BOX_WIDTH
INSTRUCTION_POPUP_HEIGHT = WINDOW_HEIGHT - FRONT_TEXT_BOX_TOP - 150

INSTRUCTION_POPUP_RECT = pygame.Rect(FRONT_TEXT_BOX_OFFSET,
                                   FRONT_TEXT_BOX_TOP + 50,
                                   INSTRUCTION_POPUP_WIDTH,
                                   INSTRUCTION_POPUP_HEIGHT)

INSTRUCTION_POPUP_BOX_WIDTH = 130
INSTRUCTION_POPUP_BOX_HEIGHT = 50

INSTRUCTION_PREV_BUTTON_TOP = FRONT_TEXT_BOX_TOP + 120
INSTRUCTION_NEXT_BUTTON_TOP = INSTRUCTION_PREV_BUTTON_TOP + INSTRUCTION_POPUP_BOX_HEIGHT + 50
INSTRUCTION_HINT_BUTTON_TOP = INSTRUCTION_NEXT_BUTTON_TOP + INSTRUCTION_POPUP_BOX_HEIGHT + 50

INSTRUCTION_PREV_POPUP_TEXTBOX = pygame.Rect(FRONT_PAGE_OFFSET,
                                        INSTRUCTION_PREV_BUTTON_TOP,
                                        INSTRUCTION_POPUP_BOX_WIDTH,
                                        INSTRUCTION_POPUP_BOX_HEIGHT)

INSTRUCTION_NEXT_POPUP_TEXTBOX = pygame.Rect(FRONT_PAGE_OFFSET,
                                        INSTRUCTION_NEXT_BUTTON_TOP,
                                        INSTRUCTION_POPUP_BOX_WIDTH,
                                        INSTRUCTION_POPUP_BOX_HEIGHT)

INSTRUCTION_HINT_POPUP_TEXTBOX = pygame.Rect(FRONT_PAGE_OFFSET + 50,
                                        INSTRUCTION_HINT_BUTTON_TOP,
                                        HINT_SIZE,
                                        HINT_SIZE)


### Instructions to the right

INSTRUCTIONS_TEXT_LEFT = FRONT_PAGE_OFFSET + 140

INSTRUCTIONS_PREV_TEXT_TOP = INSTRUCTION_PREV_BUTTON_TOP
INSTRUCTIONS_NEXT_TEXT_TOP = INSTRUCTION_NEXT_BUTTON_TOP
INSTRUCTIONS_HINT_TEXT_TOP = INSTRUCTION_HINT_BUTTON_TOP

INSTRUCTIONS_TEXT_WIDTH = INSTRUCTION_POPUP_BOX_WIDTH + 150
INSTRUCTIONS_TEXT_HEIGHT = INSTRUCTION_POPUP_BOX_HEIGHT+25

INSTRUCTION_PREV_TEXTBOX = pygame.Rect(INSTRUCTIONS_TEXT_LEFT,
                                        INSTRUCTIONS_PREV_TEXT_TOP,
                                        INSTRUCTIONS_TEXT_WIDTH,
                                        INSTRUCTIONS_TEXT_HEIGHT)
INSTRUCTION_NEXT_TEXTBOX = pygame.Rect(INSTRUCTIONS_TEXT_LEFT,
                                        INSTRUCTIONS_NEXT_TEXT_TOP,
                                        INSTRUCTIONS_TEXT_WIDTH,
                                        INSTRUCTIONS_TEXT_HEIGHT)

INSTRUCTION_HINT_TEXTBOX = pygame.Rect(INSTRUCTIONS_TEXT_LEFT,
                                    INSTRUCTIONS_HINT_TEXT_TOP,
                                    INSTRUCTIONS_TEXT_WIDTH,
                                    INSTRUCTIONS_TEXT_HEIGHT)


## DIFFICULTY_BUTTON DETAILS
DIFFICULTY_BUTTON_TOP = INSTRUCTION_BUTTON_TOP + FRONT_BUTTON_HEIGHT + FRONT_PAGE_ROW_GAP


DIFFICULTY_BUTTON_RECT = pygame.Rect(FRONT_PAGE_OFFSET,
                                     DIFFICULTY_BUTTON_TOP,
                                     FRONT_BUTTON_WIDTH,
                                     FRONT_BUTTON_HEIGHT)


POPUP_DIFFICULTY_TOP = FRONT_DIFFICULTY_TOP - 10
POPUP_DIFFICULTY_TOP = PLAY_BUTTON_TOP


## POPUP WIDTH AND HEIGHT
POPUP_DIFFICULTY_WIDTH = 400
POPUP_DIFFICULTY_HEIGHT = 150

## POPUP INNER DIMENSIONS
POPUP_RECT_PADDING = 20
POPUP_COL_GAP = 20

usable_width_popup_rect = POPUP_DIFFICULTY_WIDTH - 2 * POPUP_RECT_PADDING


## POPUP BUTTON WIDTH AND HEIGHT
POPUP_DIFFICULTY_BUTTON_WIDTH = (usable_width_popup_rect - 2 * POPUP_COL_GAP) // 3
POPUP_DIFFICULTY_BUTTON_HEIGHT = 70


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
FRONT_POPUP_RECT = pygame.Rect(FRONT_PAGE_OFFSET, 
                               POPUP_DIFFICULTY_TOP, 
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










### ======================== QUIZ PAGE ===========================


## QUIZ MARGINS
QUIZ_LEFT_MARGIN = 20
QUIZ_TOP_MARGIN = 40



#### Container -> Quiz contents are present -----------

### CONTAINER DIMENSIONS
CONTAINER_WIDTH = WINDOW_WIDTH - 2*QUIZ_LEFT_MARGIN
CONTAINER_HEIGHT = WINDOW_HEIGHT - 2*QUIZ_TOP_MARGIN
CONTAINER_SPACING = 25

## NAVBAR DIMENSIONS
NAV_BUTTON_WIDTH = 110
NAV_BAR_HEIGHT = 50
NAV_BAR_SPACING = 30


### ================ NAVBAR RECTS ========================
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
                        HINT_SIZE,
                        HINT_SIZE)

QNO_RECT = pygame.Rect(QUIZ_LEFT_MARGIN + NAV_BUTTON_WIDTH + NAV_BAR_SPACING,
                       QUIZ_TOP_MARGIN,
                       NAV_BUTTON_WIDTH,
                       NAV_BAR_HEIGHT)




### QUESTION BOX DETAILS
QUESTION_TOP_MARGIN = QUIZ_TOP_MARGIN + NAV_BAR_HEIGHT + CONTAINER_SPACING
QUESTION_BOX_WIDTH = WINDOW_WIDTH - 2 * QUIZ_LEFT_MARGIN
QUESTION_BOX_HEIGHT = 300



### HINT POPUP RECT
QUIZ_POPUP_RECT = pygame.Rect(
            2*QUIZ_LEFT_MARGIN,
            QUESTION_TOP_MARGIN + 100,
            QUESTION_BOX_WIDTH - 2*QUIZ_LEFT_MARGIN,
            QUESTION_BOX_HEIGHT - 100 - QUIZ_LEFT_MARGIN
            )


### ======================OPTIONS DETAILS===================
COLUMN_GAP = 30
ROW_GAP = 30


OPTIONS_TOP =  QUESTION_TOP_MARGIN + QUESTION_BOX_HEIGHT + CONTAINER_SPACING
AVAILABLE_HEIGHT = WINDOW_HEIGHT - OPTIONS_TOP  # remaining height for options area


# ================CALCULATIONS=============

button_width = (CONTAINER_WIDTH - COLUMN_GAP) // 2
button_height = (AVAILABLE_HEIGHT - ROW_GAP - QUIZ_TOP_MARGIN) // 2

left_x = QUIZ_LEFT_MARGIN
right_x = QUIZ_LEFT_MARGIN + button_width + COLUMN_GAP

top_y = OPTIONS_TOP
bottom_y = OPTIONS_TOP + button_height + ROW_GAP


# =================OPTION BUTTON RECTS====================

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




### =======================  FINAL PAGE ==========================

END_PAGE_OFFSET = 30

## ==========Rects==========

# SCORE BOX "You have score x/8"
SCORE_BOX_RECT = pygame.Rect(END_PAGE_OFFSET,WINDOW_HEIGHT//2 - 200,
                             WINDOW_WIDTH-2*END_PAGE_OFFSET,50)

# Remark box -> Based on score and difficulty
REMARK_BOX_RECT = pygame.Rect(END_PAGE_OFFSET,WINDOW_HEIGHT//2 - 120,
                                  WINDOW_WIDTH-2*END_PAGE_OFFSET,160)

REVIEW_BUTTON_RECT = pygame.Rect(END_PAGE_OFFSET,WINDOW_HEIGHT//2 + 100,
                                 WINDOW_WIDTH-2*END_PAGE_OFFSET,50)

# Return to main menu button
RETURN_BUTTON_RECT = pygame.Rect(END_PAGE_OFFSET,WINDOW_HEIGHT//2 + 175,
                                 WINDOW_WIDTH-2*END_PAGE_OFFSET,50)


# Exit button -> Leave game
END_EXIT_BUTTON_RECT = pygame.Rect(END_PAGE_OFFSET,WINDOW_HEIGHT//2 + 250,
                                   WINDOW_WIDTH-2*END_PAGE_OFFSET,50)



###====================REVIEW PAGE================================


## SAME AS QUIZ PAGE -> FEW CHANGES

## Return rect
REVIEW_RETURN_BUTTON_RECT = pygame.Rect(WINDOW_WIDTH-(NAV_BUTTON_WIDTH+QUIZ_LEFT_MARGIN),
                        QUIZ_TOP_MARGIN,
                        NAV_BUTTON_WIDTH,
                        NAV_BAR_HEIGHT)
