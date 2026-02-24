import pygame


from utility.components import NavBar,QuestionBox,Options
from utility.blueprints import Button,TextBox


from data.constants import DIFFICULTY_BOX_RECT, FRONT_POPUP_RECT, RETURN_BUTTON_RECT, SCORE_BOX_RECT, WINDOW_HEIGHT,WINDOW_WIDTH
from data.constants import font,title_font,difficulty_font,button_font

from data.constants import EASY_BUTTON_RECT,MEDIUM_BUTTON_RECT,HARD_BUTTON_RECT
from data.constants import TITLE_BOX_RECT,MODE_BOX_RECT,PLAY_BUTTON_RECT,DIFFICULTY_BUTTON_RECT

from data.constants import IDLE,SELECTED
from data.constants import BG_COLOR,QUIZ_BG_COLOR,BLACK,WHITE




##  draw_title
##  difficulty popup
##  draw_mode_text
class FrontPage:

    def __init__(self,screen):
    
        self.screen = screen

        self.popup_rect = FRONT_POPUP_RECT


        self.difficulty_text = 'Easy difficulty'
        self.popup = False



        ## difficulty buttons -> easy, medium,hard
        self.easy_button = Button(EASY_BUTTON_RECT,'Easy difficulty',button_font)
        self.medium_button = Button(MEDIUM_BUTTON_RECT,'Medium difficulty',button_font)
        self.hard_button = Button(HARD_BUTTON_RECT,'Hard difficulty',button_font)



        
        ## TEXT BOXES --
        self.title_box = TextBox(screen,title_font,
                                 TITLE_BOX_RECT,
                                 BLACK,WHITE)
        self.mode_box = TextBox(screen,difficulty_font,
                                MODE_BOX_RECT,
                                BLACK,WHITE)

        # sample_button = Button(pygame.Rect(WIDTH//2,HEIGHT//2,100,50),'Click me',button_font)
        self.play_button = Button(PLAY_BUTTON_RECT,
                                  'Press play',button_font)
        self.difficulty_button = Button(DIFFICULTY_BUTTON_RECT,
                                        'Choose difficulty',button_font)
        

    def update(self,mouse_pos,mouse_pressed):
        self.screen.fill(BG_COLOR)   

        play_event = self.play_button.update(mouse_pos, mouse_pressed)
        difficulty_event = self.difficulty_button.update(mouse_pos, mouse_pressed)
        if not self.popup:
            
            if difficulty_event == 'CLICK':
                self.popup = True
        else:
            play_event = None

        self.play_button.draw(self.screen)
        self.difficulty_button.draw(self.screen)
        ## Need a textbox that centers the title automatically
        self.title_box.draw_textbox('This is the title')
        self.mode_box.draw_textbox(f'Mode: {self.difficulty_text}')
        


        
            
        if self.popup:

            easy_event = self.easy_button.update(mouse_pos, mouse_pressed)
            medium_event = self.medium_button.update(mouse_pos, mouse_pressed)
            hard_event = self.hard_button.update(mouse_pos, mouse_pressed)

            if easy_event == 'CLICK':
                self.difficulty_text = self.easy_button.text
                self.popup=False
            if medium_event == 'CLICK':
                self.difficulty_text = self.medium_button.text
                self.popup=False
            if hard_event == 'CLICK':
                self.difficulty_text = self.hard_button.text
                self.popup=False


            pygame.draw.rect(self.screen,BG_COLOR,self.popup_rect)
            self.easy_button.draw(self.screen)
            self.medium_button.draw(self.screen)
            self.hard_button.draw(self.screen)
            


        return play_event,self.difficulty_text








class QuizPage:
    def __init__(self, screen, font, questions, difficulty_text):
        self.screen = screen
        self.font = font
        self.questions = questions
        self.difficulty_text = difficulty_text

        # MOVE your QUESTION PAGE DETAILS variables here
        self.navbar = NavBar(screen, font)
        self.options = Options(screen)
        self.question_box = QuestionBox(screen, font)

        self.q_page = "FRONT"
        self.qno = 0
        self.hint_open = False
        self.random_questions = questions

        self.TOTAL_PAGES = len(self.random_questions)
        self.score_increment = [0] * self.TOTAL_PAGES
        self.answers_selected = [[IDLE] * 4 for _ in range(self.TOTAL_PAGES)]
        self.total_score = 0
        self.finished = False


    def update(self,mouse_pos,mouse_pressed):
        self.screen.fill(QUIZ_BG_COLOR)
        self.q_page,self.qno,nav_event = self.navbar.prev_next_final_display(mouse_pos,
                                                                    mouse_pressed,
                                                                    self.q_page,
                                                                    self.qno,
                                                                    self.TOTAL_PAGES)
        
        

        self.question_box.draw_question_box(self.random_questions[self.qno]['question'])
        hint_event = self.navbar.draw_hint_button(mouse_pos,mouse_pressed)
        self.hint_open = self.navbar.hint_box_popup(hint_event,self.hint_open,self.random_questions[self.qno]['hint'])


        ## question number box display in nav bar
        self.navbar.qnobox_display(self.qno)


        # If question changed → rebuild buttons
        if nav_event in ("NEXT", "PREV"):
            self.options.reset_buttons()
            self.hint_open = False

        
        # ---------------- OPTIONS ----------------
        selected_index = self.options.draw(
            self.random_questions[self.qno]["options"],
            mouse_pos,
            mouse_pressed,
            self.answers_selected[self.qno]
        )

        # ---------------- HANDLE SELECTION ----------------
        if selected_index is not None:
            self.answers_selected[self.qno] = [IDLE, IDLE, IDLE, IDLE]
            self.answers_selected[self.qno][selected_index] = SELECTED
            if self.options.buttons[selected_index].text == self.random_questions[self.qno]["answer"]:
                self.score_increment[self.qno] = 1
            else:
                self.score_increment[self.qno] = 0
            print(self.score_increment)
        if nav_event == "SUBMIT":
            self.total_score = sum(self.score_increment)
            self.finished = True




class EndPage:
    def __init__(self,screen):
        self.screen = screen
        self.score_box = TextBox(screen,title_font,SCORE_BOX_RECT,WHITE,BLACK)
        self.difficulty_box = TextBox(screen,difficulty_font,DIFFICULTY_BOX_RECT,WHITE,BLACK)

        self.return_button = Button(RETURN_BUTTON_RECT,'Return to main menu',button_font)


    def update(self,mouse_pos,mouse_pressed):
        pass




# ### TO DO
# class Layout:
#     def __init__(self,screen,font,bg_color,text_color):
#         self.screen = screen
#         self.font = font
#         self.bg_color = bg_color
#         self.text_color = text_color
#         self.question_box = TextBox(self.screen,
#                                     self.font,
#                                     pygame.Rect(20,120,self.screen.get_width()-40,300),
#                                     bg_color=self.bg_color,
#                                     text_color=self.text_color)
#         # self.option_boxes = Options()



#     def draw_questionbox(self,text):
#         self.question_box.draw_textbox(text)

