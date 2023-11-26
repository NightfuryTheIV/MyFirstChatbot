import os
from fonctions import clean_adding
speech = os.listdir("speeches")


cleaned_speeches = ["Cleaned_Nomination_Chirac1.txt", "Cleaned_Nomination_Chirac2.txt",
                    "Cleaned_Nomination_Giscard dEstaing.txt", "Cleaned_Nomination_Hollande.txt",
                    "Cleaned_Nomination_Macron.txt", "Cleaned_Nomination_Mitterrand1.txt",
                    "Cleaned_Nomination_Mitterrand2.txt", "Cleaned_Nomination_Sarkozy.txt"]

directory = 'cleaned'

# presidents = presidentNameExtract(speech)


"""
#Lower case
if __name__ == "main":
    input_folder = "speeches"
    output_folder = "cleaned"
    convert_to_lowercase_and_save(input_folder, output_folder)


#Remove ponctuation
for i in cleaned_speeches:
    remove_ponctuation(i)
print()
print("Conversion to lowercase and saving completed.")
print()


#TF
for i in cleaned_speeches:
    TF(i)

#IDF
IDF(directory)

#TF_IDF
TF_IDF(directory)
'''print(matrice_result)'''
'''print(TF_IDF_values)'''


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