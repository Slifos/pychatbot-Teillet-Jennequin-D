from fonction import *
from fonction_bis import *
import os


choix = int(input("Taper 1 pour accèder aux fonctionnalités, taper 2 pour accéder au mode tchatBot :"))
while choix != 1 and choix != 2:
    choix = int(input("Erreur !\nResaisissez votre choix :"))
if choix == 1:
    if __name__ == "__main__":
        f_cleaned("./speeches/")
        tfidf = tf_idf("./cleaned/")

        #PARTIE 1
        print("Voulez vous savoir la matrice tf-idf des discours des anciens présidents français?")
        rep = input("oui/non")
        rep = rep.lower()
        if rep == "oui":
            print(tfidf)

        print("Voulez vous savoir les mots ayant les plus petits tf-idf?")
        rep = input("oui/non")
        rep = rep.lower()
        if rep == "oui":
            print(pas_important(tfidf))

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

else:
    if __name__ == "__main__":
        f_cleaned("./speeches/")
        tfidf = tf_idf("./cleaned/")

    #PARTIE 2
    chain = input("Posez votre question :")
    L_token = token(chain)
    n = intersection("chirac", L_token)
    n = tf_idf("./cleaned/")
    m = tfidf_token(chain)
    a = pertinent(n, m)
    g = grand_tfidf(m)
    rep = réponse(n, m, chain)

    print(rep)
