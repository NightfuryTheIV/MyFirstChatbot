def yoo():
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


speech = ["Nomination_Chirac1.txt","Nomination_Chirac2.txt","Nomination_Giscard dEstaing.txt","Nomination_Hollande.txt","Nomination_Macron.txt","Nomination_Mitterrand1.txt","Nomination_Mitterrand2.txt","Nomination_Sarkozy.txt"]


def presidentNameExtract():
    presidentName = ""
    presidentList = []
    for i in speech:
        presidentName = i[11:]
        if 1 or 2 in President_name:
            President_name=President_name[:-5]
        else:
            President_name=President_name[:-4]
        print (President_name)