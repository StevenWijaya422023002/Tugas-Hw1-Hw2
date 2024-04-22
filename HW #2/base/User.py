class User:
    def __init__(self, user_id, password):
        self._user_id = user_id  
        self._password = password


    def login(self, user_id, password):  
        if user_id == self._user_id and password == self._password:
            print(f"Login Berhasil {self._user_id}!")
            return True
            
        else:
            print("Login Gagal")
            return False

    def get_user_id(self):  
        return self._user_id



