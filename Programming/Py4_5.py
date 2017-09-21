def kwadraten_som(grondgetallen):
    som=1,5,3,4
    for som in grondgetallen :
        if som > 0 :
         kwadraat=som**2
        som=som+kwadraat
        return som
grondgetallen = 1,5,4,3
print(kwadraten_som(grondgetallen))
