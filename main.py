import os
from fonctions import *
speech = os.listdir("speeches")

TF_IDF("speeches")

"""
#Features
matrice_result = TF_IDF(directory)

#Nonimportant
print(TF_IDF_nonimportant_value(matrice_result))

#Hightest value
print(TF_IDF_highest_value(matrice_result))

#First person to speak of écology or climat
eco(directory)

#Words said by all président
print("They are",All_said(matrice_result))

#Who spoke of Nation and the most
print(TF_IDF_highest_value_word(matrice_result))

#Most repeted word by Chirac
print(TF_IDF_most_word_repeat(matrice_result,"Chirac"))
"""

clean_adding()