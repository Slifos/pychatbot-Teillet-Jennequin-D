import os
import math


def extraire_noms(directory: str):
    """extraire les noms des présidents à partir des noms des fichiers"""
    noms_fichiers = list_of_files(directory, ".txt")
    noms_presidents = []
    for nom_fichier in noms_fichiers:
        nom_president = nom_fichier.replace("Nomination_", "", 1)
        nom_president = nom_president.replace(".txt", "", 1)
        for i in range(10):
            nom_president = nom_president.replace(str(i), "", 1)

        if not (nom_president in noms_presidents):
            noms_presidents.append(nom_president)
    return noms_presidents


def cleaned(char):
    """récupère une chaine de caractère pour la rendre en minuscule et séparer chaque mot par des espaces tout en remplaçant les caractères spéciaux"""
    n = len(char)
    n_char = -1
    s = ""

    for elt in char:
        if elt == "§":  # ç
            s += "c"
            n_char += 1
        elif elt in "©ª¨ë":  # éêè
            s += "e"
            n_char += 1
        elif elt in "â":  # à
            s += "a"
            n_char += 1
        elif elt == "¹":  # ù
            s += "u"
            n_char += 1
        elif elt in "Ã":
            s = s
        elif ord(elt) >= 65 and ord(elt) <= 90:
            s += chr(ord(elt) + 32)
            n_char += 1

        elif ord(elt) >= 97 and ord(elt) <= 122:
            s += elt
            n_char += 1
        elif s != "" and s[n_char] != " ":
            s += " "
            n_char += 1

    # print(s)
    return s


def list_of_files(directory, extension):
    """récupère tous les noms de fichier d'une extension donnée à partir de son dossier"""
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def f_cleaned(directory):
    """Transfère les données d'un fichier à partir de son nom dans un autre tout en séparant chaque mot par des espaces"""
    directory_f = "./stopwords/"
    T_president = extraire_noms(directory)
    file = list_of_files(directory, ".txt")
    for elt in T_president:
        f2 = open(directory_f + elt + ".txt", 'w')
        for i in file:
            if elt in i:
                f = open(directory + i, 'r')
                lines = f.readlines()
                for line in lines:
                    ajout = cleaned(line)
                    f2.write(ajout)
            f.close()
        f2.close()


def mot(char):
    """retourne un tableau de mot unique dans une chaine de caractère avec des mots séparés"""
    T = []
    s = ""

    for elt in char:
        if elt == " ":
            if not (s in T):
                T.append(s)
            s = ""
        else:
            s += elt
    if s != "":
        T.append(s)
    return T


def tf(char):
    """retourne un dictionnaire avec le nb de chaque occurence pour chaque mot unique dans une chaine de caractère avec des mots séparés"""
    d = {}
    T = []
    s = ""
    for elt in char:
        if elt == " ":
            if s in T:
                d[s] = d[s] + 1
            else:
                T.append(s)
                d[s] = 1
            s = ""
        else:
            s += elt
    if s != "":
        T.append(s)
    # print(d)
    return d


def teste_occ(mot, list_T):
    """retourne le nb de fois qu'apparait un mot dans une liste 2D contenant des mots"""
    s = 0
    for i in list_T:
        for j in i:
            if j == mot:
                s += 1
    return s


def idf(directory):
    files = list_of_files(directory, ".txt")
    matrice_mot = []
    for elt in files:
        f = open(directory + elt, "r")
        line = f.read()
        T = mot(line)
        matrice_mot.append(T)
    d = {}
    n = len(matrice_mot)
    for i in matrice_mot:
        for j in i:
            d[j] = math.log(n / teste_occ(j, matrice_mot))
    # print(d)
    return d


def m_mot(directory):
    files = list_of_files(directory, ".txt")
    matrice_mot = []
    for elt in files:
        f = open(directory + elt, "r")
        line = f.read()
        T = mot(line)
        matrice_mot.append(T)
    return matrice_mot


def mot_2D(matrice_mot):
    """retourne un tableau de mot unique à partir d un tableau 2D remplie de mot"""
    T = []
    s = ""

    for elt in matrice_mot:
        for i in elt:
            if not (i in T):
                T.append(i)

    return T


def tf_idf(directory):
    matrice_mot = m_mot(directory)
    liste_mot = mot_2D(matrice_mot)
    T_president = extraire_noms(directory)
    d_idf = idf(directory)
    tfidf = [[0]]
    for elt in T_president:
        tfidf[0].append(elt)
    for i in range(len(liste_mot)):
        tfidf.append([])
        tfidf[1 + i].append(liste_mot[i])
    for i in range(1, len(tfidf[0])):
        f = open(directory + tfidf[0][i] + ".txt", 'r')
        line = f.read()
        d_tf = tf(line)
        T = mot(line)
        for j in range(1, len(tfidf)):
            if tfidf[j][0] in T:
                res = d_tf[tfidf[j][0]] * d_idf[tfidf[j][0]]
                tfidf[j].append(res)
            else:
                tfidf[j].append(0.0)
        f.close()
    return tfidf


def pas_important(t_2D):
    T = []
    for i in range(1, len(t_2D)):
        if t_2D[i][1:] == [0, 0, 0, 0, 0, 0]:
            T.append(t_2D[i][0])
    print(T)
    return T


def eleve(t_2D):
    T = []
    max = -1
    low = pas_important(t_2D)
    for i in range(1, len(t_2D)):
        s = 0
        for elt in t_2D[i][1:]:
            if elt not in low:
                s += elt
        if s > max :
            max = s
            T = [t_2D[i][0]]
        elif s == max:
            T.append(t_2D[i][0])
    print(T)


def chirac_mot():
    T = []
    max = -1
    f = open("./cleaned/Chirac.txt", 'r')
    line = f.read()
    d = tf(line)
    T_unique = mot(line)
    f.close()
    for elt in T_unique:
        if d[elt] > max:
            max = d[elt]
            T = [elt]
        elif d[elt] == max:
            T.append(elt)
    print(T)


def nation(t_2D):
    T = []
    i = 1
    max = -1
    max_president = "personne"
    while i < len(t_2D) and t_2D[i - 1][0] != "nation":
        if t_2D[i][0] == "nation":
            for j in range(1, len(t_2D[0])):
                f = open("./cleaned/" + t_2D[0][j] + ".txt")
                line = f.read()
                d = tf(line)
                if t_2D[i][0] in d.keys() and d[t_2D[i][0]] > 0:
                    T.append(t_2D[0][j])
                if t_2D[i][0] in d.keys() and d[t_2D[i][0]] > max:
                    max_president = t_2D[0][j]
        i += 1
    print(T, max_president)


def climat(t_2D):
    for i in range(1, len(t_2D[0])):
        f = open("./cleaned/" + t_2D[0][i] + ".txt", "r")
        line = f.read()
        d = tf(line)
        f.close()
        if "climat" in d.keys() or "ecologie" in d.keys():
            print(t_2D[0][i])
            return t_2D[0][i]


def tous_mots(t_2D):
    T=[]
    for i in range(1,len(t_2D)):
        verif=True
        for j in range(1,len(t_2D[0])):
            with opent("./cleaned/"+t_2D[0][j]+".txt",'r') as f1, open("./stopwords/") as f2:
            line = f1.readline()
            line_2 = f2.readline()
            T_mot = mot(line)
            if not(t_2D[i][0] in T_mot and t_2D[i][0] in ):
                verif=False
            f.close()
        if verif==True:
            T.append(t_2D[i][0])
    print(T)
