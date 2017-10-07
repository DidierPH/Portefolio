def inlezen_beginstation(stationa) :
    print("Vul uw beginstation in : ")

def inlezen_eindstation(stations, beginstation) :
    print("vul uw eindstation in : ")

def omroepen_reis(stations, beginstation, eindstation) :
    print()

stations = ['Schagen,Heerhugowaard,Alkmaar,Castricum,Zaandam,Amsterdam,Sloterdijk,Amsterdam Centraal,Amsterdam Amstel,UtrechtCentraal,s-Hertogenbosch,Eindhoven,Weert,Roermond,Sittard,Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
