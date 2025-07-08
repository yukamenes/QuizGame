"""
Module containing the quiz question data sourced from the Open Trivia Database.

This module defines a list of dictionaries, each representing a true/false question
with details such as category, difficulty, question text, correct answer, and incorrect answers.
The data is used to populate the quiz in the QuizGame application.
Source: https://opentdb.com/
"""
question_data = [
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "The film &quot;2001: A Space Odyssey&quot; was released on December 31st, 2000.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "Shaquille O&#039;Neal appeared in the 1997 film &quot;Space Jam&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "In the original Star Wars trilogy, David Prowse was the actor who physically portrayed Darth Vader.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "Leonardo DiCaprio won an Oscar for Best Actor in 2004&#039;s &quot;The Aviator&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "Samuel L. Jackson had the words, &#039;Bad Motherf*cker&#039; in-scripted on his lightsaber during the filming of Star Wars.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "George Lucas directed the entire original Star Wars trilogy.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "Actor Tommy Chong served prison time.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "&quot;Foodfight!&quot; earned less than $80,000 at box office.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "In Alfred Hitchcock&#039;s film &#039;Psycho&#039; it is said he used chocolate syrup to simulate the blood in the famous shower scene from ",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Entertainment: Film",
     "question": "In the movie The Revenant, DiCaprio&#039;s character hunts down the killer of his son.",
     "correct_answer": "True", "incorrect_answers": ["False"]}
]
