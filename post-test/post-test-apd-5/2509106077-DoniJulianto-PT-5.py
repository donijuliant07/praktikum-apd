import os 

users = [["donijulianto","077", "admin"]]  #format pengisian [username,password,role]
bookings = [] #nesteed list kosong untuk menyimpan data penyewaan. format [username,tanggal,jam, lapangan]

running = True
while running :
    os. system('cls')
    print("<== Sistem penyewaan lapangan badminton ==>")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        os.system('cls')
        print("<== LOGIN ==>")
        username = input ("Username: ")
        password = input ("Password: ")
        current_user = None
        for u in users :
            if u[0] == username and u[1] == password :
                current_user = u
                break
        if current_user:
            role = current_user[2]
            logged_in = True
            while logged_in : 
                os.system('cls')
                if role == "admin" :
                    print("<== Menu Admin==>")
                    print("1. Lihat semua penyewaan")
                    print("2. Hapus Penyewaan")
                    print("3. Logout")
                    
                    admin_menu = input("Pilih Menu: ")
                    if admin_menu == "1":
                        os.system('cls')
                        print("<== Semua Penyewaan ==>")
                        for i, b in enumerate(bookings):
                            print(f"{ i+ 1}. {b}")
                        input("Tekan Enter untuk kembali ..")
                    elif admin_menu == "2":
                        os.system('cls')
                        print("<== Hapus Penyewaan ==>")
                        for i, b in enumerate(bookings): 
                            print(f"{i + 1}. {b}")
                        idx = input("Nomor yang ingin dihapus: ")
                        if idx.isdigit():
                            idx = int(idx) - 1
                            if 0 <= idx < len(bookings): 
                                bookings.pop(idx)
                                print("Data dihapus.")
                            else: 
                                print("Nomor tidak valid.")
                        else:
                            print("Input harus angka.")
                        input("Tekan Enter untuk kembali ...")
                    elif admin_menu == "3":
                        logged_in = False
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
                    tanggal = input(" Tanggal (dd-mm-yyyy): ")
                    jam = input("Jam (HH:MM): ")
                    lapangan = input("Nomor lapangan: ")
                    bookings.append([username, tanggal, jam, lapangan])
                    print("Penyewaan Berhasil.")
                    input("Teken Enter untuk kembali... ")
                elif user_menu == "2" : 
                    os.system('cls')
                    print("<== Penyewaan Saya ==>")
                    for i, b in enumerate(bookings):
                        if b[0] == username:
                            print(f"{ i + 1}. {b}")
                        input("Tekan Enter untuk kembali...")
                elif user_menu == "3":
                    os.system('cls')
                    print("<== Ubah penyewaan ==>")
                    user_bookings = [b for b in bookings if b[0] == username]
                    for i, b in enumerate(user_bookings):
                        print(f"{ i + 1}. {b}")
                    idx = input("Nomor yang ingin diubah: ")
                    if idx.isdigit():
                        idx = int(idx) - 1
                        if 0 <= idx < len(user_bookings):
                            tanggal = input("Tanggal Baru: ")
                            jam = input("Jam baru: ")
                            lapangan = input("Lapangan baru: ")
                            for i in range (len(bookings)):
                                if bookings[i] == user_bookings[idx]:
                                    bookings[i] = [username, tanggal, jam, lapangan]
                                    print("Data diubah. ")
                                    break
                        else:
                            print("Nomor tidak valid. ")
                    else:
                        print("Input harus angka.")
                    input("Tekan Enter untuk kembali... ")
                elif user_menu == "4":
                    os.system('cls')
                    print("<== Hapus Penyewaan ==>")
                    user_bookings = [b for b in bookings if b[0] == username]
                    for i, b in enumerate(user_bookings):
                        print(f"{i + 1}. {b}")
                    idx = input("Nomor yang ingin dihapus: ")
                    if idx.isdigit():
                        idx = int(idx) - 1
                        if 0 <= idx < len(user_bookings):
                            for i in range(len(bookings)):
                                if bookings[i] == user_bookings[idx]:
                                    bookings.pop(i)
                                    print("Data dihapus. ")
                                    break
                        else:
                            print("Nomor tidak valid. ")
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
        exists = False
        for u in users:
            if u[0] == username:
                exists = True
                break 
        if exists:
            print("Username sudah terdaftar.")
        else:
            users.append([username, password, "user"])
            print("Registrasi berhasil.")
            input("Tekan Enter untuk kembali...")

    elif menu == "3":
        running = False
        print("Terima kasih telah menggunakan sistem ini.")
    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter untuk kembali...")