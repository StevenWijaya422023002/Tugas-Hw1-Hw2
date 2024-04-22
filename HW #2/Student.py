from base.User import User


class Student(User):
    def __init__(self, user_id, name, email, password, enrollment_id):
        super().__init__(user_id, password)  
        self.name = name
        self.email = email
        self.enrollment_id = enrollment_id
        self.jadwal_kuliah = {}
        self.Courses = []
        self.absensi = {}
        self.lihat_tagihan = {}
        self.nilai = {}
        self.krs = []

    
    
    
    

    def login(self, user_id, password):
        return super().login(user_id, password)

    def schedule_Kuliah(self):
        if self.jadwal_kuliah:
            print(f"Jadwal kuliah untuk Mahasiswa dengan ID {self.enrollment_id}:")
            for day, courses in self.jadwal_kuliah.items():
                print(f"{day}: {', '.join(courses)}")
        else:
            print("Jadwal kuliah tidak tersedia untuk mahasiswa ini.")
    
    def Enroll_In_Course(self, course):
        self.Courses.append(course)
        course.add_student(self)
    
    def view_course(self):
        print(f"{self.name} has class in: ")
        for course in self.Courses:
             print(f"{course.name}")

    def lihat_Absen(self):
        if self.absensi:
            print(f"Jumlah total absensi untuk mahasiswa dengan ID {self.enrollment_id}:")
            for course, attendance in self.absensi.items():
                 print(f"{course}: {attendance}")
        else:
            print("Absensi tidak tersedia untuk mahasiswa ini.")
            

    def tagihan(self):
        if self.lihat_tagihan:
            print(f"Tagihan untuk Mahasiswa dengan ID {self.enrollment_id}:")
            for item, amount in self.lihat_tagihan.items():
                print(f"{item}: {amount}")
        else:
            print("Tagihan tidak tersedia untuk mahasiswa ini.")

    def lihat_nilai(self):
        if self.nilai:
            print(f"Nilai untuk Mahasiswa dengan ID {self.enrollment_id}:")
            for course, nilai in self.nilai.items():
                print(f"{course}: {nilai}")
        else:
            print("Nilai tidak tersedia untuk mahasiswa ini.")

    def lihat_krs(self, course):
        self.krs.append(course)
        print(f"Berhasil mendaftarkan mata kuliah {course} ke dalam KRS.")



