def est_sous_chaine(chaine, sous_chaine):
    return sous_chaine in chaine

# Exemple d'utilisation
chaine_principale = "Bonjour, comment ça va ?"
sous_chaine_a_verifier = "comment"

if est_sous_chaine(chaine_principale, sous_chaine_a_verifier):
    print(f"{sous_chaine_a_verifier} est une sous-chaîne de {chaine_principale}")
else:
    print(f"{sous_chaine_a_verifier} n'est pas une sous-chaîne de {chaine_principale}")