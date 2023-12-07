from fonction import *
import os

if __name__ == "__main__":
    f_cleaned("./speeches/")
    tfidf = tf_idf("./cleaned/")

    print("Voulez vous savoir la matrice tf-idf des discours des anciens présidents français?")
    rep = input("oui/non")
    rep = rep.lower()
    if rep == "oui":
        print(tfidf)

    print("Voulez vous savoir les mots ayant les plus petits tf-idf?")
    rep = input("oui/non")
    rep = rep.lower()
    if rep == "oui":
        pas_important(tfidf)

    print("Voulez vous savoir à l'inverse le ou les mots avec le plus grand tf-idf")
    rep = input("oui/non")
    rep = rep.lower()
    if rep == "oui":
        eleve(tfidf)
    print("Voulez vous savoir les mots les plus répétés par Chirac?")
    rep = input("oui/non")
    rep = rep.lower()
    if rep == "oui":
        chirac_mot()
    print("Voulez vous savoir quels présidents ont parlé de la nation et celui qui en a le plus parlé?")
    rep = input("oui/non")
    rep = rep.lower()
    if rep == "oui":
        nation(tfidf)

    print("Voulez vous savoir quel président a parlé du climat ou du theme lié à l'écologie en premier ?")
    rep = input("oui/non")
    rep = rep.lower()
    if rep == "oui":
        climat(tfidf)

    print("Voulez vous savoir quel mot tous les présidents ont au moins utilisé durant leur discours?")
    rep = input("oui/non")
    rep = rep.lower()
    if rep == "oui":
        tous_mots(tfidf)

