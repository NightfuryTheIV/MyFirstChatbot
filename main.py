import os.path
from os import path
speech = [".\\.idea\\inspectionProfiles\\Nomination_Chirac1.txt",".\\.idea\\inspectionProfiles\\Nomination_Chirac2.txt",".\\.idea\\inspectionProfiles\\Nomination_Giscard dEstaing.txt",".\\.idea\\inspectionProfiles\\Nomination_Hollande.txt",".\\.idea\\inspectionProfiles\\Nomination_Macron.txt",".\\.idea\\inspectionProfiles\\Nomination_Mitterrand1.txt",".\\.idea\\inspectionProfiles\\Nomination_Mitterrand2.txt",".\\.idea\\inspectionProfiles\\Nomination_Sarkozy.txt"]


def prototype(listofspeech:list):
    names = []
    for filepath in listofspeech:
        names.append(os.path.basename(filepath)[:-4].split("_")[1])
    return names


prototype(speech)

"""
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


firstnamespresidents = {"de Gaulle": "Charles", "Pompidou": "Georges", "Giscard dEstaing": "Valéry", "Mitterrand": "François", "Chirac": "Jacques", "Sarkozy": "Nicolas", "Hollande": "François", "Macron": "Emmanuel"}


def full_names():
    namae = []
    for name in presidentNameExtract():
        namae.append(f"{firstnamespresidents[name]} {name}")

    tmp = []
    for i in range(len(namae)):
        if namae[i] != namae[i-1]:
            tmp.append(namae[i])

    for name in tmp:
        print(name)


full_names()
"""
# faudra revoir la fonciton 2 pq apparemment faut que ce soit une vraier fonction ou qqch