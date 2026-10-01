nilai=int(input("Pilih operasi aritmatik yang akan dijalankan\n1. Penghitungan luas\n2. Penghitungan Volume\n Masukkan kode angka: "))

if nilai == 1:
    print("kamu bakal melakukan penghitungan luas")
    panjang=float(input("masukkan nilai panjang: "))
    lebar=float(input("masukan nilai lebar: "))
    luas=panjang*lebar
    print(f"luas bidangnya itu= {luas}")
elif nilai == 2:
    print("maneh bakal lakuin penghitungan volume")
    panjang=float(input("masukkan nilai panjangnya: "))
    lebar=float(input("masukan nilai lebarnya: "))
    tinggi=float(input("masukan nilai tingginya: "))
    volumenya=panjang*lebar*tinggi
    print(f"volume bidang tersebut= {volumenya}")
else: 
    print("salah kodenya woi")  