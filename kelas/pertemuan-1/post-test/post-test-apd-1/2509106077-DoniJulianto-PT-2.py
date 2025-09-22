from tabulate import tabulate

#input data pengguna 

nama = input("Masukkan nama lengkap: ")
nim = input("Masukkan NIM: ")
harga = float(input("masukkan harga makanan (Rp) "))

#data menu dan pajak
pajak_pecel_lele = 5
pajak_mie_ayam = 8
pajak_nasi_padang = 10 

#menghitung total harga untuk setiap menu

total_harga_pecel_lele = harga + (harga * pajak_pecel_lele / 100)
total_harga_mie_ayam = harga + (harga * pajak_mie_ayam / 100)
total_harga_nasi_padang = harga + (harga * pajak_nasi_padang / 100)

#tampilkan informasi awal 

print(f"\n{nama} dengan NIM {nim} ingin membeli makanan dengan harga Rp{harga:,.2f}\n")

#susunan tabel dengan cara manual 

print("+--------------+--------+----------------------------+")
print("| Menu         | Pajak  | Total Harga Setelah Pajak  |")
print("+--------------+--------+----------------------------+")
print(f"| Pecel Lele   | {pajak_pecel_lele}%     | Rp{total_harga_pecel_lele:>25,.2f}|")
print(f"| Mie Ayam     | {pajak_mie_ayam}%     | Rp{total_harga_mie_ayam:>25,.2f}|")
print(f"| Nasi Padang  | {pajak_nasi_padang}%    | Rp{total_harga_nasi_padang:>25,.2f}|")
print("+--------------+--------+----------------------------+")
