class Grade:
    def __init__(self, student_id, course_id, letter_grade, numeric_score):
        self.student_id = student_id
        self.course_id = course_id
        self.letter_grade = letter_grade
        self.numeric_score = numeric_score

    def update_grade(self, new_letter_grade, new_numeric_score):
        self.letter_grade = new_letter_grade
        self.numeric_score = new_numeric_score
        print(f"Grade updated for Student ID {self.student_id} in Course ID {self.course_id}.")
        print(f"New Letter Grade: {self.letter_grade}, New Numeric Score: {self.numeric_score}")


grade1 = Grade("S001", "C001", "A", 85)


grade1.update_grade("B", 75)
