import random


hard_questions = [
    {
        "question": "Which group provided vital support to activists during 504 sit-in protest?",
        "options": [
            "Black Panther Party",
            "Red Cross",
            "Girl Scouts",
            "Anti-war protesters"
        ],
        "answer": "Black Panther Party",
        "hint": "Support came from a well-known 1960s–70s community activist organization focused on social justice."
    },
    {
        "question": "Where was the first public institution to care for people with disabilities?",
        "options": [
            "Waltham, Mass",
            "New York",
            "Williamsburg, Va",
            "Amherst, Mass"
        ],
        "answer": "New York",
        "hint": "Think of one of the earliest and most populated U.S. states to develop public education systems."
    },
    {
        "question": "Which disability rights advocate co-founded the American civil liberties union?",
        "options": [
            "Stevie Wonder",
            "Stephen Hawking",
            "Helen Keller",
            "None of the above"
        ],
        "answer": "Helen Keller",
        "hint": "This advocate overcame both visual and hearing impairments and became an international symbol of resilience."
    },
    {
        "question": "What do football player Derrick Coleman, hockey player James Kyte, basketball player Lance Allred and baseball player Edward Dundon have in common?",
        "options": [
            "They were the first legally deaf players in the field",
            "They were military veterans who lost limbs",
            "They used wheelchairs after they retired",
            "They played in the Paralympic Games"
        ],
        "answer": "They were the first legally deaf players in the field",
        "hint": "Their shared trait relates to hearing rather than mobility."
    },
    {
        "question": "Dwarfism means a medical or genetic condition resulting in an adult height of how many centimetres or less.",
        "options": [
            "150",
            "146",
            "147",
            "145"
        ],
        "answer": "147",
        "hint": "The measurement is just under 4 feet 10 inches in metric terms."
    },
    {
        "question": "In autistic spectrum disorder when an individual exhibits immediate imitation of words or sounds they have just heard, this is known as:",
        "options": [
            "Echoastic disorder",
            "Echolalia",
            "Phonological inhibition",
            "Grapheme dysfunction"
        ],
        "answer": "Echolalia",
        "hint": "The word comes from a Greek root meaning 'echo.'"
    },
    {
        "question": "Defects with which children are born with are known as:",
        "options": [
            "Acquired disabilities",
            "Congenital disabilities",
            "Natural impairment",
            "None of the above"
        ],
        "answer": "Congenital disabilities",
        "hint": "The term refers to conditions present from birth rather than developed later."
    },
    {
        "question": "Which of the following may cause partial or complete visual impairment?",
        "options": [
            "Glaucoma",
            "Cataracts",
            "Macular Degeneration",
            "All of the above"
        ],
        "answer": "All of the above",
        "hint": "Each option names a medical eye condition."
    },
    {
        "question": "ADHD can be prevented by",
        "options": [
            "Physiotherapy",
            "Psychotherapy",
            "Neurologists",
            "None of the above"
        ],
        "answer": "None of the above",
        "hint": "It is a neurodevelopmental condition without a guaranteed prevention method."
    }
]


for question in hard_questions:
    random.shuffle(question['options'])
