print ("Selamat Datang di Kalkulator Matriks")

# m1 = matriks 1 
# m2 = matriks 2
# nb1 : banyak baris di matrix 1
# nk1 : banyak kolom di matrix 1
# nb2 : banyak baris di matrix 2
# nk2 : banyak kolom di matrix 2


while True:
    m1 = []
    m2 = []
    mhasil = []
    print("\nMenu Operasi")
    print("1. Penjumlahan Matriks")
    print("2. Pengurangan Matriks")
    print("3. Perkalian Matriks")
    print("4. Determinant Matriks")
    print("5. Invers Matriks")
    print("6. Keluar")

    try :
        pilihan = int(input("\nSilahkan Pilih Angka Menu Operasi : "))
    except ValueError:
        print("Inputan anda salah. Silahkan input ulang.")
        continue

    # MENU 1 #    
    if pilihan == 1:
        print("\nSilahkan Input Data Matriks 1")
        while True:
            try :
                nb1 = int(input("Silahkan Input Banyak Baris (Maksimal 4): "))
            except ValueError:
                print("Inputan anda salah. Silahkan input ulang.")
                continue
            
            if 0 < nb1 < 5:
                break
            else:
                print("Tolong input dalam batas.\n")

        while True:
            try :
                nk1 = int(input("Silahkan Input Banyak Kolom (Maksimal 4) : "))
                print("\n")
            except ValueError:
                print("Inputan anda salah. Silahkan input ulang\n")
                continue
            
            if 0 < nk1 < 5:
                break
            else:
                print("Tolong input dalam batas.\n")
        
        for i in range(nb1):
            simpan_kolom1 = []
            for j in range(nk1):
                try:
                    isi_kolom1 = int(input(f"Silahkan input baris {i+1} kolom {j+1} : "))
                    simpan_kolom1.append(isi_kolom1)
                except ValueError:
                    print("Inputan anda salah. Silahkan input ulang\n")
                    continue
            m1.append(simpan_kolom1)
        
        print ("\nSilahkan Input Data Matriks 2")
        for i in range(nb1):
            simpan_kolom2 = []
            for j in range(nk1):
                try:
                    isi_kolom2 = int(input(f"Silahkan input baris {i+1} kolom {j+1} : "))
                    simpan_kolom2.append(isi_kolom2)
                except ValueError:
                    print("Inputan anda salah. Silahkan input ulang\n")
                    continue
            m2.append(simpan_kolom2)
        
        hasil_penjumlahan = []
        for i in range(nb1):
            barishasil1 = []
            for j in range(nk1):
                barishasil1.append(m1[i][j] + m2[i][j])
            hasil_penjumlahan.append(barishasil1)
        print(f"Hasil penjumlahan matriks adalah : ")
        for row in hasil_penjumlahan:
            print(row)

    # MENU 2 #  
    elif pilihan == 2:
        print("\Silahkan Input Data Matriks 1")
        while True:
            try:
                nb1 = int(input("Silahkan Input Banyak Baris (Maksimal 4) : "))
            except ValueError:
                print("Inputan anda salah. Silahkan input ulang.")
                continue

            if 0 < nb1 < 5 :
                break
            else:
                print("Tolong input dalam batas.\n")
        
        while True:
            try:
                nk1 = int(input("Silahkan Input Banyak Kolom (Maksimal 4) : "))
                print("\n")
            except ValueError:
                print("Inputan anda salah. Silahkan input ulang.\n")
                continue
            
            if 0 < nk1 < 5:
                break
            else:
                print("Tolong input dalam batas.\n")
        
        for i in range(nb1):
            simpan_kolom1 = []
            for j in range(nk1):
                try:
                    isi_kolom1 = int(input(f"Silahkan input baris {i+1} kolom {j+1} : "))
                    simpan_kolom1.append(isi_kolom1)
                except ValueError:
                    print("Inputan anda salah. Silahkan input ulang\n")
                    continue
                m1.append(simpan_kolom1)
            
            print("\nSilahkan Input Data Matriks 2")
            for i in range(nb1):
                simpan_kolom2 =[]
                for j in range(nk1):
                    try:
                        isi_kolom2 = int(input(f"Silahkan input baris {i+1} kolom {j+1} : "))
                        simpan_kolom2.append(isi_kolom2)
                    except ValueError:
                        print("Inputan anda salah. Silahkan input ulang\n")
                        continue
                m2.append(simpan_kolom2)

            hasil_pengurangan = []
            for i in range(nb1):
                barishasil1 = []
                for j in range(nk1):
                    barishasil1.append(m1[i][j] - m2[i][j])
                hasil_pengurangan.append(barishasil1)
            print(f"Hasil pengurangan matriks adalah : ")
            for row in hasil_pengurangan:
                print(row)
    # MENU 3 #
    elif pilihan == 3:
        print("\nSilahkan Input Data Matriks 1")
        # INPUT BARIS #
        while True:
            try:
                nb1 = int(input("Silahkan Input Banyak Baris (Maksimal 4) : "))
            except ValueError:
                print("Inputan anda salah. Silahkan input ulang.")
                continue

            if 0 < nb1 < 5:
                break
            else:
                print("Tolong input dalam batas.\n")


    
    else:
        break
    
    break

print(m1, m2)