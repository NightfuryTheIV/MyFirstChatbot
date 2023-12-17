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


def remove_accents(input_text):
    # Function we will use to clean the texts
    accent_mapping = {
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'à': 'a', 'â': 'a', 'ä': 'a', 'á': 'a',
        'ô': 'o', 'ö': 'o', 'ó': 'o', 'ò': 'o', 'û': 'u', 'ü': 'u', 'ù': 'u', 'î': 'i',
        'ï': 'i', 'í': 'i', 'ç': 'c',
    }
    return ''.join(accent_mapping.get(char, char) for char in input_text)


def remove_punctuation(input_text):
    # Function we will also use to clean the texts
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    translator = str.maketrans(punctuation_chars, ' ' * len(punctuation_chars))
    return input_text.translate(translator)


def clean_files(input_folder):
    # Just checking if the cleaned folder exists
    cleaned_folder_path = os.path.join(os.getcwd(), "cleaned")
    if not os.path.exists(cleaned_folder_path):
        os.makedirs(cleaned_folder_path)

    # Listing all the files to clean
    files = [file for file in os.listdir(input_folder) if file.endswith(".txt")]

    for file_name in files:
        # Input file path
        input_file_path = os.path.join(input_folder, file_name)

        # Output file path in the "cleaned" directory
        output_file_path = os.path.join(cleaned_folder_path, "Cleaned_"+file_name)

        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            # Read the content of the file
            content = input_file.read()

            # Convert to lowercase
            content = content.lower()

            # Remove accents if necessary
            content = remove_accents(content)

            # Remove punctuation characters and replace with space
            content = remove_punctuation(content)

            # Write the cleaned content to the new file
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(content)


def simple_clean(input_text):
    cleaned_text = input_text.lower()
    cleaned_text = remove_accents(cleaned_text)
    cleaned_text = remove_punctuation(cleaned_text)

    return cleaned_text


def TF(text: str):
    frequency = {}
    for word in text:
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
                    line = simple_clean(line)
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
        idfscore = round(math.log10(total_documents / frequency), 1)
        idf[single_word] = idfscore
    return idf


def TFIDF(directory):
    tfidf = []
    for i in range(len(os.listdir(directory))):
        tfidf.append(list(IDF(directory).values()))  # we do this to have a matrix already ready to become a TF-IDF matrix (after we transpose it)

    for fileno in range(len(os.listdir("cleaned"))):  # sifting through all the files in the folder using the index fileno of the files
        if os.listdir("cleaned")[fileno].endswith("txt"):
            file_path = os.path.join(directory, os.listdir("cleaned")[fileno])
            with open(file_path, 'r', encoding="utf-8") as file:
                for word in range(len(list(IDF("cleaned").keys()))):  # this is just to get all the words in the corpus
                    if list(IDF("cleaned").keys())[word] not in TF(simple_clean(str(file))):  # Since not every word in the corpus is in every file, the TF will have "empty" values, and thus we have to keep that in mind
                        tfidf[fileno][word] = 0
                    else:
                        tfidf[fileno][word] *= TF(simple_clean(str(file)))[list(IDF("cleaned").keys())[word]]  # Getting the word from its index proved trickier than expected...

    transpose = [[tfidf[j][i] for j in range(len(tfidf))] for i in range(len(tfidf[0]))]  # this is fairly straight-forward, we did this because looping words inside files was easier than the inverse, but now we need it in order.

    return transpose


# FEATURES

matrixscore = TFIDF("cleaned")


def least_important_word(TFIDF:list):  # feature 1
    least = []
    for row in range(len(TFIDF)):
        for column in range(len(TFIDF[0])):
            if TFIDF[row][column] == 0:
                least.append(TFIDF[row][column])
    return least  # This function has to be used with the TFIDF function


def highest_TDIDF(TFIDF:list):  # feature 2
    highest = []
    maxi = TFIDF[0][0]
    for row in range(len(TFIDF)):
        for column in range(len(TFIDF[0])):
            if TFIDF[row][column] > maxi:
                maxi = TFIDF[row][column]

    for row in range(len(TFIDF)):
        for col in range(len(TFIDF[0])):
            if TFIDF[row][col] == maxi:
                highest.append(list(IDF("cleaned"))[row])  # long line to get the word, not the index

    return highest


def highest_chirac():  # feature 3
    with open("cleaned\\Cleaned_Nomination_Chirac1.txt", "r") as chirac1:
        TF1 = TF(chirac1.read())
        maxi = TF1[list(TF1.keys())[0]]
        for word in TF1:
            if TF1[word] > TF1[maxi]:
                maxi = word

    with open("cleaned\\Cleaned_Nomination_Chirac2.txt", "r") as chirac2:
        TF2 = TF(chirac2.read())
        for word in TF2:
            if TF2[word] > TF2[maxi]:
                maxi = word

    chirac = []

    with open("cleaned\\Cleaned_Nomination_Chirac1.txt", "r") as chirac1:
        TF1 = TF(chirac1.read())
        for word, value in TF1.items():
            if value == maxi:
                chirac.append(word)

    with open("cleaned\\Cleaned_Nomination_Chirac2.txt", "r") as chirac2:
        TF2 = TF(chirac2.read())
        for word, value in TF2.items():
            if value == maxi:
                chirac.append(word)

    filtered = []  # Filtering out the duplicates
    for elt in chirac:
        if elt not in filtered:
            filtered.append(elt)

    return filtered


def nation(directory):  # feature 4
    files = os.listdir(directory)
    presidents = []
    nations_dico = {}
    for file in range(len(files)):
        president = presidentNameExtract(os.listdir("speeches"))[file]
        with open(f".\\{directory}\\{files[file]}") as f:
            nations = 0
            for line in f.readlines():
                lineTF = TF(line)
                nations += lineTF["nation"]
            nations_dico[president] = nations
        if nations > 0:
            presidents.append(presidentNameExtract(os.listdir("speeches"))[file])

    maxi = list(nations_dico.keys())[0]
    for key in nations_dico.keys():
        if nations_dico[key] > nations_dico[maxi]:
            maxi = key

    print("The president that mentions the most 'nation' is ", maxi)
    return presidents


def find_first_president_to_mention_ecology_or_climate(directory):
    os.chdir(directory)
    president = []
    file_names = os.listdir("..\\MyFirstChatbot\\cleaned")
    word_count = []
    for i in range(len(os.listdir(directory))):
        count = 0
        with open(file_names[i], "r") as file:
            for line in file:
                words = line.split(" ")
                for word in words:
                    if word == "climat" or word == "écologie":
                        president.append(file_names[i])
                    else:
                        count += 1
            word_count.append(count)
    lowest_count = min(word_count)
    lowest_president = ''
    for i in range(len(word_count)):
        if word_count[i] <= lowest_count:
            lowest_president = president[i]
    parts = lowest_president.split("_")
    president_name = ''
    for part in parts:
        if part != "Cleaned" and part != "Nomination" and part != "txt":
            president_name = part.replace(".txt", "")
            break
    print(f"First president to speak of climat or écologie is {president_name}")
    return president_name


