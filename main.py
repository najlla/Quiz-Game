from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

quesion_bank = []
for quesion in question_data:
    question_text = quesion["question"]
    question_answer = quesion["correct_answer"]
    new_question = Question(question_text, question_answer)
    quesion_bank.append(new_question)

quiz = QuizBrain(quesion_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")


