import os
speech = [".\\speeches\\Nomination_Chirac1.txt",".\\speeches\\Nomination_Chirac2.txt",".\\speeches\\Nomination_Giscard dEstaing.txt",".\\speeches\\Nomination_Hollande.txt",".\\speeches\\Nomination_Macron.txt",".\\speeches\\Nomination_Mitterrand1.txt",".\\speeches\\Nomination_Mitterrand2.txt",".\\speeches\\Nomination_Sarkozy.txt"]


def no_double(lst:list):
    single = []
    for elt in lst:
        if elt not in single:
            single.append(elt)

    single2 = []
    for elt in single:
        if elt[-1] == "1" or elt[-1] == "2":
            single2.append(elt[:-1])
        else:
            single2.append(elt)
    return single2
# This function will be used to avoid duplicates


def presidentNameExtract(listofspeech:list):
    names = []
    for filepath in listofspeech:
        names.append(os.path.basename(filepath)[:-4].split("_")[1]) # the os.path part is to get only the entire file name, and the split() part is to get rid of "Nomination_"

    names_nodouble = no_double(names)
    return names_nodouble


firstnamespresidents = {"de Gaulle": "Charles", "Pompidou": "Georges", "Giscard dEstaing": "Valéry", "Mitterrand": "François", "Chirac": "Jacques", "Sarkozy": "Nicolas", "Hollande": "François", "Macron": "Emmanuel"}
# This is the dictionary containing the names of all the French presidents of the Fifth Republic


def display_full_names():
    for elt in presidentNameExtract(speech):
        print(f"{firstnamespresidents[elt]} {elt}")


display_full_names()



def clean_text(text):
    cleaned_text = ""
    for char in text:
        if char.isalpha() and char.isupper():
            char = char.lower()

        # Checking if the character is a special symbol
        if not char.isalnum():
            char = ' '

        cleaned_text += char

    print(cleaned_text)
    return cleaned_text
