# Program Toko Furnitur Sumber Abadi

# Data login yang valid
valid_username = "DoniJulianto"
valid_password = "doniaja123"

# Inisialisasi variabel
total_bayar = 0
detail_pembelian = []

# Validasi Login
attempt = 0
max_attempt = 3
login_success = False

while attempt < max_attempt:
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if username == valid_username and password == valid_password:
        print("\nLogin berhasil!!\n")
        login_success = True
        break
    else:
        attempt += 1
        print(f"Login gagal. Silahkan cek Username dan Password anda kembali. ({attempt}/{max_attempt})\n")

# Jika login gagal 3 kali, keluar dari program
if not login_success:
    print("Login gagal 3 kali. Program dihentikan.")
    exit()

# Menu Pembelian Furnitur
while True:
    print("=== List harga  Furnitur ===")
    print("1. Sofa - Rp 500.000")
    print("2. Meja Belajar - Rp 250.000")
    print("3. Rak Lemari - Rp 150.000")
    print("4. Keluar")

    pilihan = input("Silahkan pilih furnitur yang tersedia (1-4): ")

    if pilihan == "1":
        harga = 500000
        nama_barang = "Sofa"
    elif pilihan == "2":
        harga = 250000
        nama_barang = "Meja Belajar"
    elif pilihan == "3":
        harga = 150000
        nama_barang = "Rak Lemari"
    elif pilihan == "4":
        print("Keluar dari menu pembelian...\n")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1-4.\n")
        continue

    jumlah = input(f"Masukkan jumlah {nama_barang} yang ingin dibeli: ")

    if jumlah.isdigit():
        jumlah = int(jumlah)
        subtotal = 0
        for _ in range(jumlah):
            subtotal += harga
        total_bayar += subtotal
        detail_pembelian.append((nama_barang, jumlah, subtotal))
        print(f"{jumlah} unit {nama_barang} ditambahkan. Subtotal: Rp {subtotal:,}\n")
    else:
        print("Jumlah harus berupa angka.\n")

# Rincian Pembelian
print("\n=== Rincian Pembelian ===")
for item in detail_pembelian:
    print(f"{item[0]} - {item[1]} unit - Rp {item[2]:,}")

print(f"\nTotal Bayar Sebelum Diskon: Rp {total_bayar:,}")

# POIN PLUS: Diskon dan Bonus
if total_bayar >= 700000:
    diskon = total_bayar * 0.20
    total_bayar -= diskon
    print(f"Anda mendapat potongan 20%. Diskon: Rp {diskon:,}")
elif total_bayar >= 500000:
    diskon = total_bayar * 0.08
    total_bayar -= diskon
    print(f"Anda mendapat potongan 8%. Diskon: Rp {diskon:,}")
elif total_bayar >= 150000:
    print("Anda mendapat bonus Kitchen Set!")

print(f"\nTotal Bayaran Anda: Rp {total_bayar:,}")
print("Terima kasih telah berbelanja di Toko Furnitur Sumber Abadi!")