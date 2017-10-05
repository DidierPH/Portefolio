
def standaardprijs(km):
    a = 0
    if km < 0:
        km = 0

    if km < 50:
        a = km *0.80
    else : km > 50
    a = 15 + (km+0.60)
    return a


def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    kinderen = leeftijd < 12
    ouderen = leeftijd >= 65
    if (kinderen or ouderen) and weekendrit == False:
        return prijs * 0.7
    elif (kinderen or ouderen) and weekendrit:
        return prijs * 0.65
    elif (kinderen or ouderen) == False and weekendrit == False:
        return prijs
    else:  # (kinderen == False and ouderen == False) and weekendrit
        return prijs * 0.6
print (ritprijs(12,False ,20))
