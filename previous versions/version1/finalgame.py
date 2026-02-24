import pygame
import sys
import random
from data.constants import IDLE,SELECTED,BG_COLOR
from data.constants import WINDOW_WIDTH,WINDOW_HEIGHT
from utility.blueprints import  Button,TextBox
from utility.generate import QuestionGenerator
from utility.components import NavBar,Options,QuestionBox
from data.questions import easy_questions,medium_questions,hard_questions
from utility.layout import QuizPage,FrontPage






pygame.init()
pygame.font.init()

WIDTH,HEIGHT = WINDOW_WIDTH,WINDOW_HEIGHT

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Four page memory')
font = pygame.font.SysFont('arial',20)
clock = pygame.time.Clock()



## COLORS
# BG_COLOR = (0,200,255)
WHITE = (255,255,255)
BLACK = (0,0,0)


# print(len(easy_questions))
# print(len(medium_questions))
# print(len(hard_questions))


#### FRONT PAGE DETAILS -----------

title_font = pygame.font.SysFont('arial',35)
button_font = pygame.font.SysFont('arial',25)
difficulty_font = pygame.font.SysFont('arial',30)

## TEXT BOXES --
title_box = TextBox(screen,title_font,pygame.Rect(50,HEIGHT//2 - 200,400,50),BLACK,WHITE)
mode_box = TextBox(screen,difficulty_font,pygame.Rect(50,HEIGHT - 150,WIDTH - 100,100),BLACK,WHITE)

# sample_button = Button(pygame.Rect(WIDTH//2,HEIGHT//2,100,50),'Click me',button_font)
play_button = Button(pygame.Rect(50,HEIGHT//2 - 50,400,50),'Press play',button_font)
difficulty_button = Button(pygame.Rect(50,(HEIGHT//2) + 20,400,50),'Choose difficulty',button_font)



### Difficulty popup details


## difficulty buttons -> easy, medium,hard
easy_button = Button(pygame.Rect(50,160,200,80),'Easy difficulty',button_font)
medium_button = Button(pygame.Rect(50,255,200,80),'Medium difficulty',button_font)
hard_button = Button(pygame.Rect(50,355,200,80),'Hard difficulty',button_font)

difficulty_text = 'Easy difficulty'
popup = False


first_page = FrontPage(screen)

#### FRONT PAGE DETAILS -----------





### END PAGE DETAILS  ---------

score_box = TextBox(screen,title_font,pygame.Rect(50,HEIGHT//2 - 200,400,50),WHITE,BLACK)
difficulty_box = TextBox(screen,difficulty_font,pygame.Rect(50,HEIGHT//2 - 100,400,120),WHITE,BLACK)

return_button = Button(pygame.Rect(50,HEIGHT//2 + 200,400,50),'Return to main menu',button_font)

### END PAGE DETAILS --------








### QUESTION PAGE DETAILS -------




### LAYOUT DETAILS
# navbar = NavBar(screen,font)

# options = Options(screen)


## PREV NEXT INITIALS

TOTAL_PAGES = 8

# question_box = QuestionBox(screen,font,navbar.container_rect.bottom + 20)
questions = easy_questions


#### QUESTION PAGE DETAILS --------
q_page = 'FRONT'
qno = 0

## scores tally
TOTAL_SCORE = 0
score_increment = [0 for _ in range(TOTAL_PAGES)]




Q_generator = QuestionGenerator(total=TOTAL_PAGES)
## answers selected
answers_selected = [[IDLE]*4 for _ in range(TOTAL_PAGES)]



### PAGE SWITCH DETAILS -----
FRONT_PAGE = "FRONT PAGE"
QUESTION_PAGE = "QUESTION PAGE"
FINAL_PAGE = "FINAL PAGE"

current_page = FRONT_PAGE
### PAGE SWITCH DETAILS -----


running = True


while running:


    screen.fill(BLACK)
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    
    
    
    ### button events
    play_event = play_button.update(mouse_pos,mouse_pressed)
    difficulty_event = difficulty_button.update(mouse_pos,mouse_pressed)



    return_event = return_button.update(mouse_pos,mouse_pressed)

    ### difficulty button events
    easy_event = easy_button.update(mouse_pos,mouse_pressed)
    medium_event = medium_button.update(mouse_pos,mouse_pressed)
    hard_event = hard_button.update(mouse_pos,mouse_pressed)


    
    
    

    if current_page == FRONT_PAGE:

        play_event, difficulty_text = first_page.update(mouse_pos, mouse_pressed)

        if play_event == "CLICK":
            random_questions = Q_generator.generate()[difficulty_text]
            quiz = QuizPage(screen, font, random_questions, difficulty_text)
            current_page = QUESTION_PAGE


    elif current_page == QUESTION_PAGE:

        quiz.update(mouse_pos, mouse_pressed)

        if quiz.finished:
            TOTAL_SCORE = quiz.total_score
            current_page = FINAL_PAGE


    elif current_page == FINAL_PAGE:

        screen.fill(BLACK)
        score_box.draw_textbox(f'You have scored {TOTAL_SCORE}/{TOTAL_PAGES}')
        difficulty_box.draw_textbox(f'You have selected {difficulty_text}')
        return_button.draw(screen)

        if return_event == 'CLICK':
            current_page = FRONT_PAGE
            difficulty_text = easy_button.text




    pygame.display.flip()
    clock.tick(60)

print(score_increment)
print(f'Total score is {TOTAL_SCORE}/{TOTAL_PAGES}')
pygame.quit()
sys.exit()
