from data import users

def login():
    try:
        username = input("Username: ")
        password = input("Password: ")
        if not username or not password:
            raise ValueError("Username dan password tidak boleh kosong.")
        if username not in users:
            raise KeyError("Username tidak ditemukan.")
        if users[username]["password"] != password:
            raise ValueError("Password salah.")
        print(f"Login berhasil sebagai {users[username]['role']}")
        return username
    except (ValueError, KeyError) as e:
        print(e)
        return None

def registrasi():
    print("<== Register ==>")
    username = input("Username: ")
    password = input("Password: ")
    if not username or not password:
        print("Username/password tidak boleh kosong")
        return
    if username in users:
        print("Username sudah terdaftar.")
    else:
        users[username] = {"password": password, "role": "user"}
        print("Registrasi berhasil.")
