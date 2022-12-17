
def valaszto():
    valasztas=int(input('Válaszd ki kineke a nevében dobsz: 1-saját , 2-Teremtmény: '))
    while not (valasztas >= 1 and valasztas <= 2):
        valasztas = int(input("Nem jó választás, kérem adja meg újra! 1-saját , 2-Teremtmény: "))
    if valasztas==1:
        print(f"Az Ön a saját nevében dob !")
    else:
        print(f"Az Ön a Teremtmény nevében dob !")

valaszto()


ugyesseg=futatto.osszead(1,6)
print(f"Ugyességi pontod: {ugyesseg}")
eletero=futatto.osszead(2,12)
print(f"Életerőd: {eletero}")
szerencse=futatto.osszead(1,6)
print(f"Szerencséd:  {szerencse}")
