import os
from datetime import datetime as DateTime

# Pfad zu den Filmen
FilmPfad = "/Volumes/osx home/kodi2020"

# Liste aller Unterverzeichnissen erstellen
FilmListe = os.listdir(FilmPfad)

# Apple Verzeichnis-Zeugs entfernen
FilmListe.remove(".DS_Store")


# FilmListe.sort()

# Listen Kopf schreiben
print ("Anzahl Filme: " + str(len(FilmListe)))
print ("Uhrzeit: " + DateTime.now().strftime('%H:%M:%S'))
print ("-------------------------------")

# alle Filme in der Liste zeilenweise ausgeben
i = 1
erstesZeichenAlt = ""

for FilmName in FilmListe:
    erstesZeichen = FilmName[0]
    if erstesZeichen == erstesZeichenAlt:
        print (str(i) + ": " + FilmName)
    else:
        print("")
        print ("--- " + erstesZeichen + " ---")
        print (str(i) + ": " + FilmName)
    erstesZeichenAlt = erstesZeichen
    i = i + 1

print ("")
print ("--------------------------------------")
print ("End of FilmListe")