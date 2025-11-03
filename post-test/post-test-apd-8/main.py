from clear import clear_screen
from autentikasi import login, registrasi
from menu import tampilkan_menu_utama, menu_admin, menu_user
from CRUD import tampilkan_semua_penyewaan, hapus_penyewaan, tambah_penyewaan, ubah_penyewaan, tampilkan_user
from data import users

def main():
    while True:
        try:
            clear_screen()
            tampilkan_menu_utama()
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                clear_screen()
                print("<== LOGIN ==>")
                username = login()
                if username:
                    role = users[username]["role"]
                    while True:
                        try:
                            clear_screen()
                            if role == "admin":
                                pilihan_admin = menu_admin()
                                if pilihan_admin == "1":
                                    tampilkan_semua_penyewaan()
                                elif pilihan_admin == "2":
                                    hapus_penyewaan("admin")
                                elif pilihan_admin == "3":
                                    break
                                else:
                                    print("Pilihan admin tidak valid.")
                            else:
                                pilihan_user = menu_user(username)
                                if pilihan_user == "1":
                                    tambah_penyewaan(username)
                                elif pilihan_user == "2":
                                    tampilkan_user(username)
                                elif pilihan_user == "3":
                                    ubah_penyewaan(username)
                                elif pilihan_user == "4":
                                    hapus_penyewaan(username)
                                elif pilihan_user == "5":
                                    break
                                else:
                                    print(" Pilihan user tidak valid.")
                        except Exception as e:
                            print(f" Kesalahan saat menjalankan menu: {e}")
                        input("Tekan Enter untuk kembali...")
                else:
                    input("Tekan Enter untuk kembali...")

            elif pilihan == "2":
                clear_screen()
                registrasi()
                input("Tekan Enter untuk kembali...")

            elif pilihan == "3":
                print("Terima kasih telah menggunakan sistem ini.")
                break

            else:
                print(" Pilihan menu utama tidak valid.")
                input("Tekan Enter untuk kembali...")

        except Exception as e:
            print(f" Kesalahan tidak terduga{e}")
main()
