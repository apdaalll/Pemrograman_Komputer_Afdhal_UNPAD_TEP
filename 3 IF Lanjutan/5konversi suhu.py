#PROGRAM KONVERSI SUHU

# suhu_awal = float(input("masukkan nilai suhunya:"))
# satuan_awal = input("1. Celcius (C)\n2. Fahrenheit (F)\n3. Kelvin (K)\n4. Reamurr (R)\npilih satuan awalnya: ").upper
# satuan_tujuan = input("1. Celcius (C)\n2. Fahrenheit (F)\n3. Kelvin (K)\n4. Reamurr (R)\npilih satuan tujuannya: ").upper

# if satuan awal == "C":
#     print("kamu akan mengkonversi suhu C")

import random

print("=== PROGRAM KONVERSI SUHU ===")
print("Satuan yang diakomodasi: C, F, K, R")

# 1 & 2. Input Satuan Awal
satuan_awal = input("Masukkan satuan awal (C/F/K/R): ").strip().upper()

# 3. Nilai suhu awal acak (1-1000)
suhu_awal = random.randint(1, 1000)
print(f"Nilai suhu awal: {suhu_awal}")

# 4. Input Satuan Tujuan
satuan_tujuan = input("Masukkan satuan tujuan (C/F/K/R): ").strip().upper()

# Daftar pilihan yang valid
satuan_suhu = ['C', 'F', 'K', 'R']

# 7.iii Antisipasi jika pilihan di luar C, F, K, R
if satuan_awal not in satuan_suhu or satuan_tujuan not in satuan_suhu:
    print("Pilihan satuan tidak valid! Gunakan hanya C, F, K, atau R.")

# 7.ii Antisipasi jika satuan awal sama dengan tujuan
elif satuan_awal == satuan_tujuan:
    print("Satuan awal dan tujuan sama! Tidak ada perhitungan konversi yang dilakukan.")
    print(f"\nHasil: Konversi suhu dari {suhu_awal} °{satuan_awal} ke °{satuan_tujuan} adalah {suhu_awal:.2f}")

# 5. Proses konversi
else:
    # --- KONVERSI DARI CELSIUS (C) ---
    if satuan_awal == 'C' and satuan_tujuan == 'F':
        hasil = (suhu_awal * 9/5) + 32
    elif satuan_awal == 'C' and satuan_tujuan == 'K':
        hasil = suhu_awal + 273
    elif satuan_awal == 'C' and satuan_tujuan == 'R':
        hasil = (suhu_awal * 9/5) + 492

    # --- KONVERSI DARI FAHRENHEIT (F) ---
    elif satuan_awal == 'F' and satuan_tujuan == 'C':
        hasil = (suhu_awal - 32) * 5/9
    elif satuan_awal == 'F' and satuan_tujuan == 'K':
        hasil = ((suhu_awal - 32) * 5/9) + 273
    elif satuan_awal == 'F' and satuan_tujuan == 'R':
        hasil = suhu_awal + 460

    # --- KONVERSI DARI KELVIN (K) ---
    elif satuan_awal == 'K' and satuan_tujuan == 'C':
        hasil = suhu_awal - 273
    elif satuan_awal == 'K' and satuan_tujuan == 'F':
        hasil = ((suhu_awal - 273) * 9/5) + 32
    elif satuan_awal == 'K' and satuan_tujuan == 'R':
        hasil = suhu_awal * 9/5

    # --- KONVERSI DARI RANKINE (R) ---
    elif satuan_awal == 'R' and satuan_tujuan == 'C':
        hasil = (suhu_awal - 492) * 5/9
    elif satuan_awal == 'R' and satuan_tujuan == 'F':
        hasil = suhu_awal - 460
    elif satuan_awal == 'R' and satuan_tujuan == 'K':
        hasil = suhu_awal * 5/9

    # 6. Tampilkan hasil
    print(f"\nHasil: Konversi suhu dari {suhu_awal} °{satuan_awal} ke °{satuan_tujuan} adalah {hasil:.2f}")