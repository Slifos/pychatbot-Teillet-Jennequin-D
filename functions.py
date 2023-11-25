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

def associer_prenom(noms_presidents):
    liste_prenoms = ['Jacques' , 'Jacques', 'Valéry ', 'François ', 'Emmanuel ', 'François', 'François', 'Nicolas']
    associations = {}
    for nom in noms_presidents:
        prenom = liste_prenoms.pop(0)
        associations[nom] = prenom
    return associations

def liste_noms(noms_presidents):
    noms_presidents = list(set(noms_presidents))
    return noms_presidents
