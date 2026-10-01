#PROGRAM 1: PROGRAM EVALUASI KUALITAS BIJI PADI
#Nama: Afdhal Ahmad Dzikri]
#NPM: 240110250041
#shift A2 Pemrograman Komputer

import random as wesya

tingkat_kematangan = float(input("masukkan tingkat kematangan biji padi (%): "))
kadar_air = float(input("masukin kadar air biji padi (%): "))

if tingkat_kematangan < 80:
    if kadar_air > 14:
        print("biji padi sangat tak layak dijual")
    else:
        print("biji padi tidak layar untuk dijual")
else:
    if kadar_air > 14:
        print("biji padi sangat tak layak dijuall")
    else:
        print("biji padi tak layak untuk dijuall")

