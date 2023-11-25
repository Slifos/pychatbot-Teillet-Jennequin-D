import re
import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir('speeches'):
        if filename.endswith('txt'):
            files_names.append(filename)
    return files_names

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

def conversion():
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    print_list(files_names)