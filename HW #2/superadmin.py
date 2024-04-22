from base.User import User

class Superadmin(User):
    def __init__(self, user_id, name, email, password, super_admin_id):
        super().__init__(user_id, password)
        self.name = name
        self.email = email
        self.super_admin_id = super_admin_id

    def get_name(self):
        return self.name

    def login(self, user_id, password):
        return super().login(user_id, password)

    def tambah_fitur(self, fitur):
        print(f"Fitur '{fitur}' telah ditambahkan.")

    def maintenance_sistem(self):
        print("Sistem sedang dalam maintenance.")


superadmin_user = Superadmin("SA1", "Tubagus", "tubagus.marzuqi@ukrida.ac.id", "supad1", "s111")

superadmin_user.tambah_fitur("Dashboard baru")
superadmin_user.maintenance_sistem()
