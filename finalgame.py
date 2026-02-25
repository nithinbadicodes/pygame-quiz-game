import pygame
import sys

from data.constants import IDLE
from data.constants import WINDOW_WIDTH,WINDOW_HEIGHT
from utility.generate import QuestionGenerator
from utility.layout import EndPage, QuizPage,FrontPage



pygame.init()
pygame.font.init()

WIDTH,HEIGHT = WINDOW_WIDTH,WINDOW_HEIGHT

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Final game')
font = pygame.font.SysFont('arial',20)
clock = pygame.time.Clock()



#### FRONT PAGE DETAILS -----------
first_page = FrontPage(screen)



TOTAL_PAGES = 8

## scores tally
TOTAL_SCORE = 0
score_increment = [0 for _ in range(TOTAL_PAGES)]



### Question generator from generate.py file
Q_generator = QuestionGenerator(total=TOTAL_PAGES)

## answers selected
answers_selected = [[IDLE]*4 for _ in range(TOTAL_PAGES)]




endpage = EndPage(screen)


### PAGE SWITCH DETAILS -----
FRONT_PAGE = "FRONT PAGE"
QUIZ_PAGE = "QUIZ PAGE"
FINAL_PAGE = "FINAL PAGE"

current_page = FRONT_PAGE
### PAGE SWITCH DETAILS -----


running = True


while running:


    
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pressed = True
    
    
    ### FRONT PAGE CODE
    if current_page == FRONT_PAGE:

        play_event, difficulty_text = first_page.update(mouse_pos, mouse_pressed)

        if play_event == "CLICK":
            random_questions = Q_generator.generate()[difficulty_text]
            quiz = QuizPage(screen, font, random_questions, difficulty_text)
            current_page = QUIZ_PAGE
        if play_event == 'EXIT':
            running = False
            break

    ### QUIZ PAGE CODE
    elif current_page == QUIZ_PAGE:

        quiz.update(mouse_pos, mouse_pressed)

        if quiz.finished:
            TOTAL_SCORE = quiz.total_score
            current_page = FINAL_PAGE

    ### FINAL PAGE CODE
    elif current_page == FINAL_PAGE:

        endpage.draw(screen, TOTAL_SCORE, TOTAL_PAGES, difficulty_text)

        action = endpage.update(mouse_pos, mouse_pressed)

        if action == "GO_TO_FRONT":
            current_page = FRONT_PAGE
            first_page.difficulty_text = 'Easy difficulty'
        if action == 'EXIT GAME':
            running = False
            break


    pygame.display.flip()
    clock.tick(60)

print(score_increment)
print(f'Total score is {TOTAL_SCORE}/{TOTAL_PAGES}')
pygame.quit()
sys.exit()
