print ("Selamat Datang di Kalkulator Matrix")

matrix1 = []
baris = []

while True:
    print ("Input Data Matriks 1") #Input data matriks 1
    while True:
        nb1 = int(input("Input baris (maksimal 4) = "))
        nk1 = int(input("Input kolom (maksimal 4) = "))
        if nb1 < 5:
            if nk1 < 5:
                break
        else:
            print("\nTolong input angka dalam batas")

    for i in range (nb1):
        simpan_kolom1 = []
        for j in range (nk1):
            isi_kolom1 = int(input(f"Input baris {i+1} kolom {j+1} = "))
            simpan_kolom1.append(isi_kolom1)
        matrix1.append(simpan_kolom1)

    print ("Input Data Matriks 2") #input data matriks 2
    while True:
        nb2 = int(input("Input baris (maksimal 4) = "))
        nk2 = int(input("Input kolom (maksimal 4) = "))
        if nb2 < 5:
            if nk2 < 5:
                break
        else:
            print("\nTolong input angka dalam batas")

    for i in range (nb2):
        simpan_kolom2 = []
        for j in range (nk2):
            isi_kolom2 = int(input(f"Input baris {i+1} kolom {j+1} = "))
            simpan_kolom2.append(isi_kolom2)
        matrix1.append(simpan_kolom2)
    
    ### PILIH MENU ###
    print ("Menu Operasi")
    print ("1. Penjumlahan Matriks")
    print ("2. Pengurangan Matriks")
    print ("3. Perkalian Matriks")
    print ("4. Transpose Matriks") #membalik baris ke kolom dan sebaliknya
    print ("5. Invers Matriks")
    print ("6. Keluar")

    while True:
        try:
            pilih = int(input("Silahkan Ketik Nomor Menu"))
        except:
            print ("Inputan anda tidak valid, silahkan input ulang")
            continue
        
        if pilih < 7:
            break
        else:
            print("Tolong Input Sesuai Nomor yang ada di Menu")
    
    if pilih == 1:  # Penjumlahan Matriks
        if nb1 == nb2 and nk1 == nk2:
            hasil = []
            for i in range(nb1):
                baris_hasil = []
                for j in range(nk1):
                    baris_hasil.append(matrix1[i][j] + matrix1[nb1 + i][j])
                hasil.append(baris_hasil)
            print("\nHasil Penjumlahan Matriks:")
            for row in hasil:
                print(row)
        else:
            print("Penjumlahan tidak bisa dilakukan karena ukuran matriks berbeda.")


    elif pilih == 2:  # Pengurangan Matriks
        if nb1 == nb2 and nk1 == nk2:
            hasil = []
            for i in range(nb1):
                baris_hasil = []
                for j in range(nk1):
                    baris_hasil.append(matrix1[i][j] - matrix1[nb1 + i][j])
                hasil.append(baris_hasil)
            print("\nHasil Pengurangan Matriks:")
            for row in hasil:
                print(row)
        else:
            print("Pengurangan tidak bisa dilakukan karena ukuran matriks berbeda.")

    elif pilih == 3:  # Perkalian Matriks
        if nk1 == nb2:
            hasil = []
            for i in range(nb1):
                baris_hasil = []
                for j in range(nk2):
                    elemen = 0
                    for k in range(nk1):
                        elemen += matrix1[i][k] * matrix1[nb1 + k][j]
                    baris_hasil.append(elemen)
                hasil.append(baris_hasil)
            print("\nHasil Perkalian Matriks:")
            for row in hasil:
                print(row)
        else:
            print("Perkalian tidak bisa dilakukan karena jumlah kolom Matriks 1 tidak sama dengan jumlah baris Matriks 2.")

    elif pilih == 4:  # Transpose Matriks
        print("1. Transpose Matriks 1")
        print("2. Transpose Matriks 2")
        pilihan_transpose = int(input("Pilih Matriks yang akan di-transpose: "))
        if pilihan_transpose == 1:
            hasil = []
            for j in range(nk1):
                baris_hasil = []
                for i in range(nb1):
                    baris_hasil.append(matrix1[i][j])
                hasil.append(baris_hasil)
            print("\nHasil Transpose Matriks 1:")
            for row in hasil:
                print(row)
        elif pilihan_transpose == 2:
            hasil = []
            for j in range(nk2):
                baris_hasil = []
                for i in range(nb2):
                    baris_hasil.append(matrix1[nb1 + i][j])
                hasil.append(baris_hasil)
            print("\nHasil Transpose Matriks 2:")
            for row in hasil:
                print(row)

    elif pilih == 5:  # Invers Matriks
        print("Invers Matriks hanya bisa dilakukan untuk matriks persegi.")
        pilihan_invers = int(input("Pilih Matriks yang akan di-invers (1 atau 2): "))
        if pilihan_invers == 1 and nb1 == nk1:
            print("Invers Matriks 1 masih membutuhkan langkah manual seperti matriks adjoint.")
        elif pilihan_invers == 2 and nb2 == nk2:
            print("Invers Matriks 2 masih membutuhkan langkah manual seperti matriks adjoint.")
        else:
            print("Invers hanya berlaku untuk matriks persegi.")


    elif pilih == 6:
        break

    else:
        print ("Pilihan tidak valid. Program otomatis berhenti")    
        break
    print (matrix1)
    break