import os
from datetime import datetime as DateTime

# Pfad, Dateiname usw. zu den Filmen
FilmPfad = "/Volumes/osx home/kodi2020"
Dateiname = "000_FilmListe2020.txt"


# Liste aller Unterverzeichnissen erstellen
FilmListe = os.listdir(FilmPfad)

# Apple Verzeichnis-Zeugs entfernen
FilmListe.remove(".DS_Store")


# FilmListe.sort()

with open('filmliste2020.txt', 'w') as datei:
    # datei = open(Dateiname, 'w')

    # Listen Kopf schreiben
    # print ("Anzahl Filme: " + str(len(FilmListe)))
    # print ("Uhrzeit: " + DateTime.now().strftime('%H:%M:%S'))
    # print ("-------------------------------")
    datei.write("Anzahl Filme: " + str(len(FilmListe)))
    datei.write("\rUhrzeit: " + DateTime.now().strftime('%H:%M:%S'))
    datei.write("\r-------------------------------")

    # alle Filme in der Liste zeilenweise ausgeben
    i = 1
    erstesZeichenAlt = ""

    for FilmName in FilmListe:
        erstesZeichen = FilmName[0]
        if erstesZeichen == erstesZeichenAlt:
            # print (str(i) + ": " + FilmName)
            datei.write("\r" + str(i) + ": " + FilmName)
        else:
            # print("")
            # print ("---" + erstesZeichen + " ---")
            # print (str(i) + ": " + FilmName)
            datei.write("\r" + "")
            datei.write("\r---< " + erstesZeichen + " >---")
            datei.write("\r" + str(i) + ": " + FilmName)
        erstesZeichenAlt = erstesZeichen
        i = i + 1

    # print ("")
    # print ("--------------------------------------")
    # print ("End of FilmListe")
    datei.write("\r" + "")
    datei.write("\r--------------------------------------")
    datei.write("\rEnd of FilmListe")

# Datei schliessen
datei.close()