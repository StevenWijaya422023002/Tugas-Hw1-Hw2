from base.User import User
from Student import Student
from Dosen import Dosen
from superadmin import Superadmin
from grade import Grade

class Admin(User):
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.admin_id = user_id
        self.password = password  

    def create_user_account(self, user_type, *args, **kwargs):  # Menggunakan **kwargs untuk menangani argumen tambahan
        if user_type == "Student":
            return Student(*args)
        elif user_type == "Dosen":
            return Dosen(*args)
        elif user_type == "superadmin":
            return Superadmin(*args, **kwargs)  # Menggunakan **kwargs saat membuat objek Superadmin
        else:
            return None

    def informasi_tagihan(self, bill_id, bills_database):
        if bill_id in bills_database:
            bill = bills_database[bill_id]
            print(f"Bill ID: {bill_id}")
            print(f"Total tagihan:{bill['total tagihan']}")
            print(f"Tanggal pembayaran:{bill['tanggal pembayaran']}")
            print(f"status:{bill['status']}")
        else:
            ValueError("Bill ID not found in the database")
