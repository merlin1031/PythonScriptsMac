import os

FilmPfad = "/Volumes/osx home/kodi2020"

FilmListe = os.listdir(FilmPfad)
print (FilmListe)
print (FilmListe.__sizeof__())
print ("Anzahl Filme: " + str(len(FilmListe)))
