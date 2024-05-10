from PyQt6.QtWidgets import *
from Student_Grades import Ui_MainWindow
import csv


class Grades(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.avg_score = None
        """
        Setting up user interface:
        > Calling submit funtion with submit button.
        > Calling clear function with clear button.
        > Making sure that combo box is linked with the change of user choice,
        also calling to the validate Number of Attempts (noa) function.
        > Hiding all labels from user until NOA is entered. 
        """
        self.setupUi(self)
        self.submit.clicked.connect(self.submit_input)
        self.clear.clicked.connect(self.clear_input)
        self.comboBox.currentIndexChanged.connect(self.validate_noa)
        self.scores = [self.score_one.text().strip(), self.score_two.text().strip(), self.score_three.text().strip(),
                       self.score_four.text().strip()]
        hide_labels = self.label_3, self.label_4, self.label_5, self.label_6
        for i in hide_labels:
            i.setVisible(False)
        hide_scores = self.score_one, self.score_two, self.score_three, self.score_four
        for i in hide_scores:
            i.setVisible(False)

    def validate_name(self) -> bool:
        """
        This is the Validation of Users Name function
        > Name is what the user entered in name_input portion of GUI.
        it is being checked for 3 errors
            -If the name_input portion of GUI is blank.
            -If the name entered is a number.
            -If the name entered is less than a recognizable name size (say the character length is too short)
         """
        name = self.name_input.text()
        if name == "":  # no name entered
            QMessageBox.warning(self, "wrong Name Entered", "Please enter student Full & Last name")
            return False
        elif name.isdigit():  # I want to check if numbers were entered.
            QMessageBox.warning(self, "Number Entered", "Please enter a First and Last name not Number")
            return False
        if len(name) < 2:  # I want to check if name length is too short.
            QMessageBox.warning(self, "Name Length Error", "Add more characters in the name section")
            return False

        return True

    def validate_noa(self):
        """
        This is the Validation of Number of Attempts (noa) from user
        > In the QT developer this default value is empty and say the user doesn't choose number of attempts it should
        prompt the user to choose 1-4 attempts from the combo box
        > This function also makes the labels appear dynamics by setting and unsetting
        visibility when a certain number is selected.
        :return: bool
        """
        if self.comboBox.currentText() == " ":
            QMessageBox.warning(self, "Number of Attempts", "Choose 1-4 attempts in the drop down menu.")
            return
            # I want to validate the user has entered 1-4
        cmb = int(self.comboBox.currentText())
        if cmb == 1:
            self.label_3.setVisible(True)
            self.score_one.setVisible(True)
            self.label_4.setVisible(False)
            self.score_two.setVisible(False)
            self.label_5.setVisible(False)
            self.score_three.setVisible(False)
            self.label_6.setVisible(False)
            self.score_four.setVisible(False)
        elif cmb == 2:
            self.label_3.setVisible(True)
            self.score_one.setVisible(True)
            self.label_4.setVisible(True)
            self.score_two.setVisible(True)
            self.label_5.setVisible(False)
            self.score_three.setVisible(False)
            self.label_6.setVisible(False)
            self.score_four.setVisible(False)
        elif cmb == 3:
            self.label_3.setVisible(True)
            self.score_one.setVisible(True)
            self.label_4.setVisible(True)
            self.score_two.setVisible(True)
            self.label_5.setVisible(True)
            self.score_three.setVisible(True)
            self.label_6.setVisible(False)
            self.score_four.setVisible(False)
        elif cmb == 4:
            self.label_3.setVisible(True)
            self.score_one.setVisible(True)
            self.label_4.setVisible(True)
            self.score_two.setVisible(True)
            self.label_5.setVisible(True)
            self.score_three.setVisible(True)
            self.label_6.setVisible(True)
            self.score_four.setVisible(True)
        return True

    # I want to validate if user enter number not letters.
    # I want to display the labels along with user input.
    def validate_scores(self) -> bool:
        """
        This function is the Score Validation function
        > Checking to see if user entered a number in the range from 0-100.
        """
        # get text no int conversion
        for score in self.scores:
            if score:
                try:
                    score_value = int(score)
                    if score_value < 0 or score_value > 100:
                        return False
                except ValueError:
                    return False
        return True
        # try:
        #     if int(i) < 0:
        #         QMessageBox.warning(self, "Number", "Please enter a number greater than 0.")
        #         return False
        #     elif int(i) > 100:
        #         QMessageBox.warning(self, "Number", "Please enter a number less than 100.")
        #         return False
        # except ValueError:  # this will help with string values.
        #     QMessageBox.warning(self, "Wrong", "Enter a number 0 - 100")
        #     return False

        # I want it to not end after pop up

    def submit_input(self) -> None:
        """
        This is the submit function
        > self.Scores takes the new scores entered.
        > The for loops ensures 0 are accounted for if user doesn't enter number.
        > The if statement makes sure all validations are meant name, number of attempts and score.
        > It then takes the users input and places it into a csv document.
        > Else is if the validations are not met specifically the number validations.
        :return: NONE
        """
        # Update self.scores with the latest input values
        self.scores = [self.score_one.text().strip(), self.score_two.text().strip(),
                       self.score_three.text().strip(), self.score_four.text().strip()]

        for i in range(len(self.scores)):
            if not self.scores[i]:
                self.scores[i] = '0'

        if self.validate_name() and self.validate_noa() and self.validate_scores():
            row_scores = [int(score) for score in self.scores if score]  # Convert scores to integers
            self.avg_score = max(row_scores)  # I just want max score
            with open('input_grades.csv', 'a', newline='') as input_grades_csv:
                content = csv.writer(input_grades_csv)
                content.writerow(['Name', 'Score1', 'Score2', 'Score3', 'Score4', 'Final'])
                content.writerow(
                    [self.name_input.text().strip(), self.scores[0], self.scores[1],
                     self.scores[2], self.scores[3], self.avg_score])
                self.clear_input()
            return QMessageBox.warning(self, "Data", f"Data is good and saved")
        else:
            return QMessageBox.warning(self, "Watch out", f"You have either not entere a correct name value. Please "
                                                          f"enter a first and last name for Student."
                                                          f"You've either entered a bad score value. Enter 0-100"
                                                          f"You have either not entered number of attempts please "
                                                          f"select 1-4")

    def clear_input(self) -> None:
        """
        This clears inputs when clear button is hit
        """
        self.name_input.clear()
        self.score_one.clear()
        self.score_two.clear()
        self.score_three.clear()
        self.score_four.clear()


def main():
    application = QApplication([])
    window = Grades()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()

#made changes to push to github
