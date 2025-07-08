"""
Main module to run the QuizGame application.

This module initializes the quiz by creating Question objects from the question data,
sets up the QuizBrain, and runs the quiz loop until completion.
"""
from question_model import Question
from data import question_data
from random import choice
from quiz_brain import QuizBrain
import html

question_bank = [
    Question(html.unescape(data["question"]), data["correct_answer"])
    for data in question_data
]

quizBrain = QuizBrain(question_bank)
while quizBrain.still_has_questions():
    quizBrain.next_question()
    quizBrain.question_number += 1

print("You've completed the quiz!")
print(f"Your final score was {quizBrain.score}/{quizBrain.question_number}")