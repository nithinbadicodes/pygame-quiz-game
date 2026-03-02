import random
from data.easy_questions import easy_questions
from data.medium_questions import medium_questions
from data.hard_questions import hard_questions



class QuestionGenerator:
    def __init__(self,total = 8):
        self.total = total
        self.easy_questions = easy_questions
        self.medium_questions = medium_questions
        self.hard_questions = hard_questions


    def generate(self):
        questions = {}

        questions['Easy'] = random.sample(self.easy_questions,self.total)
        questions['Medium'] = random.sample(self.medium_questions,self.total)
        questions['Hard'] = random.sample(self.hard_questions,self.total)


        return questions
    

