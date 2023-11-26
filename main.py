import os
from fonctions import *
from features import *
speech = os.listdir("speeches")

clean_adding()
TF_IDF("speeches")


"""
#First person to speak of écology or climat
eco(directory)

#Words said by all président
print("They are",All_said(matrice_result))
"""

choix1 = int(input("HELLO USER! And welcome to our brand new Work In Progress on data pre-processing! We have all kinds of features that will soon be listed in README.md, but however right now you can do one of 6 things:\n1 display the last important words in all of the speeches combined,\n2 Display the words with the highest chances of being important,\n3 Show the most repeated word by Jacques Chirac, \n4 Show which presidents talked about 'Nation' in their speeches, \n5 Show the first president to care about climate change and ecology [WIP]\n6 Display all the meaningful words that have been employed by all the presidents [WIP]"))

if choix1 == 1:
    print(least_important_word(TF_IDF("speeches")))
elif choix1 == 2:
    print(highest_TDIDF(TF_IDF("speeches")))
elif choix1 == 3:
    print(highest_chirac(TF_IDF("speeches")))
elif choix1 == 4:
    print(nation(TF_IDF("speeches")))
elif choix1 == 5:
    print("Work in Progress!")
elif choix1 == 6:
    print("Work in Progress!")
else:
    print("Exiting")