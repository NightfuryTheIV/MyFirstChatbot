def yoo():
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


speech = ["Nomination_Chirac1.txt","Nomination_Chirac2.txt","Nomination_Giscard dEstaing.txt","Nomination_Hollande.txt","Nomination_Macron.txt","Nomination_Mitterrand1.txt","Nomination_Mitterrand2.txt","Nomination_Sarkozy.txt"]


def presidentNameExtract():
    presidentList = []
    for i in speech:
        presidentName = i[11:]
        if "1" in presidentName or "2" in presidentName:
            presidentName = presidentName[:-5]
        else:
            presidentName = presidentName[:-4]
        presidentList.append(presidentName)
    return presidentList


firstnames = {"Chirac": "Jacques", "Giscard d'Estaing": "Valéry", "Hollande": "François", "Macron": "Emmanuel", "Mitterrand": "François"}