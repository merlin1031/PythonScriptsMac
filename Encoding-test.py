myList = ['Hallo', 'Echo']
myList.sort()

erstesZeichenAlt = ""
i = 1
for x in myList:
    erstesZeichen = x[0]
    if erstesZeichen == erstesZeichenAlt:
        print (str(i) + ": " + x)
    else:
        print ("--- " + erstesZeichen + " ---")
        print (str(i) + ": " + x)
    erstesZeichenAlt = erstesZeichen
    i = i +1
