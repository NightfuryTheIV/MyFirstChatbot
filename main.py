from os import listdir
from fonctions import *
import math
speech = os.listdir("speeches")

presidents = presidentNameExtract(speech)
# The dictionary associating the last names with first names is in fonctions.py, line 30.

clean_files("speeches")

# TF, IDF, and TF-IDF functions are in fonctions.py, from line 65 to line 147


def monologue():
    monolog = [
        "First step was to split your question into tokens that we use in three other functions to process everything we need to in order to give a valid answer.",
        "This function does work, there's no issue on this end.",
        "Then, we have another function determine the most important word of your question, the keyword.",
        "This part works sometimes but some common words like parlé can break it.",
        "Third step is to find the document in which the answer is the most likely to be. In theory it works.",
        "Last step is to pick out the first line of the document in which the keyword is but for some obscure reason, this step specifically doesn't return anything."]

    max_line_length = 0
    for line in monolog:
        if len(line) > max_line_length:
            max_line_length = len(line)
    max_line_length += 4

    first_line = ""
    for topbar in range(max_line_length):
        first_line += "_"
    first_line = " " + first_line
    print(first_line)

    for line in monolog:
        emptyspace = ""
        for emptyspaces in range(max_line_length - len(line)):
            emptyspace += " "
        print("| " + emptyspace[2:(len(emptyspace)+2)//2] + line + emptyspace[(len(emptyspace)+2)//2:] + " |")  # This centers the text

    print(first_line)


def boot_up():
    action1 = input(
        "Hello there! You can test out our application by typing Y, F to see our features, or any other key to exit. ")
    if action1 == "Y":
        question = input("Hello sir! Might you have a question for us, you shall pose it here in this dedicated area. ")
        final_answer(question, reponse)
        if response(question) == "":
            print("There might be an issue with the answer generation again.")
            action2 = input(
                "But I can explain to you in a simple way how it's supposed to generate an answer if you'd like. [Y for yes, any other key for no] ")
            if action2 == "Y":
                monologue()
            else:
                print("Very well then. Have a nice day.")

    elif action1 == "F":

        choix1 = input("")
        if choix1 == "1":
            print(least_important_word())
        elif choix1 == "2":
            print(highest_TDIDF())
        elif choix1 == "3":
            print(highest_chirac())
        elif choix1 == "4":
            print(nation("cleaned"))
        elif choix1 == "5":
            print(find_first_president_to_mention_ecology_or_climate("cleaned"))
        else:
            choix2 = input("A miss-click perhaps? ")

            if choix2 == "1":
                print(least_important_word())
            elif choix2 == "2":
                print(highest_TDIDF())
            elif choix2 == "3":
                print(highest_chirac())
            elif choix2 == "4":
                print(nation("cleaned"))
            elif choix2 == "5":
                print(find_first_president_to_mention_ecology_or_climate("cleaned"))
            else:
                print("Very well. Exiting.")
    else:
        print("Very well. Have a nice day.")


monologue()