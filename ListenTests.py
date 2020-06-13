liste = ["Anton", "Achim", "Michael", "Udo", "Xaver", "Micha", "Petra", "Udo2", "Rene", "Moritz", "Paul", "00A", "R2D2"]
liste.sort()

erstesZeichenAlt = ""
i = 1
for x in liste:
    erstesZeichen = x[0]
    if erstesZeichen == erstesZeichenAlt:
        print (str(i) + ": " + x)
    else:
        print ("--- " + erstesZeichen + " ---")
        print (str(i) + ": " + x)
    erstesZeichenAlt = erstesZeichen
    i = i +1
