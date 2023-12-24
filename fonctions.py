import math
import os


all_words = []
path = os.getcwd()
print(path)

for w in range(len(os.listdir("cleaned"))):
    filepath = os.path.join(path, "cleaned", list(os.listdir("cleaned"))[w])
    with open(filepath, "r") as file:
        for line in file.readlines():
            for word in line.split():
                if word not in all_words:
                    all_words.append(word)


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
        'ï': 'i', 'í': 'i', 'ç': 'c', 'œ': 'oe'
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
    words = text.strip().split()
    frequency = {word: words.count(word) for word in set(words)}
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


def word_idf(directory, word):
    total_documents = len(os.listdir(directory))

    # Count the number of documents containing the word
    document_frequency = sum(1 for filename in os.listdir(directory) if word_in_file(os.path.join(directory, filename), word))

    if document_frequency > 0:
        idf = round(math.log10(total_documents / document_frequency), 2)
    else:
        idf = 0
    return idf


def word_in_file(file_path, word):  # We only use it in case something goes horribly wrong, we can consider it a safety belt
    with open(file_path, 'r', encoding='utf-8') as text:
        return word in text.read().strip()


def TFIDF_dict(directory):
    # Dictionary to store TF values for each word in each file
    tf_values = {word: [0] * len(os.listdir(directory)) for word in all_words}

    # Calculate TF values for each word in each file
    for i, filename in enumerate(os.listdir(directory)):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                # Calculate TF values using the provided TF function
                tf_dict = TF(file.read().strip())

                # Update TF values only for words in unique_words
                for word in set(tf_dict.keys()) & set(all_words):
                    tf_values[word][i] = tf_dict[word]

    # Dictionary to store IDF scores for each word
    idf_scores = {word: word_idf(directory, word) for word in all_words}

    # Dictionary to store TF-IDF scores for each word in each file
    tf_idf_matrix = {word: [tf_values[word][k] * idf_scores[word] for k in range(len(tf_values[word]))] for word in all_words}

    return tf_idf_matrix


president_tfidf = TFIDF_dict("cleaned")


def least_important_word():  # feature 1
    least = []
    for row in range(len(president_tfidf)):
        for column in range(len(president_tfidf[0])):
            if president_tfidf[row][column] == 0:
                least.append(president_tfidf[row][column])
    return least  # This function has to be used with the TFIDF function


def highest_TDIDF():  # feature 2
    highest = []
    maxi = president_tfidf[0][0]
    for row in range(len(president_tfidf)):
        for column in range(len(president_tfidf[0])):
            if president_tfidf[row][column] > maxi:
                maxi = president_tfidf[row][column]

    for row in range(len(president_tfidf)):
        for col in range(len(president_tfidf[0])):
            if president_tfidf[row][col] == maxi:
                highest.append(all_words[row])  # long line to get the word, not the index

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






def tokenize(question:str):
    return simple_clean(question).split(" ")


def question_words(tokens:list):
    meaningful_words = []  # filtering out the terms that aren't in the corpus
    for j in range(len(tokens)):
        if tokens[j] in all_words:
            meaningful_words.append(tokens[j])
    return meaningful_words


def question_vector(tokens:list):
    TF_question = {}
    for j in range(len(tokens)):
        if tokens[j] in TF_question:
            TF_question[tokens[j]] += 1
        else:
            TF_question[tokens[j]] = 1

    TF_IDF_question = {}

    for key, value in TF_question.items():
        TF_IDF_question[key] = value * IDF("cleaned")[key]
    return TF_IDF_question


def scalar(vector1:list, vector2:list):
    scalar_value = 0

    for i in range(len(vector1)):
        scalar_value += vector1[i] * vector2[i]
    return scalar_value


def norm(a:list):
    somme = 0
    for coordinate in a:
        somme += coordinate**2
    return math.sqrt(somme)


def similarity(v1:list, v2:list):
    result = 0
    if norm(v1) * norm(v2) != 0:
        result = scalar(v1, v2) / (norm(v1) * norm(v2))
    return result


def relevancy(question_TFIDF, filenames):  # I don't believe we need the corpus TF-IDF...
    similarities = {}
    current = os.getcwd()

    for i in range(len(os.listdir(filenames))):
        filepath = os.path.join(current, "cleaned", "Cleaned_" + os.listdir(filenames)[i])
        with open(filepath, 'r') as text:
            singleline = ""
            for line in text.readlines():
                singleline += line

            doc_token = question_vector(question_words(tokenize(singleline)))
            doc_copy = doc_token

            question_copy = question_TFIDF
            # Now we have vectors of the same size

            similarities[filepath] = similarity(list(question_copy.values()), list(doc_copy.values()))

    maximum = similarities[list(similarities.keys())[0]]
    maxkey = ""
    for key, value in similarities.items():
        if value > maximum:
            maxkey = key

    return maxkey


def speeches_eq(path):  # This will return the equivalent file in the speeches folder
    path_chain = path.split("\\")
    path_chain[-2] = "speeches"
    path_chain[-1] = path_chain[-1][8:]
    real_path = "\\".join(path_chain)
    return real_path


def response(question):
    vector = question_vector(question_words(tokenize(question)))
    keyword = list(vector)[0]

    for key, value in vector.items():
        if value > vector[keyword]:
            keyword = key

    most_relevant_doc = speeches_eq(relevancy(vector, "speeches"))

    with open(most_relevant_doc, "r") as doc:
        save_line = ""

        for linee in doc.read().split("\n"):
            if keyword in linee:
                save_line = linee

        print("question: ", question)
        print("Relevant document returned: ", most_relevant_doc)
        print("Word that is likely to be what you're looking for: ", keyword)
        print("Response generated: ", save_line)
    return save_line


def conveniency(question):
    return response(question_vector(question_words(tokenize(question))))


QUESTION_STARTERS = {
    "comment": "Après analyse, ",
    "pourquoi": "Car, ",
    "qui": "La personne responsable de cela est ",
    "combien": "Au total il y a ",
    "est-ce que": "Il est possible que ",
    "peut-on": "Oui, il est possible de ",
    "serait-il possible": "Il est envisageable de ",
    "comment faire": "Voici comment procéder : ",
    "quelle est la raison": "La raison principale est ",
    "est-ce que tu peux": "Oui, je peux ",
    "est-ce que tu sais": "Oui, je sais que ",
    "peux-tu": "Oui, je peux ",
}

reponse = "###    mettre la phrase réponse    ###"


def final_answer(question: str, phrase: str):
    phrase = phrase.strip() + "."
    for key in QUESTION_STARTERS:
        if question.startswith(key,0,25):
            phrase = phrase[0].upper() + phrase[1:]
            phrase = QUESTION_STARTERS[key] + phrase
        else:
            phrase = "Sorry, I don't understand your query."
    print(phrase)


question = input("Hello sir! Might you have a question for humble me, you shall pose it here in this dedicated area. ")
final_answer(question, reponse)
