def presidentNameExtract(listofspeech:list):
    names = []
    for filepath in listofspeech:
        names.append(os.path.basename(filepath)[:-4].split("_")[1]) 
        # the os.path part is to get only the entire file name, and the split() part is to get rid of "Nomination_"

    last_name_of_president = no_double(names)
    return last_name_of_president
