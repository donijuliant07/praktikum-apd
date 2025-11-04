from data import bookings, booking_id_counter
from prettytable import PrettyTable
from datetime import datetime

def tambah_penyewaan(username):
    global booking_id_counter
    try:
        tanggal = input("Tanggal (dd-mm-yyyy): ")
        jam = input("Jam (HH:MM): ")
        lapangan = input("Nomor lapangan: ")
        
        try:
            waktu = datetime.strptime(f"{tanggal} {jam}", "%d-%m-%Y %H:%M")
        except ValueError:
            raise ValueError("Format tanggal atau jam tidak valid. Gunakan format dd-mm-yyyy dan HH:MM.")
        
        if waktu < datetime.now():
            raise ValueError("Waktu sewa tidak boleh di masa lalu")
        
        if not tanggal or not jam or not lapangan:
            raise ValueError("Semua data harus diisi.")
        
        bookings[str(booking_id_counter)] = {
            "username": username,
            "waktu": waktu.strftime("%d-%m-%Y %H:%M"),
            "lapangan": lapangan
        }
        booking_id_counter += 1
        print("Penyewaan berhasil.")
    except ValueError as ve:
        print(f" {ve}")
    except Exception as e:
        print(f"Kesalahan saat tambah penyewaan: {e}")

def tampilkan_semua_penyewaan():
    try:
        table = PrettyTable(["No", "User", "waktu", "Lapangan"])
        if not bookings:
            print("Belum ada data penyewaan.")
        else:
            for i, (id, b) in enumerate(bookings.items(), start=1):
                table.add_row([i, b["username"], b["waktu"], b["lapangan"]])
            print(table)
    except Exception as e:
        print(f" Gagal menampilkan data: {e}")

def tampilkan_user(username):
    try:
        table = PrettyTable(["No", "waktu", "Lapangan"])
        user_data = [(id, b) for id, b in bookings.items() if b["username"] == username]
        if not user_data:
            print("Belum ada penyewaan.")
        else:
            for i, (id, b) in enumerate(user_data, start=1):
                table.add_row([i, b["waktu"], b["lapangan"]])
            print(table)
        return user_data
    except Exception as e:
        print(f" Gagal menampilkan data pengguna: {e}")
        return []

def ubah_penyewaan(username):
    try:
        user_data = tampilkan_user(username)
        if not user_data:
            return
        idx = int(input("Nomor yang ingin diubah: ")) - 1
        if idx < 0 or idx >= len(user_data):
            raise IndexError("Nomor tidak valid.")
        
        tanggal = input("Tanggal baru: ")
        jam = input("Jam baru: ")
        lapangan = input("Lapangan baru: ")

        try:
            waktu = datetime.strptime(f"{tanggal} {jam}", "%d-%m-%Y %H:%M")
        except ValueError:
            raise ValueError("Format tanggal atau jam tidak valid. Gunakan format dd-mm-yyyy dan HH:MM.")
        
        if waktu < datetime.now():
            raise ValueError("Waktu sewa tidak boleh di masa lalu")
        
        if not tanggal or not jam or not lapangan:
            raise ValueError("Semua data harus diisi.")
        id_to_update = user_data[idx][0]
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
    except Exception as e:
        print(f" Kesalahan saat ubah data: {e}")

def hapus_penyewaan(username):
    try:
        if username == "admin":
            data_target = list(bookings.items())
            print("== Semua Penyewaan ==")
        else:
            data_target = [(id, b) for id, b in bookings.items() if b["username"] == username]
            print("== Penyewaan Anda ==")

        if not data_target:
            print("Tidak ada data penyewaan.")
            return

        from prettytable import PrettyTable
        table = PrettyTable(["No", "User", "waktu", "Lapangan"])
        for i, (id, b) in enumerate(data_target, start=1):
            table.add_row([i, b["username"], b["waktu"], b["lapangan"]])
        print(table)

        idx = int(input("Nomor yang ingin dihapus: ")) - 1
        if idx < 0 or idx >= len(data_target):
            raise IndexError("Nomor tidak valid.")

        id_to_delete = data_target[idx][0]
        bookings.pop(id_to_delete)
        print(" Data berhasil dihapus.")
    except ValueError:
        print(" Input harus berupa angka.")
    except IndexError as ie:
        print(f" {ie}")
    except Exception as e:
        print(f" Kesalahan saat hapus data: {e}")



