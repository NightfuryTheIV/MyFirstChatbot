import os.path
from os import path
speech = [".\\.idea\\inspectionProfiles\\Nomination_Chirac1.txt",".\\.idea\\inspectionProfiles\\Nomination_Chirac2.txt",".\\.idea\\inspectionProfiles\\Nomination_Giscard dEstaing.txt",".\\.idea\\inspectionProfiles\\Nomination_Hollande.txt",".\\.idea\\inspectionProfiles\\Nomination_Macron.txt",".\\.idea\\inspectionProfiles\\Nomination_Mitterrand1.txt",".\\.idea\\inspectionProfiles\\Nomination_Mitterrand2.txt",".\\.idea\\inspectionProfiles\\Nomination_Sarkozy.txt"]


def presidentNameExtract(listofspeech:list):
    names = []
    for filepath in listofspeech:
        names.append(os.path.basename(filepath)[:-4].split("_")[1])
    return names


presidentNameExtract(speech)


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




def clean_text(text):
    cleaned_text = ""
    for char in text:
        # Convert uppercase characters to lowercase
        if char.isalpha() and char.isupper():
            char = char.lower()

        # Replace special characters with space
        if not char.isalnum():
            char = ' '

        cleaned_text += char
        
    print (cleaned_text)
    return cleaned_text

# faudra revoir la fonciton 2 pq apparemment faut que ce soit une vraier fonction ou qqch



