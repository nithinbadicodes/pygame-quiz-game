import pygame
from data.constants import BUTTON_TEXT_COLOR, IDLE,SELECTED,PRESSED,HOVERED,DISABLED
from data.constants import BASE_COLOR,PRESSED_COLOR,HOVER_COLOR,SELECTED_COLOR,TEXT_COLOR
from data.constants import WINDOW_HEIGHT,WINDOW_WIDTH
from data.constants import button_font,default_font


from utility.helper_functions import get_prev_next_buttons, get_rect,wrap_text


pygame.init()
pygame.font.init()


class Button:
    def __init__(
        self,
        rect,
        text="",
        font = button_font,
        base_color=BASE_COLOR,
        hover_color=HOVER_COLOR,
        pressed_color=PRESSED_COLOR,
        selected_color = SELECTED_COLOR,
        text_color=BUTTON_TEXT_COLOR,
        border_radius=12,
    ):
        self.rect = rect
        self.text = text
        self.font = font

        self.colors = {
            IDLE: base_color,
            HOVERED: hover_color,
            PRESSED: pressed_color,
            SELECTED:selected_color
        }

        self.text_color = text_color
        self.border_radius = border_radius


        self.state = IDLE
        self._pressed_last_frame = False

    # ---------- Update ----------
    def update(self, mouse_pos, mouse_pressed):
        if self.state == DISABLED:
            return None

        hovered = self.rect.collidepoint(mouse_pos)
        event = None

        if hovered and mouse_pressed and not self._pressed_last_frame:
            self.state = PRESSED

        elif hovered and not mouse_pressed:
            if self._pressed_last_frame:
                event = "CLICK"
            self.state = HOVERED

        elif not hovered and self.state != SELECTED:
            self.state = IDLE

        self._pressed_last_frame = mouse_pressed
        return event

    #

    def draw(self, surface):
        color = self.colors.get(self.state, self.colors[IDLE])

        pygame.draw.rect(
            surface,
            color,
            self.rect,
            border_radius=self.border_radius,
        )

        # ---- Wrapped text rendering ----
        padding = 10
        max_width = self.rect.width - padding * 2

        lines = wrap_text(self.text, self.font, max_width)

        line_height = self.font.get_linesize()  # better than get_height()
        total_height = len(lines) * line_height

        # True vertical centering
        top = self.rect.top + (self.rect.height - total_height) // 2

        for i, line in enumerate(lines):
            text_surf = self.font.render(line, True, self.text_color)
            text_rect = text_surf.get_rect(
                centerx=self.rect.centerx,
                y=top + i * line_height
            )
            surface.blit(text_surf, text_rect)









class TextBox:
    def __init__(self,screen,font,box_rect,bg_color,text_color=TEXT_COLOR):
        self.box_rect = box_rect
        self.bg_color = bg_color
        self.text_color = text_color
        self.screen = screen
        self.font = font



    
    def rendered_text(self,text,topleft=None,spacing=None):
        text_surf = self.font.render(text,True,self.text_color)

        if topleft:

            text_rect = text_surf.get_rect(topleft=(self.box_rect.x+20,spacing))
        else:
            text_rect = text_surf.get_rect(center=self.box_rect.center)

        return text_surf,text_rect
    

    def wrap_text(self,text,offset=20,line_spacing = 30):
        
        
        # inner_rect = pygame.Rect(offset,offset,rect.get_width() - 2 * offset,rect.get_height() - 2*offset)
        inner_rect = get_rect(self.box_rect).inflate(-2*offset,-2*offset)
        words = text.split(" ")
        lines = []
        current = ""
        top = inner_rect.top + 10
        spacings = [top]
        for word in words:
            test_line = current + word + " "
            if self.font.size(test_line)[0] <= inner_rect.width:
                current = test_line
            else:
                lines.append(current)
                current = word + " "
                top += line_spacing
                spacings.append(top)

        lines.append(current)
        
        return inner_rect,lines,spacings
    

    def display_text(self, text, align="center"):

        inner_rect, lines, _ = self.wrap_text(text)

        line_height = self.font.get_height()

        if align == "top_left":
            start_y = inner_rect.top
        else:
            total_height = len(lines) * line_height
            start_y = inner_rect.centery - total_height // 2

        for i, line in enumerate(lines):
            text_surf = self.font.render(line, True, self.text_color)

            if align == "top_left":
                text_rect = text_surf.get_rect(
                    topleft=(inner_rect.left, start_y + i * line_height)
                )
            else:
                text_rect = text_surf.get_rect(
                    centerx=inner_rect.centerx,
                    y=start_y + i * line_height
                )

            self.screen.blit(text_surf, text_rect)

        



    ### Draw textbox explicitly (if put over a button, button loses functionality)
    def draw_textbox(self,text,align='center',border_radius = 12):
        pygame.draw.rect(self.screen,
                         self.bg_color,
                         self.box_rect,
                         border_radius = border_radius
                         )
        
        self.display_text(text,align)
        


        




class Options:
    def __init__(self, screen, answers_tl, padding=30):
        self.screen = screen
        self.padding = padding
        self.answers_tl = answers_tl

        self.button_width = (WINDOW_WIDTH - 3*self.padding) // 2
        self.button_height = (WINDOW_HEIGHT - self.answers_tl - 2*padding)//2

        self.buttons = []

    def create_buttons(self, text_options):
        self.buttons.clear()

        rects = [
            # Top Left
            pygame.Rect(self.padding,
                        self.answers_tl,
                        self.button_width,
                        self.button_height),

            # Top Right
            pygame.Rect(self.button_width + 2*self.padding,
                        self.answers_tl,
                        self.button_width,
                        self.button_height),

            # Bottom Left
            pygame.Rect(self.padding,
                        self.answers_tl + self.button_height + self.padding,
                        self.button_width,
                        self.button_height),

            # Bottom Right
            pygame.Rect(self.button_width + 2*self.padding,
                        self.answers_tl + self.button_height + self.padding,
                        self.button_width,
                        self.button_height)
        ]

        for rect, text in zip(rects, text_options):
            self.buttons.append(Button(rect, text=text))

    def draw(self, text_options, mouse_pos, mouse_pressed, saved_states):
        # Create buttons once per question change
        if not self.buttons:
            self.create_buttons(text_options)

        selected_index = None

        for i, button in enumerate(self.buttons):

            # Restore saved selection state
            button.state = saved_states[i]

            event = button.update(mouse_pos, mouse_pressed)

            if event == "CLICK":
                selected_index = i

            button.draw(self.screen)

        return selected_index

    def reset_buttons(self):
        self.buttons.clear()





