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

    # MENU 1 : OPERASI PENJUMLAHAN MATRIKS#    
    if pilihan == 1:
        print("\nMelakukan Operasi Penjumlahan")
        print("Silahkan Input Data Matriks 1")
        while True:
            try :
                nb1 = int(input("Silahkan Input Banyak Baris (Maksimal 4): "))
            except ValueError:
                print("Inputan anda salah. Silahkan input ulang.\n")
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
            baris_hasil_penjumlahan = []
            for j in range(nk1):
                baris_hasil_penjumlahan.append(m1[i][j] + m2[i][j])
            hasil_penjumlahan.append(baris_hasil_penjumlahan)
        print(f"Hasil penjumlahan matriks adalah : ")
        for row in hasil_penjumlahan:
            print(row)

    # MENU 2 : OPERASI PENGURANGAN MATRIKS#  
    elif pilihan == 2:
        print("\nMelakukan Operasi Pengurangan")
        print("Silahkan Input Data Matriks 1")
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
                baris_hasil_pengurangan = []
                for j in range(nk1):
                    baris_hasil_pengurangan.append(m1[i][j] - m2[i][j])
                hasil_pengurangan.append(baris_hasil_pengurangan)
            print(f"Hasil pengurangan matriks adalah : ")
            for row in hasil_pengurangan:
                print(row)

    # MENU 3 : OPERASI PERKALIAN MATRIKS #
    elif pilihan == 3:
        print("\nMelakukan Operasi Perkalian")

        # INPUT DATA MATRIKS MATRIKS 1 #
        print("Silahkan Input Data Matriks 1")
        # INPUT n BARIS #
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

        # INPUT n KOLOM MATRIKS 1#
        while True:
            try:
                nk1 = int(input("Silahkan Input Banyak Kolom (Maksmal 4) : "))
            except ValueError:
                continue

            if 0 < nk1 < 5:
                break
            else:
                print ("Tolong input dalam batas.\n")

        # INPUT BARIS DAN KOLOM MATRIKS 1#
        for i in range(nb1):
            simpan_kolom1 = []
            for j in range(nk1):
                try:
                    isi_kolom1 = int(input(f"Silahkan input baris {i+1} kolom {j+1} : "))
                    simpan_kolom1.append(isi_kolom1)
                except ValueError:
                    print("Inputan anda salah. Silahkan input ulang.")
                    continue
            m1.append(simpan_kolom1)

        # INPUT DATA MATRIKS 2#
        print("\nSilahkan Input Data Matriks 2")
        while True:
            #INPUT N BARIS MATRIKS 2#
            while True:
                try:
                    nb2 = int(input("Silahkan Input Banyak Baris (Maksimal 4) : "))
                except ValueError:
                    print("Inputan anda salah. Silahkan input ulang.")
                    continue

                if 0 < nb2 < 5:
                    break
                else:
                    print("Tolong input dalam batas.\n")
            

            #INPUT N KOLOM MATRIKS 2#
            while True:
                try:
                    nk2 = int(input("Silahkan Input Banyak Kolom (Maksimal 4 : "))
                except ValueError:
                    continue

                if 0 < nk2 < 5:
                    break
                else:
                    print ("Tolong input dalam batas.\n")
            
            if nb2 == nk1 or nk2 == nb1:
                break
            else:
                print("Pastikan banyak BARIS di MATRIKS 1 sama dengan banyak KOLOM di MATRIKS 2 atau sebaliknya.")
                print(f"Banyak baris anda di Matriks 1 : {nb1}")
                print(f"Banyak kolom anda di Matriks 1 : {nk1}")
        
        # INPUT BARIS DAN KOLOM MATRIKS 2#
        for i in range(nb2):
            simpan_kolom2 = []
            for j in range(nk2):
                try:
                    isi_kolom2 = int(input(f"Silahkan input baris {i +1} kolom {j+1} : "))
                    simpan_kolom2.append(isi_kolom2)
                except ValueError:
                    print("Inputan anda salah. Silahkan input ulang.")
                    continue
            m2.append(simpan_kolom2)
        
        # PROSES PERKALIAN #
        hasil_perkalian = [[0] * nb2 for _ in range(nk1)]
        for i in range(nb1):
            for j in range(nk2):
                for k in range(nk1):
                    hasil_perkalian[i][j] += m1[i][k] * m2[k][j]
        
        # HASIL OPERASI #
        print("Hasil Perkalian Matriks:")
        for row in hasil_perkalian:
            print(row)


    # MENU 4 : DETERMINANT MATRIKS#
    elif pilihan == 4:
        hasil_determinant =[]
        print("\nMelakukan Operasi Determinant Matriks")
        print ("Menu Determinant Matriks")
        print ("1. Determinant Matriks 2x2")
        print ("2. Determinant Matriks 3x3")
        print ("3. Determinant Matriks 4x4")
    
        while True:
            try :
                pilih_det = int(input("Silahkan Pilih Menu Deterimanant Matriks : "))
            except ValueError:
                print ("Inputan anda salah. Silahkan input ulang.\n")

            if 0 < pilih_det < 3:
                break
            else:
                print("Tolong input dalam batas.\n")

        # DETERMINANT MATRIKS 2x2#
        if pilih_det == 1:
            nb1 = nk1 = 2
            
            #INPUT DATA MATRIKS#
            print("Silahkan Input Data Matriks")
            for i in range(nb1):
                simpan_kolom1 =[]
                for j in range(nk1):
                    try:
                        isi_kolom1 = int(input(f"Silahkan input baris {i+1} kolom {j+1} : "))
                        simpan_kolom1.append(isi_kolom1)
                    except ValueError:
                        print("Inputan anda salah. Silahkan input ulangn.\n")
                m1.append(simpan_kolom1)

            # PROSES DETERMINANT 2x2#
            simpan_hasil_determinant1 = (
                (m1[0][0]) * (m1[1][1]) -
                (m1[0][1]) * (m1[1][0])
            )
            hasil_determinant.append(simpan_hasil_determinant1)
            
            print("Hasil Determinant Matriks adalah :")
            for row in hasil_determinant:
                print (row)

        # DETERMINANT MATRIKS 3x3 #
        elif pilih_det == 2:
            nb1 = nk1 = 3
            
            #INPUT DATA MATRIKS 1#
            print("Silahkan Input Data Matriks")
            for i in range(nb1):
                simpan_kolom1 =[]
                for j in range(nk1):
                    try:
                        isi_kolom1 = int(input(f"Silahkan input baris {i+1} kolom {j+1} : "))
                        simpan_kolom1.append(isi_kolom1)
                    except ValueError:
                        print("Inputan anda salah. Silahkan input ulangn.\n")
                m1.append(simpan_kolom1)

            # PROSES DETERMINANT 3x3#
            simpan_hasil_determinant2 = (
                (m1[0][0]) * (m1[1][1]) * (m1[2][2]) +
                (m1[0][1]) * (m1[1][2]) * (m1[2][0]) +
                (m1[0][2]) * (m1[1][0]) * (m1[2][1]) -
                (m1[0][2]) * (m1[1][1]) * (m1[2][0]) -
                (m1[0][0]) * (m1[1][2]) * (m1[2][1]) -
                (m1[0][1]) * (m1[1][0]) * (m1[2][2])
            )
            hasil_determinant.append(simpan_hasil_determinant2)

            print("Hasil Determinant Matriks adalah :")
            for row in hasil_determinant:
                print (row)

        #DETERMINANT MATRIKS 4X4#
        elif pilih_det == 3:
            nb1 = nk1 = 4

            #INPUT DATA MATRIKS#
            print("Silahkan Input Data Matriks")
            for i in range(nb1):
                simpan_kolom1 =[]
                for j in range(nk1):
                    try:
                        isi_kolom1 = int(input(f"Silahkan input baris {i+1} kolom {j+1} : "))
                        simpan_kolom1.append(isi_kolom1)
                    except ValueError:
                        print("Inputan anda salah. Silahkan input ulangn.\n")
                m1.append(simpan_kolom1)
            
            # PROSES DETERMINANT 4x4 #
            simpan_hasil_determinant3=(
                (m1[0][0] * m1[1][1] * m1[2][2] * m1[3][3]) -
                (m1[0][1] * m1[1][2] * m1[2][3] * m1[3][0]) +
                (m1[0][2] * m1[1][3] * m1[2][0] * m1[3][1]) -
                (m1[0][3] * m1[1][0] * m1[2][1] * m1[3][2]) -
                (m1[0][0] * m1[1][3] * m1[2][2] * m1[3][1]) +
                (m1[0][1] * m1[1][0] * m1[2][3] * m1[3][2]) -
                (m1[0][2] * m1[1][1] * m1[2][0] * m1[3][3]) +
                (m1[0][3] * m1[1][2] * m1[2][1] * m1[3][0])
            )
            hasil_determinant.append(simpan_hasil_determinant3)
            
            print("Hasil Determinant Matriks adalah :")
            for row in hasil_determinant:
                print(row)

    #MENU 5 : INVERS MATRIKS#
    elif pilihan == 5:
        print("\nMelakukan Operasi Invers Matriks")
        print("Menu Invers Matriks")
        print("1. Invers Matriks 2x2")
        print("2. Invers Matriks 3x3")

        # PILIH MENU MATRIKS #
        while True:
            try :
                pilih_invers = int(input("Silahkan Pilih Menu Invers Matriks : "))
            except ValueError:
                print ("Inputan anda salah. Silahkan input ulang.\n")

            if 0 < pilih_invers < 3:
                break
            else:
                print("Tolong input dalam batas.\n")

        # INVERS MATRIKS 2x2#
        if pilih_invers == 1:
            nb1 = nk1 = 2

            #INPUT DATA MATRIKS#
            print("Silahkan Input Data Matriks")
            for i in range(nb1):
                simpan_kolom1 =[]
                for j in range(nk1):
                    try:
                        isi_kolom1 = float(input(f"Silahkan input baris {i+1} kolom {j+1} : "))
                        simpan_kolom1.append(isi_kolom1)
                    except ValueError:
                        print("Inputan anda salah. Silahkan input ulang.\n")
                m1.append(simpan_kolom1)
            
            #DETERMINANT MATRIKS 2x2#
            det = m1[0][0] * m1[1][1] - m1[0][1] *m1[1][0]
            if det == 0:
                print("Matriks ini tidak memiliki invers (determinant = 0).\n")
            else:
                pass

            #PROSES INVERS 2x2#
            hasil_invers = [
                [m1[1][1] / det, -m1[0][1] / det],
                [-m1[1][0] / det, -m1[0][0] / det]
            ]

            print("Invers Matriks:")
            for row in hasil_invers:
                print(row)

        elif pilih_invers == 2:
            nb1 = nk1 = 3

            # INPUT DATA MATRIKS #
            print("Silahkan Input Data Matriks")
            for i in range(nb1):
                simpan_kolom1 =[]
                for j in range(nk1):
                    try:
                        isi_kolom1 = float(input(f"Silahkan input baris {i+1} kolom {j+1} : "))
                        simpan_kolom1.append(isi_kolom1)
                    except ValueError:
                        print("Inputan anda salah. Silahkan input ulangn.\n")
                m1.append(simpan_kolom1)
            
            #DETERMINANT MATRIKS 3x3 #
            det = (
                (m1[0][0]) * (m1[1][1]) * (m1[2][2]) +
                (m1[0][1]) * (m1[1][2]) * (m1[2][0]) +
                (m1[0][2]) * (m1[1][0]) * (m1[2][1]) -
                (m1[0][2]) * (m1[1][1]) * (m1[2][0]) -
                (m1[0][0]) * (m1[1][2]) * (m1[2][1]) -
                (m1[0][1]) * (m1[1][0]) * (m1[2][2])
            )

            if det == 0:
                print ("Matriks ini tidak memiliki invers (determinant = 0).\n")
            else:
                print ("Maaf kode ini belum selesai dikerjakan. Harap kembali lain waktu.") 
                break

    #MENU 6 : KELUAR#
    elif pilihan == 6:        
        break
    break