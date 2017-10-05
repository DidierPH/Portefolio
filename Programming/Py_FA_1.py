
def standaardprijs(km):
    a = 0
    if km < 0:
        km = 0

    elif km < 50:
        a = km *0.80
    else :
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

print (ritprijs(11, False, 20))
print (ritprijs(12, False, 20))
print (ritprijs(64, False, 20))
print (ritprijs(65, False, 20))

print (ritprijs(11, True, 20))
print (ritprijs(12, True, 20))
print (ritprijs(64, True, 20))
print (ritprijs(65, True, 20))

print (ritprijs(11, False, 60))
print (ritprijs(12, False, 60))
print (ritprijs(64, False, 60))
print (ritprijs(65, False, 60))

print (ritprijs(11, True, 60))
print (ritprijs(12, True, 60))
print (ritprijs(64, True, 60))
print (ritprijs(65, True, 60))



