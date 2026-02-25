import pygame


from utility.components import NavBar,QuestionBox,Options
from utility.blueprints import Button,TextBox


from data.constants import REMARK_BOX_RECT, WINDOW_HEIGHT,WINDOW_WIDTH
from data.constants import IDLE,SELECTED
from data.constants import PRIMARY_TEXT_COLOR

## Fonts ~
from data.constants import front_button_font,popup_button_font,title_font,difficulty_font
from data.constants import end_score_font,nav_button_font,question_box_font
 

## Front page --- 
from data.constants import FRONT_POPUP_COLOR,FRONT_BG_COLOR,FRONT_OVERLAY_BG_COLOR,TITLE_BOX_COLOR
from data.constants import FRONT_POPUP_RECT,TITLE_BOX_RECT,MODE_BOX_RECT,PLAY_BUTTON_RECT,DIFFICULTY_BUTTON_RECT
from data.constants import EASY_BUTTON_RECT,MEDIUM_BUTTON_RECT,HARD_BUTTON_RECT



## End page --------
from data.constants import  END_EXIT_BUTTON_RECT,RETURN_BUTTON_RECT, SCORE_BOX_RECT, EXIT_BUTTON_RECT 
from data.constants import END_BG_COLOR,QUIZ_BG_COLOR,FINAL_BOX_COLOR





class FrontPage:

    def __init__(self,screen):
    
        self.screen = screen

        self.popup_rect = FRONT_POPUP_RECT


        self.difficulty_text = 'Easy difficulty'
        self.popup = False


        
        ## TEXT BOXES --
        self.title_box = TextBox(screen,title_font,
                                 TITLE_BOX_RECT,
                                 TITLE_BOX_COLOR,PRIMARY_TEXT_COLOR)
        self.mode_box = TextBox(screen,difficulty_font,
                                MODE_BOX_RECT,
                                TITLE_BOX_COLOR,PRIMARY_TEXT_COLOR)


        ## BUTTONS --
        self.play_button = Button(PLAY_BUTTON_RECT,
                                  'Press play',
                                  front_button_font)
        self.difficulty_button = Button(DIFFICULTY_BUTTON_RECT,
                                        'Choose difficulty',
                                        front_button_font)

        ## popup difficulty buttons -> easy, medium,hard
        self.easy_button = Button(EASY_BUTTON_RECT,
                                  'Easy difficulty',
                                  popup_button_font)
        self.medium_button = Button(MEDIUM_BUTTON_RECT,
                                    'Medium difficulty',
                                    popup_button_font)
        self.hard_button = Button(HARD_BUTTON_RECT,
                                  'Hard difficulty',
                                  popup_button_font)

        self.exit_button = Button(EXIT_BUTTON_RECT,
                                  'Exit game',
                                  front_button_font)
        

        ### Overlay details
        self.overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.overlay.fill(FRONT_OVERLAY_BG_COLOR)   # adjust alpha if needed

        

    def update(self,mouse_pos,mouse_pressed):
        self.screen.fill(FRONT_BG_COLOR)   

        play_event = None
        difficulty_event = None
        exit_event = None

        if not self.popup:
            play_event = self.play_button.update(mouse_pos, mouse_pressed)
            difficulty_event = self.difficulty_button.update(mouse_pos, mouse_pressed)
            exit_event = self.exit_button.update(mouse_pos,mouse_pressed)

            if difficulty_event == 'CLICK':
                self.popup = True
            if exit_event == 'CLICK':
                return 'EXIT',""

        self.play_button.draw(self.screen)
        self.difficulty_button.draw(self.screen)
        self.exit_button.draw(self.screen)


        ## Need a textbox that centers the title automatically
        self.title_box.draw_textbox('V-shesh: Quiz on disability',border_radius=10)
        self.mode_box.draw_textbox(f'Mode: {self.difficulty_text}',border_radius=10)
        
        


        
            
        if self.popup:
            
            self.screen.blit(self.overlay,(0,0))


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


            if mouse_pressed and not self.popup_rect.collidepoint(mouse_pos):
                self.popup = False

            pygame.draw.rect(self.screen,FRONT_POPUP_COLOR,self.popup_rect,border_radius=12)
            self.easy_button.draw(self.screen)
            self.medium_button.draw(self.screen)
            self.hard_button.draw(self.screen)


            return None, self.difficulty_text
            


        return play_event,self.difficulty_text








class QuizPage:
    def __init__(self, screen, font, questions, difficulty_text):
        self.screen = screen
        self.font = font
        self.questions = questions
        self.difficulty_text = difficulty_text

        # MOVE your QUESTION PAGE DETAILS variables here
        self.navbar = NavBar(screen, nav_button_font)
        self.options = Options(screen)
        self.question_box = QuestionBox(screen, question_box_font)

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


        hint_event = self.navbar.draw_hint_button(mouse_pos,mouse_pressed)
        self.hint_open = self.navbar.hint_box_popup(hint_event,self.hint_open,self.random_questions[self.qno]['hint'])

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
        self.bg_color = END_BG_COLOR

        self.score_box = TextBox(self.screen,difficulty_font,
                                 SCORE_BOX_RECT,FINAL_BOX_COLOR,
                                 PRIMARY_TEXT_COLOR)
        
        self.remark_box = TextBox(self.screen,end_score_font,
                                  REMARK_BOX_RECT,
                                  FINAL_BOX_COLOR,
                                  PRIMARY_TEXT_COLOR)
        
        self.return_button = Button(RETURN_BUTTON_RECT,'Return to main menu',end_score_font)
        self.exit_button = Button(END_EXIT_BUTTON_RECT,'Exit game',end_score_font)

    def draw(self, screen, total_score, total_pages, difficulty_text):
        screen.fill(self.bg_color)

        self.score_box.draw_textbox(
            f"You have scored {total_score}/{total_pages}"
        )


        remark = self.get_remark(total_score,total_pages,difficulty_text)
        
        self.remark_box.draw_textbox(remark)
        self.return_button.draw(screen)
        self.exit_button.draw(screen)





    def get_remark(self, score, total_questions, difficulty):
        percentage = score / total_questions

        # --- Tier 1 ---
        if percentage <= 0.40:
            base_remark = (
                "This topic has many important nuances. "
                "Revisiting key concepts can help deepen your understanding."
            )

        # --- Tier 2 ---
        elif percentage <= 0.75:
            base_remark = (
                "You show a solid understanding of disability awareness principles. "
                "Reviewing missed areas can further strengthen your perspective."
            )

        # --- Tier 3 ---
        else:
            base_remark = (
                "Excellent understanding! You demonstrate thoughtful awareness "
                "and strong consideration of inclusive practices."
            )

        # --- Difficulty Adjustment ---
        if difficulty.lower() == "hard":
            difficulty_note = " Completing the challenging level makes this especially commendable."
        elif difficulty.lower() == "medium":
            difficulty_note = " You handled a moderate level of challenge well."
        else:
            difficulty_note = " This is a good foundation to continue building upon."

        return base_remark + difficulty_note

    def update(self, mouse_pos, mouse_pressed):
        return_event = self.return_button.update(mouse_pos, mouse_pressed)
        exit_event = self.exit_button.update(mouse_pos, mouse_pressed)

        if return_event == "CLICK":
            return "GO_TO_FRONT"
        if exit_event == 'CLICK':
            return "EXIT GAME"

        return None


