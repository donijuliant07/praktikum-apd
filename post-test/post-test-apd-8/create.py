from data import bookings, booking_id_counter
from prettytable import PrettyTable

def tambah(username):
    global booking_id_counter
    tanggal = input("Tanggal (dd-mm-yyyy): ")
    jam = input("Jam (HH:MM): ")
    lapangan = input("Nomor lapangan: ")
    if not tanggal or not jam or not lapangan:
        print("Semua data harus diisi.")
        return
    bookings[str(booking_id_counter)] = {
        "username": username,
        "tanggal": tanggal,
        "jam": jam,
        "lapangan": lapangan
    }
    booking_id_counter += 1
    print("Penyewaan berhasil.")

def tampilkan_semua():
    table = PrettyTable(["No", "User", "Tanggal", "Jam", "Lapangan"])
    if not bookings:
        print("Belum ada data penyewaan.")
    else:
        for i, (id, b) in enumerate(bookings.items(), start=1):
            table.add_row([i, b["username"], b["tanggal"], b["jam"], b["lapangan"]])
        print(table)

def tampilkan_user(username):
    table = PrettyTable(["No", "Tanggal", "Jam", "Lapangan"])
    user_data = [(id, b) for id, b in bookings.items() if b["username"] == username]
    if not user_data:
        print("Belum ada penyewaan.")
    else:
        for i, (id, b) in enumerate(user_data, start=1):
            table.add_row([i, b["tanggal"], b["jam"], b["lapangan"]])
        print(table)
    return user_data

def ubah(username):
    user_data = tampilkan_user(username)
    if not user_data:
        return
    idx = int(input("Nomor yang ingin diubah: ")) - 1
    if idx < 0 or idx >= len(user_data):
        print("Nomor tidak valid.")
        return
    tanggal = input("Tanggal baru: ")
    jam = input("Jam baru: ")
    lapangan = input("Lapangan baru: ")
    id_to_update = user_data[idx][0]
    bookings[id_to_update] = {
        "username": username,
        "tanggal": tanggal,
        "jam": jam,
        "lapangan": lapangan
    }
    print("Data berhasil diubah.")

def hapus(username):
    user_data = tampilkan_user(username)
    if not user_data:
        return
    idx = int(input("Nomor yang ingin dihapus: ")) - 1
    if idx < 0 or idx >= len(user_data):
        print("Nomor tidak valid.")
        return
    id_to_delete = user_data[idx][0]
    bookings.pop(id_to_delete)
    print("Data berhasil dihapus.")
