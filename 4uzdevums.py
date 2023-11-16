#cipars
cipars=int(input("Ievadi ciparu:"))
#faktoriāla sākums aka 1
faktorials=1

#faktoriala reizinasana
for reizes in range(1, cipars+1):
    faktorials=faktorials*reizes

print(f"Faktoriāls{cipars} ir: {faktorials}")