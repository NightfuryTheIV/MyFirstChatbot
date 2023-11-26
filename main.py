import os
import math
speech = os.listdir("speeches")

#Presidents last name
for i in speeches:

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
            with open(file_path, 'r', encoding="utf-8") as file:
                unique_words_in_doc = set()  # Set used to discard duplicates

                for line in file:
                    line = clean_text(line)
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

"""
def TFIDF(directory):
    tfidf_matrix = []

    for filename in os.listdir(directory):
        if filename.endswith("txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                set_of_words = set()  # Set used to discard duplicates

    for row in range(len(set_of_words)):
        tmp_list = []
        for column in range(len(os.listdir(directory))):
            f = open(f".\\{directory}\\{os.listdir(directory)[column]}")
            lineTF = 0
            for line in f.readlines():
                lineTF += TF(line)[set_of_words[row]]
            print(lineTF*IDF(directory)[list(IDF(directory).keys())[row]])
            tmp_list.append(lineTF*IDF(directory)[list(IDF(directory).keys())[row]])
        tfidf_matrix.append(tmp_list)

    return tfidf_matrix


print(TFIDF("speeches")
"""


def TF_IDF(directory):
    idf = IDF(directory)
    file_names = os.listdir(f".\\{directory}\\..\\cleaned")
    nofiles = len(file_names)
    tfidf = {}
    os.chdir('cleaned')

    for word in idf.keys():
        tfidf[word] = []

    for i in range(nofiles):
        with open(file_names[i], "r", encoding="utf-8") as f:
            tf = {}
            for line in f:
                dico_temp = TF(line)
                for word in dico_temp.keys():
                    if word not in tf.keys():
                        tf[word] = dico_temp[word]
                    else:
                        tf[word] += dico_temp[word]
            dico_tfidf = {}

            for word in tf.keys():
                word_tfidf = tf[word]*idf[word]
                dico_tfidf[word] = word_tfidf

            for word in idf.keys():
                if word not in dico_tfidf.keys():
                    tfidf[word].append(0)
                else:
                    tfidf[word].append(dico_tfidf[word])
    os.chdir('..')
    return tfidf