#NAMA : Afdhal Ahmad Dzikri
#NPM : 240110250041
#KELAS : A2 pemkom 
#univ: Universitas Padjadjaran

#DATA BOOLEAN
a= True
b= False
print(a)
print(b)
#output: True
#output: False

#DATA STRING
c = "Kang james ganteng bismillah dapet A"
d = ", pelis kang"
data_string = c + d
print(data_string)
#output: Kang james ganteng bismillah dapet A, pelis kang

#DATA INTEGER ATAU BULAT
e = 10
f = 50
int= e + f
print(int)
#output: 60

#DATA FLOAT, MENGAMBANG, atau DESIMAL
g = 10.5
h = 5.5
float = g + h
print(float)
#output: 16.0

#TIPE DATA LIST
i = [1, 2, 3, 4, 5]
i[0]= 10
print(i)
#output: [10, 2, 3, 4, 5]

buah = ["buah wesya", "buah ben", "buah gema"]
buah[0] = "buah wesya ganteng"
print(buah)
print(buah[0])
print(buah[1])
print(buah[2])
print(buah[1:3])
#output buah: ['buah wesya ganteng', 'buah ben', 'buah gema']
#output buah[0]: buah wesya ganteng
#output buah[1:3]: ['buah ben', 'buah gema'], * memotong jadi dimulai dari indeks 1 sampai indeks 2, batas 3

#TIPE DATA TUPLE
pa_mimin = ("pa mimin ganteng", 3.14, 5, False, True, 'pa mimin baik')
print(pa_mimin)
print(pa_mimin[0])
 #output sama permisalannya kayak data list, tapi tuple ga bisa diubah
 #tuple biasa ada seperti di titik koordinat peta

#TIPE DATA DICTIONARY
kamus_muslim = {1: "bismillah", 2: "allahuakbar", 3: "anjay"}
print(kamus_muslim[1] + " " + "hirohim")
#output: bismillah hirohim

print(kamus_muslim[3])
#output: anjay
    
#PENGUBAHAN INT KE FLOAT
nama_asprak = "james theo"
umur_asprak = (float("25"))
#output: 25.0
umur_kangjames = (int("20"))
#output: 20
#string ga bisa diubah jadi integer, tapi integer bisa diubah jadi string

