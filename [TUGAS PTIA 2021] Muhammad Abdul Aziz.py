while(True):
    print("===============================")
    print("PETROLEUM PROPERTIES CALCULATOR")
    print("===============================") 
    print("1. Porositas\n2. Saturasi (Sw,So,Sg)\n3. Densitas"
    "\n4. Specific Gravity (SG)\n5. Derajat API\n6. Viskositas"
    "\n7. Permeabilitas\n8. Exit\n\nApa yang ingin Anda cari?")

    pilihan = float(input("Masukkan pilihan Anda (1/2/3/4/5/6/7/8): "))
    if pilihan == 1:
        print("\nOke, kita akan mencari nilai porositas")
        pore = float(input("Masukkan nilai pore volume (dalam cc): "))
        bulk = float(input("Masukkan nilai bulk volume (dalam cc): "))
        porositas = pore / bulk
        porpersen = porositas*100
        print("\nNilai porositas = ", porositas, "atau", porpersen,"%")
        print()

    elif pilihan == 2:
        while(True):
            print("\nOke, kita akan mencari nilai saturasi gas, air, dan minyak")
            print("Sebelumnya, Anda ingin mencari nilai saturasi apa?"
                "\n1. Saturasi Air (Sw)\n2. Saturasi Minyak (So)\n3. Saturasi Gas (Sg)"
                "\n4. Ketiganya\n5. Menu")
            pilihan2 = float(input("Masukkan pilihan Anda (1/2/3/4/5): "))
            print()
            if pilihan2 == 1:
                poriair = float(input("Masukkan volume pori yang terisi air (dalam cc): "))
                poritotal = float(input("Masukkan volume pori total (dalam cc): "))
                sw = poriair / poritotal
                print("\nNilai saturasi air (Sw) = ", sw)
                print()
            elif pilihan2 == 2:
                poriminyak = float(input("Masukkan volume pori yang terisi minyak (dalam cc): "))
                poritotal = float(input("Masukkan volume pori total (dalam cc): "))
                so = poriminyak / poritotal
                print("\nNilai saturasi minyak (Sw) = ", so)
                print()
            elif pilihan2 == 3:
                porigas = float(input("Masukkan volume pori yang terisi gas (dalam cc): "))
                poritotal = float(input("Masukkan volume pori total (dalam cc): "))
                sg = porigas / poritotal
                print("\nNilai saturasi gas (Sg) = ", sg)
                print()
            elif pilihan2 == 4:
                poriair = float(input("Masukkan volume pori yang terisi air (dalam cc): "))
                poriminyak = float(input("Masukkan volume pori yang terisi minyak (dalam cc): "))
                porigas = float(input("Masukkan volume pori yang terisi gas (dalam cc): "))
                sw = poriair / (poriair + poriminyak + porigas)
                so = poriminyak / (poriair + poriminyak + porigas)
                sg = porigas / (poriair + poriminyak + porigas)
                print("\nNilai saturasi air    =", sw,
                      "\nNilai saturasi minyak =", so, 
                      "\nNilai saturasi gas    =", sg)
                print()
            elif pilihan2 == 5:
                break
            else:
                print("\nInput yang Anda masukkan salah, silahkan pilih angka 1 sampai 5")
                continue
                
    elif pilihan == 3:
        print("\nOke, kita akan mencari nilai densitas")
        massa = float(input("Masukkan massa fluida (dalam gram): "))
        volume = float(input("Masukkan volume fluida (dalam cc): "))
        densitas = massa / volume
        print("\nNilai densitas = ", densitas, "gram/cc")
        print()

    elif pilihan == 4:
        print("\nOke, kita akan mencari nilai specific gravity (SG)")
        denfluidatentu = float(input("Masukkan nilai densitas fluida (dalam gram/cc): "))
        denfluidastandar = float(input("Masukkan nilai densitas fluida standar (dalam gram/cc): "))
        sgravity = denfluidatentu / denfluidastandar
        print("\nNilai specific gravity = ", sgravity)
        print()

    elif pilihan == 5:
        print("\nOke, kita akan mencari nilai derajat API")
        sgravity = float(input("Masukkan nilai SG: "))
        api = (141.5 / sgravity) - 131.5
        print("\nNilai derajat API = ", api)
        print()

    elif pilihan == 6:
        while(True):
            print("\nOke, kita akan mencari nilai viskositas dinamis dan kinematis")
            print("Sebelumnya, Anda ingin mencari nilai viskositas apa?"
                  "\n1. Viskositas Kinematis\n2. Viskositas Dinamis\n3. Keduanya"
                  "\n4. Menu")
            pilihan3 = float(input("Masukkan pilihan Anda (1/2/3/4): "))
            print()
            if pilihan3 == 1:
                konstantaalat = float(input("Masukkan nilai konstanta alat: "))
                waktuvisko = float(input("Masukkan waktu yang dibutuhkan (dalam sekon): "))
                viskokinematis = konstantaalat * waktuvisko
                print("\nNilai viskositas kinematis = ", viskokinematis, "centistoke")
                print()
            elif pilihan3 == 2:
                viskokinematis = float(input("Masukkan nilai viskositas kinemtis (dalam centistoke): "))
                densitas = float(input("Masukkan nilai densitas: "))
                viskodinamis = viskokinematis * densitas
                print("\nNilai viskositas dinamis = ", viskodinamis, "centipoise")
                print()
            elif pilihan3 == 3:
                konstantaalat = float(input("Masukkan konstanta alat: "))
                waktuvisko = float(input("Masukkan waktu yang dibutuhkan (dalam sekon): "))
                densitas = float(input("Masukkan nilai densitas (dalam gram/cc): "))
                viskokinematis = konstantaalat * waktuvisko
                viskodinamis = viskokinematis * densitas
                print("\nNilai viskositas kinematis =", viskokinematis, "centistoke"
                      "\nNilai viskositas dinamis   =", viskodinamis, "centipoise")
                print()
            elif pilihan3 == 4:
                break
            else:
                print("\nInput yang Anda masukkan salah, silahkan pilih angka 1 sampai 4")
                continue

    elif pilihan == 7:
        print("\nOke, kita akan mencari nilai permeabilitas")
        viskositas = float(input("Masukkan nilai viskositas (dalam centipoise): "))
        lajualir = float(input("Masukkan nilai laju alir (dalam cc/detik): "))
        panjangsampel = float(input("Masukkan nilai panjang sampel (dalam cm): "))
        upstream = float(input("Masukkan nilai tekanan masuk/upstream (dalam atma): "))
        downstream = float(input("Masukkan nilai tekanan keluar/downstream (dalam atma): "))
        time = float(input("Masukkan waktu yang dibutuhkan (dalam sekon): "))
        luaspermukaan = float(input("Masukkan nilai luas permukaan (dalam cm kuadrat): "))
        permeabilitas = viskositas * lajualir * panjangsampel / (luaspermukaan * (upstream - downstream) * time)
        print("\nNilai permeabilitas = ", permeabilitas, "Darcy")
        print()
    elif pilihan == 8:
        break
    else:
        print("\nInput yang Anda masukkan salah, silahkan pilih angka 1 sampai 8\n")
        continue
        
print("\n==============================================================")
print("Terima kasih telah menggunakan Petroleum Properties Calculator")
print("==============================================================")