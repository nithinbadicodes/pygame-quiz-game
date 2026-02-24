import random


medium_questions = [
    {
        "question": "Where did the first national disability pride parade take place?",
        "options": [
            "New York city",
            "San Francisco",
            "Chicago, Illinois",
            "Washington, D.C."
        ],
        "answer": "Chicago, Illinois",
        "hint": "This Midwestern city is often called the birthplace of the Disability Pride movement in the U.S."
    },
    {
        "question": "Who is “the mother” of disability rights movement?",
        "options": [
            "Helen Keller",
            "Lois Curtis",
            "Alice Wong",
            "Judy Heumann"
        ],
        "answer": "Judy Heumann",
        "hint": "She used a wheelchair due to polio and played a major role in the 504 Sit-in and the fight for the ADA."
    },
    {
        "question": "Where was the first American school for deaf people?",
        "options": [
            "Martha’s Vineyard, Mass",
            "West Hartford, Conn",
            "Beverly, Mass",
            "Albany, N.Y."
        ],
        "answer": "West Hartford, Conn",
        "hint": "It was founded in 1817 by Thomas Gallaudet and Laurent Clerc in Connecticut."
    },
    {
        "question": "This summer, Special Olympics celebrates its 50th anniversary. Where did the organization get its start?",
        "options": [
            "A program at the Chicago Park District",
            "A campaign by activists in San Francisco",
            "A 5K race in New York City",
            "None of the above"
        ],
        "answer": "A program at the Chicago Park District",
        "hint": "The first International Special Olympics Games were held in this city's park district in 1968."
    },
    {
        "question": "Who is known as “Father of Sports for People with Disabilities”?",
        "options": [
            "Karl Rogers",
            "Ludwig Guttmann",
            "Lesley Neve",
            "Clifford Morgan"
        ],
        "answer": "Ludwig Guttmann",
        "hint": "He organized the Stoke Mandeville Games in 1948, which later evolved into the Paralympics."
    },
    {
        "question": "Which is not the definition of disability as seen by the Human Rights and Equal Opportunity Commission (1994)?",
        "options": [
            "Loss of physical or mental function",
            "Loss of a part of the body",
            "Any condition which affects a person’s thought processes",
            "Emotional stress"
        ],
        "answer": "Emotional stress",
        "hint": "This may result from disability but is not classified as one on its own."
    },
    {
        "question": "What is Braille?",
        "options": [
            "An electronic display that helps visually impaired students read computer screens",
            "A tactile output that helps students use telephones",
            "A communications system of touch that allows persons who are blind to read, review, and study the written word",
            "None of the above"
        ],
        "answer": "A communications system of touch that allows persons who are blind to read, review, and study the written word",
        "hint": "It uses raised dots arranged in patterns that can be read by touch."
    },
    {
        "question": "Environmental accommodations for students with sensory needs may include:",
        "options": [
            "Seating placement of the student",
            "Modifications to the classroom",
            "Modifications for instruction and instructional materials",
            "All of the above"
        ],
        "answer": "All of the above",
        "hint": "Support for sensory needs often involves adjustments to environment, materials, and seating."
    },
    {
        "question": "Which of the following is a hereditary genetic disease of muscle?",
        "options": [
            "Leprosy",
            "Thalassemia",
            "Muscular Dystrophy",
            "None of the above"
        ],
        "answer": "Muscular Dystrophy",
        "hint": "This condition causes progressive weakening and degeneration of skeletal muscles."
    },
    {
        "question": "Which Deaf/hard of hearing person broke barriers and won two popular reality television show competitions?",
        "options": [
            "Nyle DiMarco",
            "Lou Ferringo",
            "Marlee Matlin",
            "Linda Bove"
        ],
        "answer": "Nyle DiMarco",
        "hint": "He won America's Next Top Model (Cycle 22) and Dancing with the Stars (Season 22)."
    },
    {
        "question": "One of the most important early childhood measures to prevent disabilities is:",
        "options": [
            "Late immunization",
            "Avoiding breastfeeding",
            "Timely immunization as per national schedule",
            "Admission to special school"
        ],
        "answer": "Timely immunization as per national schedule",
        "hint": "Vaccines protect children from preventable diseases that can cause lifelong impairments."
    },
    {
        "question": "The primary characteristic of children with ‘dyslexia’ includes:",
        "options": [
            "Attention deficit disorders",
            "Divergent thinking; fluency in reading",
            "Inability to read fluently",
            "Engaging in repetitive locomotor actions"
        ],
        "answer": "Inability to read fluently",
        "hint": "This learning disorder mainly affects reading accuracy and fluency."
    },
    {
        "question": "Which among the following can cause impairment during pregnancy?",
        "options": [
            "Use of drugs and medicines",
            "Certain infections",
            "Inadequate consumption of food and nutrients like iron",
            "All of the above"
        ],
        "answer": "All of the above",
        "hint": "Multiple environmental and health factors during pregnancy can affect fetal development."
    },
    {
        "question": "The following disability is an example of non-functioning of muscle coordination due to damage in brain:",
        "options": [
            "Autism",
            "Dwarfism",
            "Locomotor disability",
            "Cerebral Palsy"
        ],
        "answer": "Cerebral Palsy",
        "hint": "This condition affects movement, muscle tone, and posture due to early brain damage."
    }
]


for question in medium_questions:
    random.shuffle(question['options'])

