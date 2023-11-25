import os
from functions import *

dirPath = r"speeches"
noms_fichiers = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
print(noms_fichiers)

#extraction des noms à partir des documents
noms_presidents = extraire_noms(noms_fichiers)
print(noms_presidents)

#associer prénom aux présidents
noms_prenoms = associer_prenom(noms_presidents)
print(noms_prenoms)

#afficher la liste des noms des présidents sans doublon
unique_noms_presidents = liste_noms(noms_presidents)
print(unique_noms_presidents)
