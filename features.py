from fonctions import *
matrixscore = TF_IDF("speeches")


def least_important_word(TFIDF:list):  # feature 1
    least = []
    for row in range(len(TFIDF)):
        for column in range(len(TFIDF[0])):
            if TFIDF[row][column] == 0:
                least.append(TFIDF[row][column])
    return least  # This function has to be used with the TF_IDF function


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
                highest.append(matrixscore[list(matrixscore)[row]])  # long line to get the word, not the index

    return highest


def highest_chirac(TFIDF:list):  # feature 3
    chirac = []
    maxi = TFIDF[0][0]
    for row in range(len(TFIDF)):
        for column in range(2):  # because chirac's speeches are the first 2
            if TFIDF[row][column] > maxi:
                maxi = TFIDF[row][column]

    for row in range(len(TFIDF)):
        for col in range(len(TFIDF[0])):
            if TFIDF[row][col] == maxi:
                chirac.append(matrixscore[list(matrixscore)[row]])

    return chirac


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


def words_said_by_all_presidents(dico):
    list_all_said_words = []
    presidents_count = len(dico)  # Assuming dico is a dictionary containing TF-IDF values for each president

    for word, values in dico.items():
        if sum(1 for value in values if value >= 0.0) == presidents_count and word not in least_important_word(TF_IDF("speeches")):
            list_all_said_words.append(word)

    words_count = len(list_all_said_words)
    print(f"There are {words_count} words said by all presidents")
    return list_all_said_words
