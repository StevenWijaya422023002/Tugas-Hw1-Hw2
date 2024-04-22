class Attendance:
    def __init__(self, student_id, course_id, dates_absent):
        self.student_id = student_id
        self.course_id = course_id
        self.dates_absent = dates_absent

    def record_absence(self, date):
        self.dates_absent.append(date)
        print(f"Absence recorded for Student ID {self.student_id} in Course ID {self.course_id} on {date}.")

    def calculate_attendance_rate(self, total_classes):
        total_absences = len(self.dates_absent)
        attendance_rate = ((total_classes - total_absences) / total_classes) * 100
        return attendance_rate

attendance = Attendance("S1", "S2", [])


attendance1.record_absence("2024-04-10")
attendance1.record_absence("2024-04-15")
attendance1.record_absence("2024-04-20")


attendance_rate = attendance.alculate_attendance_rate(total_classes=20)
print(f"Attendance rate for student {attendance.student_id} in course {attendance.course_ID}: {attendane_rate}")
