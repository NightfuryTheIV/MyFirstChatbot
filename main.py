from os import listdir
from fonctions import *
speech = os.listdir("speeches")

presidents = presidentNameExtract(speech)
# The dictionary associating the last names with first names is in fonctions.py, line 30.

clean_files("speeches")

# TF, IDF, and TF-IDF functions are in fonctions.py, from line 65 to line 147

boot_up()
