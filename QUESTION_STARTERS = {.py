QUESTION_STARTERS = {
    "comment": "Après analyse, ",
    "pourquoi": "Car, ",
    "qui": "La personne responsable de cela est ",
    "combien": "Au total il y a ",
    "est-ce que": "Il est possible que ",
    "peut-on": "Oui, il est possible de ",
    "serait-il possible": "Il est envisageable de ",
    "comment faire": "Voici comment procéder : ",
    "quelle est la raison": "La raison principale est ",
    "est-ce que tu peux": "Oui, je peux ",
    "est-ce que tu sais": "Oui, je sais que ",
    "peux-tu": "Oui, je peux ",
}
phrase="###    mettre la phrase réponse    ###"


def final_answer(question:str, phrase:str) -> str:
    phrase = phrase.strip() + "."
    for key in QUESTION_STARTERS:
        if(question.startswith(key,0,25)):
            phrase = phrase[0].upper() +phrase[1:]
            phrase = QUESTION_STARTERS[key] + phrase
    print(phrase)
    return phrase

question=input()
final_answer(question, phrase)