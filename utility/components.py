import pygame

from utility.helper_functions import create_image, get_prev_next_buttons
from utility.blueprints import Button,TextBox


from data.constants import DISABLED, IDLE

# RECTS
from data.constants import OPTIONS_RECTS, QUIZ_POPUP_RECT, REVIEW_RETURN_BUTTON_RECT
from data.constants import QNO_RECT,SUBMIT_RECT,HINT_RECT

# COLORS
from data.constants import BASE_COLOR, BUTTON_TEXT_COLOR,CORRECT_COLOR, PRIMARY_TEXT_COLOR, QUESTION_BOX_COLOR, QUIZ_POPUP_COLOR, QUIZ_POPUP_OVERLAY_COLOR, WRONG_COLOR

# DIMENSIONS
from data.constants import WINDOW_HEIGHT,WINDOW_WIDTH,QUESTION_BOX_WIDTH,QUESTION_BOX_HEIGHT
from data.constants import QUIZ_LEFT_MARGIN,QUESTION_TOP_MARGIN

# FONTS
from data.constants import option_button_font



pygame.init()
pygame.font.init()



### Navbar and its functionality
class NavBar:
    def __init__(self,screen,font):
        
        self.font = font
        self.screen = screen
        self.hint_open=False


        self.popup_color = QUIZ_POPUP_COLOR
        self.text_color = BUTTON_TEXT_COLOR
        self.popup_text_color = PRIMARY_TEXT_COLOR

        ## Buttons
        # Prev and Next buttons
        self.prev_button,self.next_button = get_prev_next_buttons()
        # Submit button for Quiz page
        self.submit_button = Button(SUBMIT_RECT,text="Submit",font = font)
        # Return button for Review page
        self.return_button = Button(REVIEW_RETURN_BUTTON_RECT,text="Return",font = font)
        # Hint button
        self.hint_button = Button(HINT_RECT,text="",font=font,border_radius=50)


        ## Rects
        self.container_rect = pygame.Rect(10,10,self.screen.get_width(),100)
        self.question_rect = QNO_RECT
         
        self.popup_rect = QUIZ_POPUP_RECT

        # Icons path 
        cross_icon1,cross_icon2 = 'assets/icons/black_cross.png','assets/icons/black_circle_white_cross.png'
        bulb_icon = 'assets/icons/black_bulb.png'

        # Hint icon details
        self.hint_bulb_image,self.hint_bulb_image_rect = create_image(bulb_icon,
                                                       self.hint_button.rect.centerx,
                                                       self.hint_button.rect.centery,
                                                       self.hint_button.rect.width-15,
                                                        self.hint_button.rect.height - 15)
        self.hint_cross_image,self.hint_cross_image_rect = create_image(cross_icon1,
                                                       self.hint_button.rect.centerx,
                                                       self.hint_button.rect.centery,
                                                       self.hint_button.rect.width-15,
                                                        self.hint_button.rect.height - 15)
        
        
        self.popup_textbox = TextBox(self.screen,
                                     self.font,
                                     self.popup_rect,
                                     self.popup_color,
                                     self.popup_text_color)
        ### Overlay details
        self.overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.overlay.fill(QUIZ_POPUP_OVERLAY_COLOR)



        
    def prev_next_display(self, mouse_pos, mouse_pressed, page,review):

        if page != "FRONT":
            prev_event = self.prev_button.update(mouse_pos, mouse_pressed)
            self.prev_button.draw(self.screen)
        else:
            prev_event = None

        if page == "SUBMIT":
            nav_event = self.submit_button.update(mouse_pos, mouse_pressed)
            self.submit_button.draw(self.screen)
        elif page == 'RETURN':
            nav_event = self.return_button.update(mouse_pos,mouse_pressed)
            self.return_button.draw(self.screen)
        else:
            
            nav_event = self.next_button.update(mouse_pos, mouse_pressed)
            self.next_button.draw(self.screen)

        

        if nav_event == "CLICK":
            if review:
                return 'RETURN' if page == 'RETURN' else 'NEXT'
            return "SUBMIT" if page == "SUBMIT" else "NEXT"

        if prev_event == "CLICK":
            return "PREV"

        return None


    ### Prev and next button functionality
    def prev_next_final_display(self,mouse_pos,mouse_pressed,page,qno,TOTAL_PAGES,review_page=False):
        nav_event = self.prev_next_display(mouse_pos,mouse_pressed,page,review=review_page)
    



        if nav_event == "NEXT":
            qno += 1
            
            self.close_hint()
        elif nav_event == "PREV":
            qno -= 1
            
            self.close_hint()

        # Clamp qno
        qno = max(0, min(qno, TOTAL_PAGES - 1))

        # Update page state
        if qno == 0:
            page = "FRONT"
        elif qno == TOTAL_PAGES - 1:
            if review_page:
                page = "RETURN"
            else:
                page = "SUBMIT"
        else:
            page = "MIDDLE"
            
        return page,qno,nav_event



    ## Question number box in the nav bar (different from the main question box)
    def qnobox_display(self,qno):
        qno_box = TextBox(self.screen,
                          self.font,
                          self.question_rect,
                          QUESTION_BOX_COLOR,
                          PRIMARY_TEXT_COLOR)
        qno_box.draw_textbox(f'Qno: {qno + 1}')




       
        

    def hint_box_popup(self,hint_event,text):
        
        ## Render popup box
        if hint_event == "CLICK":
            self.hint_open = not self.hint_open


        if self.hint_open:
            self.screen.blit(self.overlay,(0,0))
            text = "Hint not available" if not text else text
            self.popup_textbox.draw_textbox(text=text,border_radius=20)
    

    def draw_hint_button(self,mouse_pos,mouse_pressed):

        hint_event = self.hint_button.update(mouse_pos,mouse_pressed)
        self.hint_button.draw(self.screen)
        if self.hint_open:
            self.screen.blit(self.hint_cross_image,self.hint_cross_image_rect)
        else:
            self.screen.blit(self.hint_bulb_image,self.hint_bulb_image_rect)


        return hint_event
    
    def close_hint(self):
        self.hint_open = False







## Component 2 - Question box
class QuestionBox:
    def __init__(self,screen,font):
        self.screen = screen
        self.font = font
        self.left = QUIZ_LEFT_MARGIN
        self.top = QUESTION_TOP_MARGIN
        self.box_width = QUESTION_BOX_WIDTH
        self.box_height = QUESTION_BOX_HEIGHT
        self.box_color = QUESTION_BOX_COLOR
        self.text_color = PRIMARY_TEXT_COLOR


    def draw_question_box(self,text):
        question_textbox = TextBox(self.screen,
                                   self.font,
                                   pygame.Rect(
                                       self.left,
                                       self.top,
                                       self.box_width,
                                       self.box_height),
                                   self.box_color,self.text_color)
        
        question_textbox.draw_textbox(text,'top_left')




## Component 3 - Options container with options (Already a class)

class Options:
    def __init__(self, screen,correct_answers,selected_answers,mode = "QUIZ"):
        self.screen = screen
        self.rects = OPTIONS_RECTS
        self.buttons = []

        self.correct_answers = correct_answers
        self.selected_answers = selected_answers
        self.mode = mode



    def create_buttons(self, text_options):
        self.buttons.clear()
        for rect, text in zip(self.rects, text_options):
            self.buttons.append(Button(rect, text=text,font=option_button_font))




    def draw(
    self,
    text_options,
    mouse_pos,
    mouse_pressed,
    saved_states,
    q_index
):

        if not self.buttons:
            self.create_buttons(text_options)

        selected_index = None

        for i, button in enumerate(self.buttons):

            # ---------------- QUIZ MODE ----------------
            if self.mode == "QUIZ":

                button.state = saved_states[i]

                event = button.update(mouse_pos, mouse_pressed)

                if event == "CLICK":
                    selected_index = i

                button.draw(self.screen)

            # ---------------- REVIEW MODE ----------------
            elif self.mode == "REVIEW":

                button.state = DISABLED  # no interaction

                correct_answer = self.correct_answers[q_index]
                selected_answer = self.selected_answers[q_index]

                if text_options[i] == correct_answer:
                    button.colors[IDLE] = CORRECT_COLOR

                elif text_options[i] == selected_answer:
                    button.colors[IDLE] = WRONG_COLOR

                else:
                    button.colors[IDLE] = BASE_COLOR

                button.draw(self.screen)

        return selected_index
    


    

    def reset_buttons(self):
        self.buttons.clear()





