from base.User import User


class Dosen:
    def __init__(self, user_id, name, email, password, faculty_id):
        super().__init__(user_id, name, email, password)
        self.FacultyID = faculty_id
        self.IsiNilai = {}  
        self.Absen = {}  
        self.UpdateJadwal = {}  

    
    def login(self, user_id, password):
        return super().login(user_id, password)

    def isi_nilai(self, student_id, course, grade):
        
        if student_id not in self.IsiNilai:
            self.IsiNilai[student_id] = {}
        self.IsiNilai[student_id][course] = grade
        print(f"Nilai untuk mahasiswa dengan ID {student_id} pada mata kuliah {course} telah diisi: {grade}")

    def absen(self, course, date, attendance_list):
        
        if course not in self.Absen:
            self.Absen[course] = {}
        self.Absen[course][date] = attendance_list
        print(f"Absensi untuk mata kuliah {course} pada tanggal {date} telah dicatat: {attendance_list}")

    def update_jadwal(self, course, new_schedule):
        
        self.UpdateJadwal[course] = new_schedule
        print(f"Jadwal untuk mata kuliah {course} telah diperbarui menjadi: {new_schedule}")


