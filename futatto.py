import random
#jatékos adatai
jatekos_ugyesseg=0
jatekos_eletero=0
jatekos_szerencse=0

#teremtmény adatai

teremtmeny_ugyesseg=0
teremtmeny_eletero=0
teremtmeny_szerencse=0




def dobas(dobasok_szama): #legenerálom a dobásokat
    i=0
    dobott_szam=[]
    while i<dobasok_szama:
        vel = int(random.random() * 5) + 1
        dobott_szam.append(vel)
#        print(dobott_szam)
        i+=1
    #    print(dobott_szam)
    return dobott_szam

def osszead(dobasok_szama,kezdo_ertek): #hozzáadja a dobásokat a megadott értékhez
    dobasok=dobas(dobasok_szama)
    i = 0
    ossz = kezdo_ertek
    while i < len(dobasok):
        ossz += dobasok[i]
        i += 1
    #print(ossz)
    return ossz

def valaszto(oldal_szam):
    if oldal_szam == 1:
        valasztas = int(input('Kiszeretnéd nyitni? 1-igen 2-nem: '))
    elif oldal_szam == 56:
        valasztas = int(input('Át mászol rajta? 1-igen 2-nem: '))
    elif oldal_szam == (66 or 270):
        valasztas = int(input(' Keletre mész? 1-igen 2-nem, Nyugatra: '))
    while not (oldal_szam >= 1 and oldal_szam <= 2):
        if oldal_szam == 1:
            valasztas = int(input('Kiszeretnéd nyitni? 1-igen 2-nem: '))
        elif oldal_szam == 56:
            valasztas = int(input('Át mászol rajta? 1-igen 2-nem: '))
        elif oldal_szam == (66 or 270):
            valasztas = int(input(' Keletre mész? 1-igen 2-nem: '))




def eroosszemeres(sajat_ero,termtmeny_ereje):               #Csata kimenetelétől függően adott pontra lépés
    lepes=0
    if termtmeny_ereje<sajat_ero:
        lepes=4
        return lepes
    elif sajat_ero< termtmeny_ereje:
        lepes=5
        return lepes
    elif sajat_ero==termtmeny_ereje:
        lepes=1
        return lepes

def szerencse():        #ha szerencsés volt a játékos 1-true, 0-false
    szerencse_osszege=0
    szerencse_osszege=osszead(2,0)
    if szerencse_osszege<szerencse:
        return 1
    else:
        return 0

def kiir():
    a='Üdvözöllek a halál labirintusban!!!'
    print(a.upper())
    print('Egy versenyre nevezel, aminek a lényege, hogy át kell kelni a halállabirintuson. '
          'A labirintusban tárgyakat találhatsz és szörnyekkel kell harcoljál.')

def beker():
    jatokos_neve=str(input('Kérlek add meg a neved: '))
    return jatokos_neve

def elsoo():
    kiir()
    valaszto(1)
    print('Miután öt percet haladtál lassan az alagútban, egy kőasztalhoz érsz, amely a bal oldali fal mellett áll. Hat doboz van rajta, egyikükre a te neved festették. '
          'Ha ki akarod nyitni a dobozt?')
    kinyit=input('Kérlek válassz ki nyitod I-igen, N-nem: ' )
    if kinyit.upper()=='I':
        ketszazhetven()
    else:
        hatvanhat()



def otvenhat():
    print('Látod, hogy az akadály egy széles, barna, sziklaszerű tárgy. '
          'Megérinted, és meglepve tapasztalod, hogy lágy, szivacsszerű. ')
    kiir(56)
def hatvanhat():
    print('Néhány perc gyaloglás után egy elágazáshoz érsz az'
          ' alagútban. Egy, a falra festett fehér nyíl nyugatfelé mutat. A földön nedves lábnyomok jelzik, merre haladtak '
          'az előtted járók. Nehéz biztosan megmondani, de úgy tűnik, hogy három közülük a nyíl irányába halad, míg '
          'egyikük úgy döntött, hogy keletnek megy. ')
    kiir(66)

def szazharminchet():
    print('Ahogy végigmész az alagúton, csodálkozva látod, hogy egy jókora vasharang csüng alá a boltozatról.')


def ketszaztizenot():
    print('Kardod könnyedén áthatol a spóragolyó vékonykülső burkán. Sűrű barna spórafelhő csap ki a golyóból, '
          'és körülvesz. Némelyik spóra a bőrödhöz tapad, és rettenetes viszketést okoz. Nagy daganatok nőnek '
          'az arcodon és karodon, és a bőröd mintha égne. 2 ÉLETERŐ pontot veszítesz. Vadul vakarózva átléped '
          'a leeresztett golyót, és keletnek veszed az utad.')

def ketszazhetven():
    print(
        'A doboz teteje könnyedén nyílik. Benne két aranypénzt találsz, és egy üzenetet, amely egy kis pergamenen neked szól. '
        'Előbb zsebre vágod az aranyakat, aztán elolvasod az üzenetet: - „Jól tetted. Legalább volt annyi eszed, '
        'hogy megállj és elfogadd az ajándékot. Most azt tanácsolom neked, hogy keress és használj különféle tárgyakat, ha sikerrel '
        'akarsz áthaladni Halállabirintusomon.” Az aláírás Szukumvit. '
        'Megjegyzed a tanácsot, apró darabokra téped a pergament, és tovább mész észak felé')


def ketszazkilencvenharom():
    print('A három pár nedves lábnyomot követve az alagút nyugati elágazásában hamarosan'
          ' egy újabb el-ágazáshoz érsz. Ha továbbmész nyugat felé a lábnyomokat követve')


def haromhetvenharom():
    print('Fölmászol a lágy sziklára, attól tartasz, hogy bár-melyik pillanatban elnyelhet.'
          ' Nehéz átvergődni rajta, mert puha anyagában alig tudod a lábadat emelni, de végül '
          'átvergődsz rajta. Megkönnyebbülten érsz újra szilárd talajra, és fordulsz kelet felé.')

def haromnyolcvanhet():
    print('Hallod, hogy elölről súlyos lépések közelednek. Egy széles, állatbőrökbe öltözött, kőbaltás, primitív lény '
          'lép elő. Ahogy meglát, morog, a földre köp, majd a kőbaltát felemelve közeledik, és mindennek kinéz, '
          'csak barátságosnak nem. Előhúzod kardodat, és felkészülsz, hogy megküzdj a Barlangi Emberrel.')
