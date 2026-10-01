#PROGRAM 3: PENENTUAN JENIS TANAMAN
#Nama: Afdhal Ahmad Dzikri
#NPM: 240110250041 A2 PEMKOM


jenis_tanah = input("jenis tanah adalah: ")
kondisi_iklim = input("kondisi iklim: ")

if jenis_tanah == "lempung":
    if kondisi_iklim == "cukup lembap":
        print("cocok untuk menanam padi")
    else:
        print("ga cocok tanem pdi")
elif jenis_tanah == "pasir":
    if kondisi_iklim == "panas":
        print("cocok untuk tanam jagung")
    else:
        print("ga cocok tanem jgung")
elif jenis_tanah == "tanah liat":
    if kondisi_iklim == "sedang":
        print("cocok untuk tanam sayur")
    else:
        print("ga cocok buat tanem syur")
else:
    print("tanah apaan dah")