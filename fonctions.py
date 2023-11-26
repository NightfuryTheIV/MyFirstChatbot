
def extract_name_president(name):
    president_name = name[11:]
    if ("1" in president_name) or ("2" in president_name):
        president_last_name = president_name[:-5]
    else:
        president_last_name = president_name[:-4]
    return president_last_name
