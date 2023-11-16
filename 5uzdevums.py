#uzzinat laiku
laiks=float(input("Ievadi laiku:"))

#pateikt cik šobrīd ir pulkstens
pulkstens=int(laiks)

#izdomat vai ir rīts, diena vai vakars
if pulkstens in range(6, 12):
    print("Labrīt")
elif pulkstens in range(12, 19):
    print("Labdien")
elif pulkstens in range(19, 24):
        print("Labvakar")
else:
    print("Šitāds laiks nepastāv ;)")