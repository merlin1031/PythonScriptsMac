import os
from datetime import datetime as DateTime

# Pfad zu den Filmen
FilmPfad = "/Volumes/osx home/kodi2020"

# Liste aller Unterverzeichnissen erstellen
FilmListe = os.listdir(FilmPfad)

# Apple Verzeichnis-Zeugs entfernen
FilmListe.remove(".DS_Store")

# Listen Kopf schreiben
print ("Anzahl Filme: " + str(len(FilmListe)))
print ("Uhrzeit: " + DateTime.now().strftime('%H:%M:%S'))
print ("-------------------------------")

# alle Filme in der Liste zeilenweise ausgeben
i = 1
for FilmName in FilmListe:
    print(str(i) + ": " + FilmName)
    i = i + 1

