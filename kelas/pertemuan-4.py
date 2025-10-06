#for i in range ( 1, 10, 2) :  #angka pertama : start, angka kedua : end, angka ke 3 : step ==> (start, stop, step)
    #print (f'Perulangan ke {i}')

#mahasiswa = ["Bintang", "Fathur", 10]

#for i in mahasiswa: 
    #print(i)

#for i in range (1, 10):
    #for j in range (1, i + 1):
# print("#", end=" ")
# print("")

#perulangan while


#jawab = 'ya'
#hitung = 0
#while(jawab == 'ya'):
#    hitung += 1
#    jawab = input("Ulang lagi? ")
#print(f"Total perulangan: {hitung}")

#angka = [2, 5, 8, 12, 15, 7, 20]
#print("Mencari angka pertama yang lebih besar dari 10...")
#for n in angka:
#   print(f"Sekarang memeriksa angka: {n}")
#   if n > 10:
#        print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
#        break



while True :
    print("MENU")
    print("1. fitur 1")
    print("2. fitur 2")

    opsi = int(input("Masukkan Opsi: "))

    if opsi == 1 :
        print("1. fitur 1")
    elif opsi == 2 :
        print("2. fitur 2")
    elif opsi == 3 :
        break
    else :
        print("pilihan innvalid")
    

