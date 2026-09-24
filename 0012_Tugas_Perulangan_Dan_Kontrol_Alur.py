print ("--- Bilangan Genap ---/n")
for i in range (0, 51):
    if i % 2 == 0:
        print (i, end=" ")
print ("akhiri dari program\n")

print ("--- Bilangan Prima ---/n")
for angka in range (0,101):
    prima = True
    for pembagi in range (2, angka):
        if angka % pembagi == 0:
            prima = False
            break
    if prima:
        print (angka, end = " ")
print ("akhiri dari program\n")