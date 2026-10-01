#PROGRAM 1: PROGRAM EVALUASI KUALITAS BIJI PADI
#Nama: Afdhal Ahmad Dzikri
#NPM: 240110250041
#shift A2 Pemrograman Komputer

import random as wesya
#INI PAKE INPUT KAYAK PRAKTIKUM KEMARIN ATAU PRAKTIKUM KEDUA

# tingkat_kematangan = float(input("masukkan tingkat kematangan biji padi (%): "))
# kadar_air = float(input("masukin kadar air biji padi (%): "))

#INI PAKE RENTANG DARI 0 KE 100

# tingkat_kematangan = wesya.randint (0, 100)
# kadar_air = wesya.randint (0, 100)
# print(tingkat_kematangan, kadar_air)

#INI PAKE ROUND ATAU PEMBULATAN

tingkat_kematangan = wesya.random() * 100
kadar_air = wesya.random () * 100
tingkat_kematangan = round(tingkat_kematangan, 1)
kadar_air = round(kadar_air, 1)
print(tingkat_kematangan, kadar_air)

if tingkat_kematangan < 80:
    if kadar_air > 14:
        print("biji padi sangat tak layak dijual\nrugi")
    else:
        print("biji padi tidak layak untuk dijual\nyahh satu")
else:
    if kadar_air > 14:
        print("biji padi tidak layak untuk dijual\n yahhh")
    else:
        print("biji padi layak untuk dijual\n oke pak")

