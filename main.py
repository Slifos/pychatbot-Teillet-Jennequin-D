import os
from functions import *

dirPath = r"speeches"
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
print(result)
nom = ['Chirac', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Sarkozy']
for i in range(len(result)):
    for elt in nom:
        if elt in result[i]:
            result[i] = elt
print(result)
print('hey')