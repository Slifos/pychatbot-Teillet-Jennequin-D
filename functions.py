import re
def est_sous_chaine(chaine, sous_chaine):
    return sous_chaine in chaine

#extraction des noms à partir des documents
def extraire_noms(noms_fichiers):
    noms_presidents = []
    for nom_fichier in noms_fichiers:
        nom_president = re.sub(r'Nomination_|\.txt|\d$', '', nom_fichier)
        noms_presidents.append(nom_president)
    return noms_presidents