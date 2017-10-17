import xmltodict
def procesXML(stations):
    with open(stations) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

stationsdict = procesXML('stations.xml')
stations = stationsdict['Stations']['Station']

print("dit zijn de codes en types van de "+ str(len(stations))+" stations")

for station in stations:
    print(station['Code'] + "-" + (station['Type']))

print("Dit zijn alle stations met één of meer synoniemen: ")
for station in stations:
    if station["Synoniemen"] == None:
        break
    print(station["Code"] , "-" , station["Synoniemen"])

print("Dit is de lange naam van elk station:")
for station in stations:
    print(station["Code"] + "-" + station["Namen"]["Lang"])


name_of_first_station = stations[0]['Namen']
shortname_of_second_station = stations[1] ['Namen'] ['Kort']


