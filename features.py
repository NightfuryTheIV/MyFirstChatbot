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

