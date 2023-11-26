import os
from fonctions import *
speech = os.listdir("speeches")

clean_adding()
TF_IDF("speeches")


"""
#First person to speak of écology or climat
eco(directory)

#Words said by all président
print("They are",All_said(matrice_result))

#Who spoke of Nation and the most
print(TF_IDF_highest_value_word(matrice_result))

#Most repeted word by Chirac
print(TF_IDF_most_word_repeat(matrice_result,"Chirac"))
"""

choix1 = int(input("HELLO USER! And welcome to our brand new Work In Progress on data pre-processing! We have all kinds of features that will soon be listed in README.md, but however right now you can do one of 6 things:\n1 display the last important words in all of the speeches combined,\n2 Display the words with the highest chances of being important,\n3 Show the most repeated word by Jacques Chirac, \n4 Show which presidents talked about 'Nation' in their speeches, \n5 Show the first president to care about climate change and ecology [WIP]\n6 Display all the meaningful words that have been employed by all the presidents [WIP]"))

if choix1 == 1:
    print()
