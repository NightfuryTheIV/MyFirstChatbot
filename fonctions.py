import math
import os


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


def presidentNameExtract(listofspeech:list):
    names = []
    for filepath in listofspeech:
        names.append(os.path.basename(filepath)[:-4].split("_")[1]) 
        # the os.path part is to get only the entire file name, and the split() part is to get rid of "Nomination_"

    last_name_of_president = no_double(names)
    return last_name_of_president


firstnamespresidents = {"de Gaulle": "Charles", "Pompidou": "Georges", "Giscard dEstaing": "Valéry", "Mitterrand": "François", "Chirac": "Jacques", "Sarkozy": "Nicolas", "Hollande": "François", "Macron": "Emmanuel"}
# This is the dictionary containing the names of all the French presidents of the Fifth Republic


def display_full_names():
    for elt in presidentNameExtract(os.listdir("speeches")):
        print(f"{firstnamespresidents[elt]} {elt}")


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


def clean_adding():
    for file in os.listdir("speeches"):
        with open(f".\\cleaned\\Cleaned_{file}", "w", encoding="utf-8") as clean:
            with open(f".\\speeches\\{file}", "r") as f:
                for line in f.readlines():
                    clean.write(clean_text(line))
    return True


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


def TF_IDF(directory):
    idf = IDF(directory)
    file_names = os.listdir(f".\\cleaned")
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

    # turning this tfidf dictionary into a usable matrix
    keys = list(tfidf.keys())
    values = list(tfidf.values())
    matrix = [[values[j][i] for j in range(len(values)) for i in range(len(values[0]))]]

    return matrix

