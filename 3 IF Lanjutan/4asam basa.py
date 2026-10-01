#PROGRAM 4 ATAU 5: PROGRAM PENGUJIAN ASAM BASA LARUTAN (KERJAKAN UNTUK LAPORAN)
#Nama: Afdhal Ahmad Dzikri
#NPM: 240110250041

lakmus_merah = input("lakmus merah: ")
lakmus_biru = input("lakmus biru: ")

if lakmus_merah == "merah":
    if lakmus_biru == "merah":
        print ("sifat larutannya asam")
    elif lakmus_biru == "biru":
        print("sifat larutan netral")
    else:
        print("lakmus birunya yang bener lah")
elif lakmus_merah == "biru":
    if lakmus_biru == "biru":
        print("larutannya basa")
    else:
        print("lakmus biru nya ga jelas")
else:
    print("apaan dah")


#output merah, biru: netral
#output merah, merah: asam
#output biru, biru: basa
#output biru, merah: birunya ga jelas
#output ngawur, ...: apaan dah