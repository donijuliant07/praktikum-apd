def tampilkan_menu_utama():
    print("===========================================")
    print("|no|<== Sistem Penyewaan Lapangan ==>     |")
    print("|1.| Login                                |")
    print("|2.| Register                             |")
    print("|3.| Keluar                               |")
    print("===========================================")

def menu_admin():
    print("===========================")
    print("|no|  <== Menu Admin ==>  |")
    print("|1.| Lihat semua penyewaan|")
    print("|2.| Hapus penyewaan      |")
    print("|3.| Logout               |")
    print("===========================")
    return input("Pilih menu: ")

def menu_user(username):
    print("===========================================")
    print(f"|no| <== Menu Pengguna ({username}) ==>   |")
    print("|1.| Tambah penyewaan                     |")
    print("|2.| Lihat penyewaan saya                 |")
    print("|3.| Ubah penyewaan                       |")
    print("|4.| Hapus penyewaan                      |")
    print("|5.| Logout                               |")
    print("===========================================")
    return input("Pilih menu: ")