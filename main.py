import os
import math
speech = [".\\speeches\\Nomination_Chirac1.txt",".\\speeches\\Nomination_Chirac2.txt",".\\speeches\\Nomination_Giscard dEstaing.txt",".\\speeches\\Nomination_Hollande.txt",".\\speeches\\Nomination_Macron.txt",".\\speeches\\Nomination_Mitterrand1.txt",".\\speeches\\Nomination_Mitterrand2.txt",".\\speeches\\Nomination_Sarkozy.txt"]


def no_double(lst:list):
    single = []
    for elt in lst:
        if elt[-1] == "1" or elt[-1] == "2":
            single.append(elt[:-1])
        else:
            single.append(elt)

    single2 = []
    for elt in single:
        if elt not in single2:
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
    special_char = ['-',"'"]
    for char in text:
        if char.isalpha() and char.isupper():
            char = char.lower()

        # Checking if the character is a special symbol
        if char in special_char:
            char = ' '
        if char== '.' or char == '!' or char == '?':
            char = ''

        cleaned_text += char
    return cleaned_text


def TF(text:str):
    frequency = {}
    cleaned_text = clean_text(text)
    words = cleaned_text.split(" ")
    for word in words:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1
    return frequency


def IDF(directory):
    file_names = []
    for filename in os.listdir(directory):
        if filename.endswith("txt"):
            file_names.append(filename)
    # Getting a list of all the files in the folder

    idf = {}
    total_words = []
    for text in file_names:
        f = open(f".\\{directory}\\{text}", "r")
        for line in f.readlines():
            for elt in list(TF(line).keys()):
                if elt not in total_words:
                    total_words.append(elt)
    # This is only to have a list of all the words in all the files

    for word in total_words:
        total_word_occurrence = 0
        for file in file_names:
            f = open(f".\\{directory}\\{file}", "r")
            line = f.readline()
            found = False
            while line != "" and found is False:
                if word in line:
                    found = True
                    total_word_occurrence += 1

        idf[word] = math.log(len(file_names)/total_word_occurrence)
    return idf


def TFIDF():
