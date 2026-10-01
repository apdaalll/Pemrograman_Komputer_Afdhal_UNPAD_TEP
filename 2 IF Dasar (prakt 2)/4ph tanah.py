#bismillah program 4
#nama: Afdhal Ahmad Dzikri      

ph=float(input("masukin nilai ph: "))

if ph < 1 or ph > 14:
    print("bukan nilai ph")
elif ph < 4.5:
    print("sangat masam")
elif ph <= 5.5:
    print("masam")
elif ph <= 6.5:
    print("agak masam")
elif ph <= 7.5:
    print("netral")
elif ph <= 8.5:
    print("agak alkalis")
else:
    print("alkalis")