# -*- coding: iso-8859-1 -*-
myList = ['Hallo', 'Echo', 'Rainer', 'Rolf', 'Petra', 'Yoda', 'Laia', 'Han', 'C3PO', 'R2D2']
myList += ['Darth Vader', 'BD2', 'Lando', 'Endor', 'Tie Fighter', 'X-Wing', 'Y-Wing', 'B-Wing', 'A-Wing']
myList += ['Tatoine', 'Millenium Falke', 'Alderan', 'Todesstern']
myList += ['Östereich']
myList.sort() # Verhindert dass Buchstaben mehrmals aufkommen

text = "Inhalt mit UMlauten: ÄÖÜ "
print (text)
Mitarbeitertb
erstesZeichenAlt = ""
i = 1
for x in myList:
    erstesZeichen = x[0]
    if erstesZeichen == erstesZeichenAlt:
        print (str(i) + ": " + x)
    else:
        print (" ")
        print ("--- " + erstesZeichen + " ---")
        print (str(i) + ": " + x)
    erstesZeichenAlt = erstesZeichen
    i = i +1
