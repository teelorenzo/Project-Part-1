from PyQt6.QtWidgets import *
from Student_Grades import *
import csv


class Grades(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.submit.clicked.connect(lambda: self.submit_input())
        self.clear.clicked.connect(lambda: self.clear_input())

    def csv(self):
        with open('input.csv', 'w', newline='') as input_csv:
            content = csv.writer(input_csv)
            content.writerow(['Name', 'Score1', 'Score2', 'Score3', 'Score4', 'Final'])

    # def submit_input(self):
    #     try:
    #         student_name = str(self.name.text())
    #         num_attempts = int(self.noa.text())
    #         s1 = int(self.score_one.text())
    #         s2 = int(self.score_two.text())
    #         s3 = int(self.score_three.text())
    #         s4 = int(self.score_four.text())

    def score_grade(score, best_score):  # this function calcs a letter grade for current score and best score.
        if score >= best_score - 10:
            return 'A'
        if score >= best_score - 20:
            return 'B'
        if score >= best_score - 30:
            return 'C'
        if score >= best_score - 40:
            return 'D'
        else:
            return 'F'

    def grades(self):
        students = int(input("Enter the total number of students: "))
        scores_ints = []
        scores_entered_str = []

        while len(scores_entered_str) < students:
            scores_entered_str = input(f'Enter {students} score(s): ').split()

        i = 0
        while len(scores_ints) < len(scores_entered_str):
            scores_ints.append(int(scores_entered_str[i]))
            i += 1

        best_score = max(scores_ints)

        for i in range(len(scores_ints)):
            print(
                f'Student {i + 1} score is {scores_ints[i]}, and grade is, {self.score_grade(scores_ints[i], best_score)}')

        avg_score = sum(scores_ints) / len(scores_ints)
        print(f'The average score is {avg_score:.2f}, a grade of {self.score_grade(avg_score, best_score)}')

    def clear_input(self):
        self.name.setText('')
        self.noa.setText('')
        self.score_one.setText('')
        self.score_two.setText('')
        self.score_three.setText('')
        self.score_four.setText('')
