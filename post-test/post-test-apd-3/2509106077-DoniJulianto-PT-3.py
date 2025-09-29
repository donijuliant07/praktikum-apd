UKT = 6000000
datanama = "Doni Julianto"
datanim = "2509106077"

print("<--LOGIN MAHASISWA-->")
nama = (input("Masukkan Nama: "))
NIM  = (input("Masukkan NIM: "))

if nama == datanama and NIM == datanim :
    print ("\nLOGIN BERHASIL!!")
    print (f"Selamat Datang {nama}, dengan NIM {NIM}. Silahkan Memilih Metode Pembayaran UKT")
    print ("<--MENU PEMBAYARAN-->") 
    print ("1. Sekali Bayar(Lunas) - Biaya Admin 1%")
    print ("2. Cicilan 2x - Biaya Admin 5%")
    print ("3. Cicilan 4x - Biaya Admin 8%")
    print ("4. Cicilan 6x - Biaya Admin 12%")
    
    pilihan = input("pilihlah motode pembayaran (1/2/3/4): ")

    if pilihan == "1" :
        admin = 0.01
        total = UKT + ( UKT * admin ) 
        print(f"\nMetode: Sekali Bayar")
        print(f"Total Bayar: Rp {total:,.0f}")
    elif pilihan == "2" : 
        admin = 0.05
        cicilan = 2 
        total = UKT + ( UKT * admin )
        per_cicilan= total/ cicilan
        print("\nMetode: Cicilan 2x")
        print(f"Total Bayar : Rp {total:,.0f}")
        print(f"Per cicilan: Rp {per_cicilan:,.0f}")
    elif pilihan == "3" : 
        admin = 0.08
        cicilan = 4
        total = UKT + (UKT * admin )
        per_cicilan = total / cicilan 
        print("\nMetode: Cicilan 4x")
        print(f"total Bayar: {total:,.0f}")
        print(f"per cicilan = {per_cicilan:,.0f}")
    elif pilihan == "4" :
        admin = 0.12
        cicilan = 6
        total = UKT ( UKT * admin )
        per_cicilan = total/cicilan 
        print("\n Metode: Cicilan 6x")
        print(f"Total Bayar : Rp {total:,.0f}")
        print(f"Per cicilan: Rp {per_cicilan:,.0f}")
    else :
        print("pilihan yang anda pilih tidak ada")

else :
    print("GAGAL LOGIN:(")
    print("Silahkan cek kembali nama dan NIM anda. :)")
    

