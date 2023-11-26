import os
from functions import *

#extraction des noms des documents
noms_fichiers = list_of_files('speeches', '.txt')
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

test = conversion_minuscule()