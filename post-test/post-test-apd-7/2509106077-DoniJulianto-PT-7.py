import os


users = {
    "donijulianto": {"password": "077", "role": "admin"}
}
bookings = {}
booking_id_counter = 1
running = True

def menu_admin():
    print("===========================")
    print("|no|  <== Menu Admin ==>  |")
    print("|1.| Lihat semua penyewaan|")
    print("|2.| Hapus penyewaan      |")
    print("|3.| Logout               |")
    print("===========================")
    pilihan_admin = input("Pilih menu: ")
    return pilihan_admin


def registrasi():
    os.system('cls')
    print("<== Register ==>")
    username = input("Username: ")
    password = input("Password: ")
    if not username or not password:
        print("Username/password tidak boleh kosong")
        input("Tekan Enter untuk kembali")
        return
    if username in users:
            print("Username sudah terdaftar.")
    else:
        users[username] = {"password": password, "role": "user"}
        print("Registrasi berhasil.")
    input("Tekan Enter untuk kembali...")

def menu_user(username):
    print( "=========================================")
    print(f"|no| <== Menu Pengguna ({username}) ==> |")
    print( "|1.|          Tambah penyewaan          |")
    print( "|2.|        Lihat penyewaan saya        |")
    print( "|3.|           Ubah penyewaan           |")
    print( "|4.|          Hapus penyewaan           |")
    print( "|5.|               Logout               |")
    print( "=========================================")
    user_menu = input("Pilih menu: ")
    return user_menu

def login(percobaan=1):
    if percobaan > 3:
        print("Terlalu banyak percobaan login.")
        return None
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
    except ValueError as ve:
            print(f" {ve}")
    except KeyError as ke:
            print(f" {ke}")
    except Exception as e:
            print(f" Kesalahan tidak terduga: {e}")

def tampilkan_semua_penyewaan():
    os.system('cls')
    print("<== Semua Penyewaan ==>")
    if not bookings: 
        print("Belum ada data penyewaan.")
    else:
        for i, (id, b) in enumerate(bookings.items()):
            print(f"{i + 1}. {b}")
    input("Tekan Enter untuk kembali...")

def tampilkan_menu_utama():
    os.system('cls')
    print("================================================")
    print("|no|<== Sistem penyewaan lapangan badminton ==>|")
    print("|1.|               Login                       |")
    print("|2.|              Register                     |")
    print("|3.|              Keluar                       |")
    print("================================================")

def tambah_penyewaan(username):
    global booking_id_counter
    os.system('cls')
    print("<== Tambah Penyewaan ==>")
    try:
        print("isi data dibawah ini sesuai dengan format")
        tanggal = input("Tanggal (dd-mm-yyyy): ")
        jam = input("Jam (HH:MM): ")
        lapangan = input("Nomor lapangan: ")
        if not tanggal or not jam or not lapangan:
            raise ValueError("Semua data harus diisi.")
        bookings[str(booking_id_counter)] = {
            "username": username,
            "tanggal": tanggal,
            "jam": jam,
            "lapangan": lapangan
        }
        booking_id_counter += 1
        print("Penyewaan berhasil.")
    except ValueError as ve :
        print(f"{ve}")
    except Exception as e:
        print(f"Kesalahan saat tambah penyewaan: {e}")
    input("Tekan Enter untuk kembali...")

def ubah_penyewaan(username):
    try:
        user_bookings = [(id, b) for id, b in bookings.items() if b["username"] == username]
        if not user_bookings:
            raise KeyError("Tidak ada penyewaan untuk pengguna ini.")
        for i, (id, b) in enumerate(user_bookings):
            print(f"{i + 1}. {b}")

        idx = int(input("Nomor yang ingin diubah: ")) - 1
        if idx < 0 or idx >= len(user_bookings):
            raise IndexError("Nomor yang anda masukkan tidak valid.")

        tanggal = input("Tanggal Baru: ")
        jam = input("Jam baru: ")
        lapangan = input("Lapangan baru: ")

        if not tanggal or not jam or not lapangan:
            raise ValueError("Semua data harus diisi.")

        id_to_update = user_bookings[idx][0]
        bookings[id_to_update] = {
            "username": username,
            "tanggal": tanggal,
            "jam": jam,
            "lapangan": lapangan
        }
        print("Data berhasil diubah.")
    except ValueError as ve:
        print(f" {ve}")
    except IndexError as ie:
        print(f" {ie}")
    except KeyError as ke:
        print(f" {ke}")
    except Exception as e:
        print(f" Kesalahan tidak terduga: {e}")
    input("Tekan Enter untuk kembali...")

def hapus_penyewaan(username):
    os.system('cls')
    print("<== Hapus Penyewaan ==>")
    try:
        user_bookings = [(id, b) for id, b in bookings.items() if b["username"] == username]
        if not user_bookings:
            raise KeyError("Tidak ada penyewaan untuk pengguna ini.")

        for i, (id, b) in enumerate(user_bookings):
            print(f"{i + 1}. {b}")

        idx = input("Nomor yang ingin dihapus: ")
        if not idx.isdigit():
            raise ValueError("Input harus berupa angka.")

        idx = int(idx) - 1
        if idx < 0 or idx >= len(user_bookings):
            raise IndexError("Nomor tidak valid.")

        id_to_delete = user_bookings[idx][0]
        bookings.pop(id_to_delete)
        print("Data berhasil dihapus.")
    except ValueError as ve:
        print(f" {ve}")
    except IndexError as ie:
        print(f" {ie}")
    except KeyError as ke:
        print(f" {ke}")
    except Exception as e:
        print(f" Kesalahan tidak terduga: {e}")
    input("Tekan Enter untuk kembali...")

def main():
    global running 
    while running:
        try:
            tampilkan_menu_utama()
            menu = input("Pilih menu: ")

            if menu == "1":
                os.system('cls')
                print("<== LOGIN ==>")
                username = login()
                if username:
                    role = users[username]["role"]
                    logged_in = True
                    while logged_in:
                        try:
                            os.system('cls')
                            if role == "admin":
                                pilihan_admin = menu_admin()
                                if pilihan_admin == "1":
                                    tampilkan_semua_penyewaan()
                                elif pilihan_admin == "2":
                                    hapus_penyewaan(username="admin")
                                elif pilihan_admin == "3":
                                    logged_in = False
                                else:
                                    print("Pilihan tidak valid.")
                                    input("Tekan Enter untuk kembali...")
                            else:
                                user_menu = menu_user(username)
                                if user_menu == "1":
                                    tambah_penyewaan(username)
                                elif user_menu == "2":
                                    tampilkan_semua_penyewaan()
                                elif user_menu == "3":
                                    ubah_penyewaan(username)
                                elif user_menu == "4":
                                    hapus_penyewaan(username)
                                elif user_menu == "5":
                                    logged_in = False
                                else:
                                    raise ValueError("Pilihan user tidak valid.")
                        except ValueError as ve:
                            print(f"{ve}")
                            input("Tekan Enter untuk kembali...")
                        except KeyError as ke:
                            print(f"Data tidak ditemukan: {ke}")
                            input("Tekan Enter untuk kembali...")
                        except Exception as e:
                            print(f"Kesalahan tidak terduga: {e}")
                            input("Tekan Enter untuk kembali...")
                else:
                    input("Tekan Enter untuk kembali...")

            elif menu == "2":
                registrasi()

            elif menu == "3":
                running = False
                print("Terima kasih telah menggunakan sistem ini.")

            else:
                raise ValueError("Pilihan menu utama tidak valid.")
            
        except ValueError as ve:
            print(f"{ve}")
            input("Tekan Enter untuk kembali...")
        except Exception as e:
            print(f"Kesalahan tidak terduga di sistem utama: {e}")
            input("Tekan Enter untuk kembali...")
main()