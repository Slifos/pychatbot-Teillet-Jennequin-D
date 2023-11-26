import re
import os
def list_of_files(directory: str, extension: str):
    '''extraction des noms des fichiers'''
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def extraire_noms(noms_fichiers : list):
    """extraire les noms des présidents à partir des noms des fichiers"""
    noms_presidents = []
    for nom_fichier in noms_fichiers:
        nom_president = re.sub(r'Nomination_|\.txt|\d$', '', nom_fichier)
        noms_presidents.append(nom_president)
    return noms_presidents

def associer_prenom(noms_presidents : list):
    """association d'un prénom à chaque président"""
    liste_prenoms = ['Jacques' , 'Jacques', 'Valéry ', 'François ', 'Emmanuel ', 'François', 'François', 'Nicolas']
    associations = {}
    for nom in noms_presidents:
        prenom = liste_prenoms.pop(0)
        associations[nom] = prenom
    return associations

def liste_noms(noms_presidents : list):
    """affichage de la liste des noms des présidents sans doublon"""
    noms_presidents = list(set(noms_presidents))
    return noms_presidents

def conversion_minuscule():
    """conversion des 8 fichiers en miniscules"""
    new_files = ['Nomination_Chirac1.txt', 'Nomination_Chirac2.txt', 'Nomination_Giscard dEstaing.txt', 'Nomination_Hollande.txt', 'Nomination_Macron.txt', 'Nomination_Mitterrand1.txt', 'Nomination_Mitterrand2.txt', 'Nomination_Sarkozy.txt']
    for file in new_files:
        input_file_path = os.path.join('speeches', file)
        output_file_path = os.path.join('cleaned', file)
        for filename in os.listdir('speeches'):
                with open(input_file_path, 'r') as f1 , open(output_file_path, 'w') as f2:
                    lines = f1.readlines()
                    for line in lines:
                        for caractere in line:
                            if (ord(caractere) >= 65) and (ord(caractere) <= 90):
                                val_ord = ord(caractere) + 32
                                f2.write(chr(val_ord))
                            else:
                                f2.write(caractere)
    return

def sup_ponctuation(filename: str):
    """Suppression de la ponctuation dans tous les fichiers textes du dossier cleaned"""
    for file in os.listdir('cleaned'):
        input_file_path = os.path.join('cleaned', file)
        output_file_path = os.path.join('cleaned', file)
        if file == filename:
            with open(input_file_path, 'r') as f1:
                lines = f1.readlines()
                for i in range(len(lines)):
                    updated_line = ""
                    for char in lines[i]:
                        if (ord(char) < 97) or (ord(char) > 122) and char not in ["'", '-']:
                            updated_line += ' '
                        else:
                            updated_line += char
                    lines[i] = updated_line + '\n'

            # Write the modified lines back to the file
            with open(output_file_path, 'w') as f2:
                f2.writelines(lines)
    return