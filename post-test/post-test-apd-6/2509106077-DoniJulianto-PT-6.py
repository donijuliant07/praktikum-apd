import os

users = {
    "donijulianto": {"password": "077", "role": "admin"}
}  # format {username: {"password": ..., "role": ...}}

bookings = {}  # format {id: {"username": ..., "tanggal": ..., "jam": ..., "lapangan": ...}}
booking_id_counter = 1

running = True
while running:
    os.system('cls')
    print("<== Sistem penyewaan lapangan badminton ==>")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        os.system('cls')
        print("<== LOGIN ==>")
        username = input("Username: ")
        password = input("Password: ")
        current_user = None
        if username in users and users[username]["password"] == password:
            current_user = [username, password, users[username]["role"]]
        if current_user:
            role = current_user[2]
            logged_in = True
            while logged_in:
                os.system('cls')
                if role == "admin":
                    print("<== Menu Admin ==>")
                    print("1. Lihat semua penyewaan")
                    print("2. Hapus Penyewaan")
                    print("3. Logout")

                    admin_menu = input("Pilih Menu: ")
                    if admin_menu == "1":
                        os.system('cls')
                        print("<== Semua Penyewaan ==>")
                        for i, (id, b) in enumerate(bookings.items()):
                            print(f"{i + 1}. {b}")
                        input("Tekan Enter untuk kembali ..")
                    elif admin_menu == "2":
                        os.system('cls')
                        print("<== Hapus Penyewaan ==>")
                        for i, (id, b) in enumerate(bookings.items()):
                            print(f"{i + 1}. {b}")
                        idx = input("Nomor yang ingin dihapus: ")
                        if idx.isdigit():
                            idx = int(idx) - 1
                            if 0 <= idx < len(bookings):
                                key_to_delete = list(bookings.keys())[idx]
                                bookings.pop(key_to_delete)
                                print("Data dihapus.")
                            else:
                                print("Nomor tidak valid.")
                        else:
                            print("Input harus angka.")
                        input("Tekan Enter untuk kembali ...")
                    elif admin_menu == "3":
                        logged_in = False
                        break
                    else:
                        print("Pilihan tidak valid.")
                        input("Tekan Enter untuk kembali ...")
                else:
                    print(f"<== Menu Pengguna ({username}) ==>")
                    print("1. Tambah penyewaan")
                    print("2. Lihat penyewaan saya")
                    print("3. Ubah penyewaan")
                    print("4. Hapus penyewaan")
                    print("5. Logout")
                    user_menu = input("Pilih menu: ")

                    if user_menu == "1":
                        os.system('cls')
                        print("<== Tambah Penyewaan ==>")
                        tanggal = input("Tanggal (dd-mm-yyyy): ")
                        jam = input("Jam (HH:MM): ")
                        lapangan = input("Nomor lapangan: ")
                        bookings[str(booking_id_counter)] = {
                            "username": username,
                            "tanggal": tanggal,
                            "jam": jam,
                            "lapangan": lapangan
                        }
                        booking_id_counter += 1
                        print("Penyewaan Berhasil.")
                        input("Tekan Enter untuk kembali... ")
                    elif user_menu == "2":
                        os.system('cls')
                        print("<== Penyewaan Saya ==>")
                        found = False
                        for i, (id, b) in enumerate(bookings.items()):
                            if b["username"] == username:
                                print(f"{i + 1}. {b}")
                                found = True
                        if not found:
                            print("Belum ada penyewaan.")
                        input("Tekan Enter untuk kembali...")
                    elif user_menu == "3":
                        os.system('cls')
                        print("<== Ubah Penyewaan ==>")
                        user_bookings = [(id, b) for id, b in bookings.items() if b["username"] == username]
                        for i, (id, b) in enumerate(user_bookings):
                            print(f"{i + 1}. {b}")
                        idx = input("Nomor yang ingin diubah: ")
                        if idx.isdigit():
                            idx = int(idx) - 1
                            if 0 <= idx < len(user_bookings):
                                tanggal = input("Tanggal Baru: ")
                                jam = input("Jam baru: ")
                                lapangan = input("Lapangan baru: ")
                                id_to_update = user_bookings[idx][0]
                                bookings[id_to_update] = {
                                    "username": username,
                                    "tanggal": tanggal,
                                    "jam": jam,
                                    "lapangan": lapangan
                                }
                                print("Data diubah.")
                            else:
                                print("Nomor tidak valid.")
                        else:
                            print("Input harus angka.")
                        input("Tekan Enter untuk kembali... ")
                    elif user_menu == "4":
                        os.system('cls')
                        print("<== Hapus Penyewaan ==>")
                        user_bookings = [(id, b) for id, b in bookings.items() if b["username"] == username]
                        for i, (id, b) in enumerate(user_bookings):
                            print(f"{i + 1}. {b}")
                        idx = input("Nomor yang ingin dihapus: ")
                        if idx.isdigit():
                            idx = int(idx) - 1
                            if 0 <= idx < len(user_bookings):
                                id_to_delete = user_bookings[idx][0]
                                bookings.pop(id_to_delete)
                                print("Data dihapus.")
                            else:
                                print("Nomor tidak valid.")
                        else:
                            print("Input harus angka.")
                        input("Tekan Enter untuk kembali...")
                    elif user_menu == "5":
                        logged_in = False
                    else:
                        print("Pilihan tidak valid.")
                        input("Tekan Enter untuk kembali... ")
        else:
            print("Login gagal.")
            input("Tekan enter sekali lagi untuk kembali...")

    elif menu == "2":
        os.system('cls')
        print("<== Register ==>")
        username = input("Username: ")
        password = input("Password: ")
        if username in users:
            print("Username sudah terdaftar.")
        else:
            users[username] = {"password": password, "role": "user"}
            print("Registrasi berhasil.")
            input("Tekan Enter untuk kembali...")
            continue

    elif menu == "3":
        running = False
        print("Terima kasih telah menggunakan sistem ini.")
    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter untuk kembali...")
        