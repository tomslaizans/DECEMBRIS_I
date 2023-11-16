#lietotaja cipars
cipars=int(input("Ievadi ciparu, kurš ir vismaz 1:"))

#parbauda vai ir vismaz 1
while cipars <= 0:
    print("Ievieto ciparu, kas ir vismaz 1")
    cipars=int(input("Tagad ievadi ciparu, kurš ir vismaz 1:"))

#Skaita
for vismaz_viens in range(1, cipars+1):
    print(vismaz_viens)