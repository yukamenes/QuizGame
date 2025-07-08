"""
Module defining the Question class for representing quiz questions.

The Question class stores the text and correct answer for each quiz question.
"""
class Question:
    def __init__(self, text, answer):
        """
        Initialize a Question object.

        Args:
            text (str): The question text.
            answer (str): The correct answer ('True' or 'False').
        """
        self.text = text
        self.answer = answer