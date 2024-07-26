print(f"PILIH SALAH SATU JAWABAN\n1. Penjumlahan\n2. Pengurangan\n3. Pembagian\n4. Perkalian")
pilihan = input("Pilih salah satu nomor 1/2/3/4: ")

if pilihan == "1":
    # Penjumlahan 
    x = float(input("Masukkan angka pertama: "))
    y = float(input("Masukkan angka kedua: "))
    hasil = x + y
    print(f"Hasil dari {x} + {y} adalah {hasil}")
elif pilihan == "2":
    # Pengurangan
    x = float(input("Masukkan angka pertama: "))
    y = float(input("Masukkan angka kedua: "))
    hasil = x - y
    print(f"Hasil dari {x} - {y} adalah {hasil}")
elif pilihan == "3":
    # Pembagian
    x = float(input("Masukkan angka pertama: "))
    y = float(input("Masukkan angka kedua: "))
    if y != 0:
        hasil = x / y
        print(f"Hasil dari {x} / {y} adalah {hasil}")
    else:
        print("Pembagian dengan nol tidak diperbolehkan.")
elif pilihan == "4":
    # Perkalian
    x = float(input("Masukkan angka pertama: "))
    y = float(input("Masukkan angka kedua: "))
    hasil = x * y
    print(f"Hasil dari {x} × {y} adalah {hasil}")
else:
    print("Pilihan tidak valid.")
