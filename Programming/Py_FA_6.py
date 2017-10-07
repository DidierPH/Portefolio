maxKluizen = 12

def kluizen_lijst[1,2,3,4,5,6,7,8,9,10,11,12]

def lees_kluizen():
    print("lees_kluizen")
    bestand = open("kluizen.txt","r")
    regels = bestand.readlines()
    kluizen ={}
    for regel in regels:
        kluis = regel.strip(l.split('.')
        kluizen.append(int(kluis[0]), kluis[1])
    bestand.close()
    return kluizen

def schrijf_kluizen(kluizen):
    print("schrijf_bestand")


def geef_wachtwoord():
    return input("geef wachtwoord: ")

def zoek_kluis(kluizen,kluisnummer):
    for kluis in kluizen:
        if kluis[0] == kluisnummer:
            return kluis
        return
def kluis_opnenen(kluis_nr):
    kluis_nr = eval(input("uw kluisnummer: "))



def nieuwe_kluis():
    lees_kluizen()


def toon_aantal_kluizen_vrij():

def kluis_teruggeven():
    print ("kluis_teruggeven doe ik niet!")

while True:
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: ik wil een nieuwe kluis")
    print("3: ik wil iets uit mijn kluis halen")
    print("4: ik geef mijn kluis terug")

    keuze = eval(input("Uw keuze: "))
    if keuze == 1:
        toon_aantal_kluizen_vrij()
    elif keuze == 2:
        nieuwe_kluis()
    elif keuze == 3:
        kluis_opnenen()
    elif keuze == 4:
        kluis_teruggeven()

