"""
Module defining the QuizBrain class for managing the quiz logic.

The QuizBrain class handles the flow of the quiz, including tracking the current question,
user score, and validating user answers. It interacts with Question objects to present
questions and evaluate responses.
"""
class QuizBrain:
    def __init__(self, questions_list):
        """
        Initialize the QuizBrain with a list of questions.

        Args:
            questions_list (list): List of Question objects to be used in the quiz.
        """
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        """
        Check if there are remaining questions in the quiz.

        Returns:
            bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.questions_list)

    def next_question(self):
        """
        Present the next question to the user and process their answer.
        """
        question = self.questions_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {question.text} (True/False)? ").lower()
        while user_answer not in ["true", "false"]:
            print("Wrong answer! Type True or False, please :)")
            user_answer = input(f"Q.{self.question_number + 1}: {question.text} (True/False)? ").lower()
        self.check_answer(user_answer, question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        """
        Check if the user's answer is correct and update the score.

        Args:
            user_answer (str): The user's answer ('true' or 'false').
            correct_answer (str): The correct answer for the question.
        """
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number + 1}")
        print("\n")