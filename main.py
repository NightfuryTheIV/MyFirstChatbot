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
    doc_frequency = {}
    total_documents = 0

    for filename in os.listdir(directory):
        if filename.endswith("txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                unique_words_in_doc = set()  # Set used to discard duplicates

                for line in file:
                    words = line.strip().split()
                    unique_words_in_doc.update(words)

                # Update the overall document frequency dictionary
                for word in unique_words_in_doc:
                    if word in doc_frequency:
                        doc_frequency[word] += 1
                    else:
                        doc_frequency[word] = 1

                total_documents += 1

    idf = {}

    for single_word, frequency in doc_frequency.items():
        # Calculate the inverse document frequency (IDF) for each word
        idfscore = math.log10(total_documents / frequency)
        idf[single_word] = idfscore

    return idf


def TFIDF(directory):
    tfidf_matrix = [[]]
    for row in range(len(IDF(directory))):
        tmp_list = []
        for column in range(len(os.listdir(directory))):
            f = open(f".\\{directory}\\{os.listdir(directory)[column]}")
            lineTF = 0
            for line in f.readlines():
                if list(IDF(directory))[row] in line:
                    lineTF += 1
            tmp_list.append(lineTF*IDF(directory)[list(IDF(directory).keys())[row]])
        tfidf_matrix.append(tmp_list)

    return tfidf_matrix
