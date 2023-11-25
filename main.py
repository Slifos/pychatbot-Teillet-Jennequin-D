import os
from functions import *

dirPath = r"speeches"
noms_fichiers = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
print(noms_fichiers)

#extraction des noms à partir des documents
noms_presidents = extraire_noms(noms_fichiers)
print(noms_presidents)

