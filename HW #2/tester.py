from admin import Admin
from course import Course
from Dosen import Dosen
from Student import Student
from grade import Grade
from superadmin import Superadmin

def main():
    admin = Admin("A1", "Supri", "supri@si.ukrida.ac.id", "adminpass")

   
    student = admin.create_user_account("student", "Student", "Steven Wijaya", "steven@si.ukrida.ac.id", "studentpass", "E1234")
    student1 = Student("Steven Wijaya", "422023002", "Steven@si.ukrida.ac.id", "studentpass", "E1234")

    dosen = admin.create_user_account("dosen", "Dosen", "Hendrik", "hendrick@si.ukrida.ac.id", "dosenpass", "F1212")
    dosen1 = Dosen("Hendrik", "42202909", "hendrick@si.ukrida.ac.id", "studentpass", "E1234")
   
    superadmin = admin.create_user_account("superadmin", "Superadmin", "Tubagus", "tubagus@ukrida.ac.id", "superadminpass", super_admin_id="S111")

    for user in [student, student1, dosen, superadmin]:
        if user:
            print(f"User {user.get_user_id()} can log in: {user.login(user.get_user_id(), user._password)}")
    

  

    print("\nSuper Admin Name: ", superadmin.get_name())

    print("\n")

    
    dsp_course = Course("siwp1001", "Algorithma", "Introduction to programming and algorithms fundamental")
    pbo_course = Course("siwp2005", "PBO", "object oriented programming")

    
    student1.Enroll_In_Course(dsp_course)
    print(f"Student {student1.get_user_id()} enrolled in course {dsp_course.name}")

    student1.Enroll_In_Course(pbo_course)
    print(f"Student {student1.get_user_id()} enrolled in course {pbo_course.name}")

    dosen1.Enroll_In_Course(pbo_course)
    print(f"Dosen  mengajar di class {pbo_course.name}")



if __name__ == "__main__":
    main()
