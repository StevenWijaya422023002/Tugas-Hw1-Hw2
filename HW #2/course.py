from Student import Student



class Course:
    def __init__(self, course_id, name, description):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.students_enrolled = []
        self.course_materials = []

    def add_student(self, student_id):
        self.students_enrolled.append(student_id)
        print(f"Student ID {student_id} has been enrolled in Course ID {self.course_id}.")

    def remove_student(self, student_id):
        if student_id in self.students_enrolled:
            self.students_enrolled.remove(student_id)
            print(f"Student ID {student_id} has been removed from Course ID {self.course_id}.")
        else:
            print(f"Student ID {student_id} is not enrolled in Course ID {self.course_id}.")

    def update_course_material(self, new_material):
        self.course_materials.append(new_material)
        print(f"Course material '{new_material}' has been updated for Course ID {self.course_id}.")


course1 = Course("C001", "Programming Fundamentals", "Introduction to programming concepts")


course1.add_student("S001")
course1.add_student("S002")


course1.remove_student("S002")


course1.update_course_material("Week 2 slides")
